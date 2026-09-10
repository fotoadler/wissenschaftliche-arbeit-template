"""Paginierungs-Postprocessing fuer den Word-Export (DOCX).

Stellt das 4-teilige Paginierungsschema gemaess wissenschaftlichen Hochschulrichtlinien her:
1. Titelblatt & Sperrvermerk: Keine Seitenzahlen.
2. Verzeichnisse (Inhalt, Abkuerzungen, Abb., Tab.): Roemische Zahlen (I, II, III...).
3. Haupttext (Einleitung bis Anhang): Arabische Ziffern ab Seite 1 (1, 2, 3...).
4. Erklaerungen (KI & Eigenstaendigkeit): Keine Seitenzahlen.

Zusatzfunktionen:
- Setzt outlineLvl=9 auf formale Seiten, damit sie nicht im Inhaltsverzeichnis erscheinen.
- Schreibt updateFields=true in word/settings.xml, damit Word beim Oeffnen alle
  Verzeichnisse und Nummerierungen automatisch aktualisiert.

Aufruf:
    python 05_assets/pagenum_postprocess.py "02_export/Dokument.docx"
"""
import sys, zipfile, copy, re, os, shutil
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
from lxml import etree

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PR = "http://schemas.openxmlformats.org/package/2006/relationships"
CT = "http://schemas.openxmlformats.org/package/2006/content-types"

def w(t): return f"{{{W}}}{t}"
def rid(t): return f"{{{R}}}{t}"

FOOTER_RELTYPE = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer"
FOOTER_CT = "application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"

