#!/usr/bin/env bash
# ==============================================================================
# Build-Pipeline: Markdown -> Word (.docx) mit wissenschaftlicher Formatierung
# ==============================================================================
set -e

# Projektpfad bestimmen
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

OUTPUT_DIR="02_export"
OUTPUT_FILE="$OUTPUT_DIR/Wissenschaftliche_Arbeit.docx"
REFERENCE_DOC="scripts/reference.docx"

mkdir -p "$OUTPUT_DIR"

echo "----------------------------------------------------------------"
echo "[BUILD] Starte Kompilierung: Markdown -> DOCX"
echo "----------------------------------------------------------------"

# 1. Pruefen ob Pandoc installiert ist
if ! command -v pandoc &> /dev/null; then
    echo "[FEHLER] Pandoc ist nicht installiert oder nicht im PATH."
    echo "Installiere Pandoc via: brew install pandoc (macOS) oder apt install pandoc (Linux)"
    exit 1
fi

# 2. Pruefen ob Python3 und lxml verfuegbar sind
if ! python3 -c "import lxml" &> /dev/null; then
    echo "[WARNUNG] Python-Paket 'lxml' nicht gefunden. Installiere temporaer..."
    pip3 install lxml || pip install lxml
fi

# 3. Pandoc-Aufruf
echo "[1/3] Fuehre Pandoc-Export aus..."
pandoc \
  01_kapitel/00_titelblatt.md \
  01_kapitel/00a_sperrvermerk.md \
  01_kapitel/00b_verzeichnisse.md \
  01_kapitel/01_einleitung.md \
  01_kapitel/02_hauptteil_platzhalter.md \
  01_kapitel/07_literaturverzeichnis.md \
  01_kapitel/08_anhang.md \
  01_kapitel/09_ki_erklaerung.md \
  01_kapitel/10_eigenstaendigkeitserklaerung.md \
  --from markdown \
  --to docx \
  --output "$OUTPUT_FILE" \
  --reference-doc="$REFERENCE_DOC" \
  --metadata lang="de-DE" \
  --mathml

echo "[2/3] Fuehre Paginierungs-Postprocessing aus (Roemisch / Arabisch)..."
python3 scripts/pagenum_postprocess.py "$OUTPUT_FILE"

echo "[3/3] Fuehre Tabellen-Postprocessing aus (cantSplit, Breiten, 9pt)..."
python3 scripts/table_layout_postprocess.py "$OUTPUT_FILE"

echo "----------------------------------------------------------------"
echo "[ERFOLG] Dokument erfolgreich generiert:"
echo "         $OUTPUT_FILE"
echo "----------------------------------------------------------------"

