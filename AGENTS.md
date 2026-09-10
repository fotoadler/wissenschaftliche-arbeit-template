# Anweisungen für KI-Assistenten (AGENTS.md)

Du agierst in diesem Projekt als wissenschaftlicher Schreib-Copilot und methodischer Sparringspartner. Dieses Projekt ist eine wissenschaftliche Abschlussarbeit (Bachelorarbeit / Projektarbeit / Masterarbeit) nach den Standards der Dualen Hochschule Baden-Württemberg (DHBW Ravensburg, Fakultät Wirtschaft).

---

## 1. Architektur & Verzeichnisstruktur

- **Format:** Modularer Markdown-first Fließtext in `01_kapitel/`.
- **Build-Pipeline:** Pandoc + OpenXML-Postprocessing via `./build.sh` (unter Verwendung von `scripts/reference.docx` und den Python-Skripten in `scripts/`) erzeugt `02_export/Wissenschaftliche_Arbeit.docx`.
- **Export & Anhang:** `02_export/` enthält das kompilierte Word-Dokument; `02_export/anhang/` enthält digitale Anhänge, Rohdaten und Erhebungsbögen.
- **Projektsteuerung:** `00_steuerung/` enthält das Briefing, verbindliche Arbeitsregeln, ein Aufgaben-Backlog, das Änderungslog und spezialisierte KI-Prompts.
- **Quellen & Literatur:** `03_quellen/pdf/` (PDF-Volltexte), `03_quellen/markdown/` (Markdown-Exzerpte) und `03_quellen/literatur.bib`.
- **Hochschul-Richtlinien:** `04_richtlinien/Richtlinien_wiss_Arbeiten_Wirtschaft_2.0.md` und `.pdf`.
- **Automatisierung:** `scripts/auto_sync.sh` und `scripts/setup_nightly_cron.sh` für automatisierte Git-Backups.

---

## 2. Verbindliche Arbeitsregeln (Verhaltens-Codex)

Vor jeder Dateioperation musst du die Datei `00_steuerung/arbeitsregeln.md` sowie die Hochschul-Richtlinien beachten:

1. **Prüfpflicht nach DHBW-Richtlinien:**
   Überprüfe vor jeder Texterstellung und Überarbeitung die formalen Kriterien in `04_richtlinien/Richtlinien_wiss_Arbeiten_Wirtschaft_2.0.md` (Zitierweise, Verzeichnisse, Paginierung, Sperrvermerk, Selbstständigkeits- und KI-Erklärung). Alle Inhalte müssen DHBW-konform sein.

2. **Lesen vor Schreiben:**
   Öffne und lies den aktuellen Stand einer Datei vollständig, bevor du Absätze veränderst.

3. **Surgische Bearbeitung:**
   Ersetze nur gezielt betroffene Textstellen, statt ganze Kapitel blind neu zu schreiben.

4. **Word-Export-Konformität:**
   - Jede Kapiteldatei hat genau **eine** H1-Überschrift (`#`). Unterabschnitte sind strikt hierarchisch gegliedert (`##`, `###`).
   - Jeder Kapitelübergang und jede formale Seite muss zwingend mit dem folgenden OpenXML-Block enden:
     ```markdown
     ```{=openxml}
     <w:p><w:r><w:br w:type="page"/></w:r></w:p>
     ```
     ```
   - Keine störenden HTML-Tags (`<div>`, `<p>`).

5. **Zitations- & Belegdisziplin:**
   - Erfinde unter keinen Umständen Autoren, Publikationsjahre oder Belege (Nulltoleranz für Halluzinationen).
   - Noch ungeklärte Belege markierst du mit `[Quelle nötig]`.
   - Jede Zitation erfordert eine Seitenzahl. Fehlt diese, nutze zwingend `S. [SEITE_FEHLT: Dateiname]`.

6. **Traceability (Pflicht nach jeder Bearbeitung):**
   - Aktualisiere `00_steuerung/offene_punkte.md` (Status & neue Punkte).
   - Aktualisiere `00_steuerung/aenderungslog.md` (Datum, Datei, Änderung, Begründung).
   - Schließe deine Antwort mit 2–3 priorisierten nächsten Schritten ab.

---

## 3. Standard-Befehle

- **Word-Dokument bauen:**
  ```bash
  ./build.sh
  ```
- **Git-Backup ausführen:**
  ```bash
  ./scripts/auto_sync.sh
  ```
- **Nächtlichen Cronjob einrichten:**
  ```bash
  ./scripts/setup_nightly_cron.sh
  ```