FOOTER_NUM = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:p><w:pPr><w:jc w:val="right"/></w:pPr>''' + \
('<w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/><w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr>%s</w:r>' % '<w:fldChar w:fldCharType="begin"/>') + \
('<w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/><w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>') + \
('<w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/><w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr><w:fldChar w:fldCharType="separate"/></w:r>') + \
('<w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/><w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr><w:t>1</w:t></w:r>') + \
('<w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/><w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr><w:fldChar w:fldCharType="end"/></w:r>') + \
'</w:p></w:ftr>'

FOOTER_EMPTY = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:p/></w:ftr>'

# Konfigurierbare Suchbegriffe fuer Abschnittsuebergaenge
# Format: (Ueberschrifts-Praefix, Footer-Typ, Zahlenformat der ENDENDEN Sektion)
SECTION_PLAN = [
    ("Inhaltsverzeichnis", "EMPTY", None),          # Ende Sektion 1 (Titelblatt/Sperrvermerk)
    ("1 Einleitung",       "NUM",   "upperRoman"),   # Ende Sektion 2 (Verzeichnisse)
    ("Erklärung",          "NUM",   "decimal"),      # Ende Sektion 3 (Hauptteil Einleitung bis Anhang)
]

# Ueberschriften, die nicht im Inhaltsverzeichnis auftauchen duerfen
TOC_EXCLUDE = [
    "Sperrvermerk", 
    "Inhaltsverzeichnis",
    "Erklärung", 
    "Erklärung und Nutzungsdokumentation", 
    "Eigenständigkeitserklärung"
]

def ptext(p):
    return "".join(t.text or "" for t in p.iter(w("t"))).strip()

def is_heading(p):
    pPr = p.find(w("pPr"))
    if pPr is None: return False
    st = pPr.find(w("pStyle"))
    return st is not None and ("Heading" in (st.get(w("val")) or "") or "berschrift" in (st.get(w("val")) or ""))

def is_pagebreak_only(el):
    if el.tag != w("p"): return False
    if ptext(el): return False
    brs = [b for b in el.iter(w("br")) if (b.get(w("type")) == "page")]
    return len(brs) >= 1

def exclude_from_toc(body):
    n = 0
    for p in body.iter(w("p")):
        if not is_heading(p): continue
        t = ptext(p)
        if not any(t == x or t.startswith(x) for x in TOC_EXCLUDE): continue
        pPr = p.find(w("pPr"))
        if pPr is None: continue
        ol = pPr.find(w("outlineLvl"))
        if ol is not None:
            ol.set(w("val"), "9")
        else:
            ol = etree.Element(w("outlineLvl")); ol.set(w("val"), "9")
            anchor = pPr.find(w("rPr"))
            if anchor is None: anchor = pPr.find(w("sectPr"))
            if anchor is not None: anchor.addprevious(ol)
            else: pPr.append(ol)
        n += 1
    return n

def build_sectpr(template_sectpr, footer_rid, num_fmt):
    sect = etree.SubElement(etree.Element(w("pPr")), w("sectPr"))
    fr = etree.SubElement(sect, w("footerReference")); fr.set(w("type"), "default"); fr.set(rid("id"), footer_rid)
    typ = etree.SubElement(sect, w("type")); typ.set(w("val"), "nextPage")
    for tag in ("pgSz", "pgMar"):
        el = template_sectpr.find(w(tag))
        if el is not None: sect.append(copy.deepcopy(el))
    if num_fmt:
        pnt = etree.SubElement(sect, w("pgNumType")); pnt.set(w("fmt"), num_fmt); pnt.set(w("start"), "1")
    for tag in ("cols", "docGrid"):
        el = template_sectpr.find(w(tag))
        if el is not None: sect.append(copy.deepcopy(el))
    return sect

def make_break_para(sectpr):
    p = etree.Element(w("p")); pPr = etree.SubElement(p, w("pPr")); pPr.append(sectpr); return p

def process(path):
    zin = zipfile.ZipFile(path, "r")
    names = zin.namelist()
    doc = etree.fromstring(zin.read("word/document.xml"))
    rels = etree.fromstring(zin.read("word/_rels/document.xml.rels"))
    ctypes = etree.fromstring(zin.read("[Content_Types].xml"))
    settings = etree.fromstring(zin.read("word/settings.xml"))
    body = doc.find(w("body"))
    children = list(body)
    final_sectpr = children[-1] if children[-1].tag == w("sectPr") else None
    assert final_sectpr is not None, "Fehler: Kein finales sectPr im Dokument gefunden."

    used = [int(m.group(1)) for rel in rels for m in [re.match(r"rId(\d+)", rel.get("Id") or "")] if m]
    base = max(used) + 1 if used else 1
    RID_NUM, RID_EMPTY = f"rId{base}", f"rId{base+1}"

    for r_id, target in ((RID_NUM, "footerNum.xml"), (RID_EMPTY, "footerEmpty.xml")):
        e = etree.SubElement(rels, f"{{{PR}}}Relationship")
        e.set("Id", r_id); e.set("Type", FOOTER_RELTYPE); e.set("Target", target)
    for part in ("/word/footerNum.xml", "/word/footerEmpty.xml"):
        o = etree.SubElement(ctypes, f"{{{CT}}}Override")
        o.set("PartName", part); o.set("ContentType", FOOTER_CT)

    report = []
    for needle, ftype, fmt in SECTION_PLAN:
        frid = RID_NUM if ftype == "NUM" else RID_EMPTY
        idx = None
        for i, el in enumerate(body):
            if el.tag == w("p") and is_heading(el):
                t = ptext(el)
                if t == needle or t.startswith(needle):
                    idx = i; break
        if idx is None:
            report.append(f"   [WARNUNG] Ueberschrift nicht gefunden: '{needle}'"); continue
        sect = build_sectpr(final_sectpr, frid, fmt)
        prev = body[idx-1] if idx > 0 else None
        if prev is not None and is_pagebreak_only(prev):
            body.replace(prev, make_break_para(sect))
            report.append(f"   [OK] '{needle}': Seitenumbruch -> Abschnittsumbruch (Format={fmt})")
        else:
            body.insert(idx, make_break_para(sect))
            report.append(f"   [OK] '{needle}': Abschnittsumbruch eingefuegt (Format={fmt})")

    # Finale Sektion (Erklaerungen): Leere Fusszeile
    fr = etree.Element(w("footerReference")); fr.set(w("type"), "default"); fr.set(rid("id"), RID_EMPTY)
    final_sectpr.insert(0, fr)

    # Ueberschriften aus TOC ausschliessen
    n_excl = exclude_from_toc(body)
    report.append(f"   [OK] {n_excl} Ueberschriften aus Inhaltsverzeichnis ausgeschlossen (outlineLvl=9)")

    # Automatische Feldaktualisierung (TOC, Abbildungen, Tabellen)
    update_fields = settings.find(w("updateFields"))
    if update_fields is None:
        update_fields = etree.SubElement(settings, w("updateFields"))
    update_fields.set(w("val"), "true")
    report.append("   [OK] Automatische Feldaktualisierung in Word aktiviert")

    tmp = path + ".tmp"
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for n in names:
            if n in ("word/document.xml", "word/settings.xml", "word/_rels/document.xml.rels", "[Content_Types].xml"): continue
            zout.writestr(n, zin.read(n))
        zout.writestr("word/document.xml", etree.tostring(doc, xml_declaration=True, encoding="UTF-8", standalone=True))
        zout.writestr("word/settings.xml", etree.tostring(settings, xml_declaration=True, encoding="UTF-8", standalone=True))
        zout.writestr("word/_rels/document.xml.rels", etree.tostring(rels, xml_declaration=True, encoding="UTF-8", standalone=True))
        zout.writestr("[Content_Types].xml", etree.tostring(ctypes, xml_declaration=True, encoding="UTF-8", standalone=True))
        zout.writestr("word/footerNum.xml", FOOTER_NUM)
        zout.writestr("word/footerEmpty.xml", FOOTER_EMPTY)
    zin.close()
    shutil.move(tmp, path)

    print(f"\n[Postprocessing] {os.path.basename(path)}")
    for r in report: print(r)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Verwendung: python pagenum_postprocess.py <pfad-zur-docx>")
        sys.exit(1)
    for p in sys.argv[1:]:
        process(p)
