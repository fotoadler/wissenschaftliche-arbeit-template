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

7. **Automatisches Führen des KI-Verzeichnisses (DHBW-Pflicht):**
   - Nach jeder inhaltlichen, analytischen, methodischen oder codierenden Sitzung trägst du den Arbeitsschritt **automatisch** in `01_kapitel/09_ki_erklaerung.md` in die standardisierte Tabelle ein.
   - Formuliere den Prompt dabei stets **normalisiert und generalisiert** (den methodischen Kern ohne flüchtige Zwischenbefehle).
   - Halte fest: Kategorie (A: Themenfindung, B: Recherche & Quellen, C: Datenanalyse & Coding, D: Sprachliches Lektorat, E: Visualisierung), Werkzeug (z. B. Codex, Claude Code, Antigravity, ChatGPT, Claude, NotebookLM), generalisierter Prompt, betroffener Bereich/Datei und Art der menschlichen Kontrolle.
   - So ist das KI-Verzeichnis von Tag 1 an lückenlos, DHBW-konform und ohne manuellen Aufwand vollständig gepflegt.

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

## 4. Verbindliche Git-Sicherung nach Logikbausteinen

Dieses Repository ist die persönliche Arbeitskopie des Studierenden. Das öffentliche Template ist nur die Ausgangsbasis und darf niemals als `origin` für eigene Arbeit verwendet werden.

Nach jedem fertig bearbeiteten, in sich verständlichen Logikbaustein (z. B. ein Abschnitt, ein Quellenpaket, eine methodische Entscheidung oder ein abgeschlossener Build-/Formatierungsblock) sicherst du den Stand automatisch:

1. Prüfe `git status`, den Diff und ob `origin` auf das persönliche Repository des Studierenden zeigt.
2. Führe die für den Arbeitsblock passenden Prüfungen bzw. den Build aus.
3. Füge nur die zu diesem Arbeitsblock gehörenden Dateien hinzu.
4. Erzeuge einen kurzen, verständlichen Commit, z. B. `Kapitel 1: Forschungsfragen geschärft`.
5. Pushe den Commit zu `origin` und prüfe anschließend, dass der Push erfolgreich war und der Arbeitsstand sauber ist.

Nicht nach jedem einzelnen Satz committen, sondern nach abgeschlossenen, nachvollziehbaren Arbeitsblöcken. Vor einem Push niemals Zugangsdaten, Tokens oder andere Geheimnisse einchecken. Wenn GitHub nicht verbunden ist, der Push fehlschlägt oder `origin` nicht zum persönlichen Repository gehört, halte an, erkläre den konkreten Grund und tue nicht so, als wäre der Stand online gesichert. Das Nacht-Backup ist eine zusätzliche Sicherheitskopie und ersetzt diese Zwischen-Sicherungen nicht.
