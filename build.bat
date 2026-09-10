@echo off
REM ==============================================================================
REM Build-Pipeline: Markdown -> Word (.docx) fuer Windows
REM ==============================================================================

set OUTPUT_DIR=02_export
set OUTPUT_FILE=%OUTPUT_DIR%\Wissenschaftliche_Arbeit.docx
set REFERENCE_DOC=scripts\reference.docx

if not exist "%OUTPUT_DIR%" mkdir "%OUTPUT_DIR%"

echo ----------------------------------------------------------------
echo [BUILD] Starte Kompilierung: Markdown -^> DOCX
echo ----------------------------------------------------------------

echo [1/3] Fuehre Pandoc-Export aus...
pandoc ^
  01_kapitel\00_titelblatt.md ^
  01_kapitel\00a_sperrvermerk.md ^
  01_kapitel\00b_verzeichnisse.md ^
  01_kapitel\01_einleitung.md ^
  01_kapitel\02_hauptteil_platzhalter.md ^
  01_kapitel\07_literaturverzeichnis.md ^
  01_kapitel\08_anhang.md ^
  01_kapitel\09_ki_erklaerung.md ^
  01_kapitel\10_eigenstaendigkeitserklaerung.md ^
  --from markdown ^
  --to docx ^
  --output "%OUTPUT_FILE%" ^
  --reference-doc="%REFERENCE_DOC%" ^
  --metadata lang="de-DE" ^
  --mathml

if %ERRORLEVEL% NEQ 0 (
    echo [FEHLER] Pandoc ist fehlgeschlagen. Bitte Installation pruefen.
    exit /b %ERRORLEVEL%
)

echo [2/3] Fuehre Paginierungs-Postprocessing aus...
python scripts\pagenum_postprocess.py "%OUTPUT_FILE%"

echo [3/3] Fuehre Tabellen-Postprocessing aus...
python scripts\table_layout_postprocess.py "%OUTPUT_FILE%"

echo ----------------------------------------------------------------
echo [ERFOLG] Dokument erstellt: %OUTPUT_FILE%
echo ----------------------------------------------------------------
