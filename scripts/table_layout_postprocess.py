"""Tabellen-Layout-Nachbearbeitung fuer den Word-Export (DOCX).

Optimiert jede Tabelle im Export:
1. cantSplit auf jeder Zeile: Zeilen werden an Seitenumbruechen nicht durchtrennt.
2. Spaltenbreiten proportional zur Textlast: Breitere Spalten fuer mehr Inhalt
   statt starrer Pandoc-Gleichverteilung.
3. Tabellenschriftart auf 9 pt verkleinert fuer saubere Platznutzung.
4. Feste Tabellenbreite auf 100 % der Satzspiegelbreite.

Aufruf (immer NACH pagenum_postprocess.py):
    python 05_assets/table_layout_postprocess.py "02_export/Dokument.docx"
"""
import sys, zipfile, os, shutil
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
from lxml import etree

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
def w(t): return f"{{{W}}}{t}"

TOTAL_DXA = 9026      # Nominale Satzspiegelbreite A4 in dxa
TABLE_W_PCT = 5000    # 100 % Textbreite (5000 = 100%)
FONT_HALFPT = "18"    # 9 pt (Halbpunkte); Standard-Schriftgrad fuer Tabellen
MIN_WEIGHT = 6        # Mindestgewicht fuer schmale Spalten

def cell_text(tc):
    return "".join(t.text or "" for t in tc.iter(w("t"))).strip()

def first_child(parent, tag):
    el = parent.find(w(tag))
    if el is None:
        el = etree.Element(w(tag))
        parent.insert(0, el)
    return el

def process(path):
    zin = zipfile.ZipFile(path, "r")
    names = zin.namelist()
    doc = etree.fromstring(zin.read("word/document.xml"))

    n_tbl = 0
    n_width = 0
    for tbl in doc.iter(w("tbl")):
        n_tbl += 1
        rows = [c for c in tbl if c.tag == w("tr")]
        grid = tbl.find(w("tblGrid"))
        cols = grid.findall(w("gridCol")) if grid is not None else []
        ncols = len(cols)

        # 1. Spaltengewichte berechnen
        if ncols:
            first_row_cells = [c for c in rows[0] if c.tag == w("tc")] if rows else []
            first_row_texts = [cell_text(c).strip() for c in first_row_cells] if first_row_cells else []
            
            # Spezialfall: Abkuerzungsverzeichnis (Kuerzel / Bedeutung)
            if ncols == 2 and first_row_texts and any(x in first_row_texts[0].lower() for x in ["kürzel", "kuerzel", "abkürzung"]):
                weights = [20, 80]
            else:
                weights = [MIN_WEIGHT] * ncols
                for tr in rows:
                    cells = [c for c in tr if c.tag == w("tc")]
                    if len(cells) == ncols:
                        for i, tc in enumerate(cells):
                            weights[i] = max(weights[i], len(cell_text(tc)))
            
            tot = sum(weights)
            dxa = [max(1, round(TOTAL_DXA * x / tot)) for x in weights]
            pct = [max(1, round(TABLE_W_PCT * x / tot)) for x in weights]
            dxa[-1] += TOTAL_DXA - sum(dxa)
            pct[-1] += TABLE_W_PCT - sum(pct)

            for i, gc in enumerate(cols):
                gc.set(w("w"), str(dxa[i]))
            for tr in rows:
                cells = [c for c in tr if c.tag == w("tc")]
                if len(cells) == ncols:
                    for i, tc in enumerate(cells):
                        tcPr = first_child(tc, "tcPr")
                        tcW = tcPr.find(w("tcW"))
                        if tcW is None:
                            tcW = etree.Element(w("tcW")); tcPr.insert(0, tcW)
                        tcW.set(w("type"), "pct"); tcW.set(w("w"), str(pct[i]))
            n_width += 1

        # 2. Tabelle auf feste Breite (100 %) stellen
        tblPr = tbl.find(w("tblPr"))
        if tblPr is not None:
            tl = tblPr.find(w("tblLayout"))
            if tl is not None:
                tl.set(w("type"), "fixed")
            tw = tblPr.find(w("tblW"))
            if tw is not None:
                tw.set(w("type"), "pct"); tw.set(w("w"), str(TABLE_W_PCT))

        # 3. cantSplit auf jede Zeile setzen
        for tr in rows:
            trPr = tr.find(w("trPr"))
            if trPr is None:
                trPr = etree.Element(w("trPr")); tr.insert(0, trPr)
            if trPr.find(w("cantSplit")) is None:
                trPr.insert(0, etree.Element(w("cantSplit")))

        # 4. Schriftgroesse auf 9 pt (18 Halbpunkte)
        for r in tbl.iter(w("r")):
            rPr = r.find(w("rPr"))
            if rPr is None:
                rPr = etree.Element(w("rPr")); r.insert(0, rPr)
            for tag in ("sz", "szCs"):
                e = rPr.find(w(tag))
                if e is None:
                    e = etree.SubElement(rPr, w(tag))
                e.set(w("val"), FONT_HALFPT)

    tmp = path + ".tmp"
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for n in names:
            if n == "word/document.xml": continue
            zout.writestr(n, zin.read(n))
        zout.writestr("word/document.xml", etree.tostring(doc, xml_declaration=True, encoding="UTF-8", standalone=True))
    zin.close()
    shutil.move(tmp, path)

    print(f"[Tabellen-Postprocessing] {os.path.basename(path)}: {n_tbl} Tabellen formatiert (cantSplit, Breiten, 9pt).")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Verwendung: python table_layout_postprocess.py <pfad-zur-docx>")
        sys.exit(1)
    for p in sys.argv[1:]:
        process(p)
