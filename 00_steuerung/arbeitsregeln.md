# Arbeitsregeln für die wissenschaftliche Bearbeitung (Governance v2.0)

Diese Regeln gelten verbindlich für alle KI-Assistenten und den Verfasser. Sie sichern wissenschaftliche Exzellenz, fehlerfreie Word-Exporte (Pandoc) und lückenlose Nachvollziehbarkeit.

---

## 1. Modularität & Dateioperationen

- **Lesen vor Schreiben:** Vor jeder Bearbeitung muss der aktuelle Stand der Datei vollständig geladen sein, um Kontextverluste oder doppelte Absätze zu vermeiden.
- **Surgische Bearbeitung:** Bevorzuge gezielte Ersetzungen und Patches gegenüber dem vollständigen Überschreiben ganzer Kapitel.
- **Klare Ordnerdisziplin:**
  - Kapitel gehören nach `01_kapitel/`
  - Exporte und digitale Anhänge nach `02_export/` und `02_export/anhang/`
  - Literatur-Volltexte nach `03_quellen/pdf/`, Exzerpte nach `03_quellen/markdown/` und BibTeX nach `03_quellen/literatur.bib`
  - Richtlinien nach `04_richtlinien/` (verbindliche Prüfung gegen `Richtlinien_wiss_Arbeiten_Wirtschaft_2.0.md`)
  - Skripte und Formatvorlagen nach `scripts/`
  - Logos und Abbildungen nach `05_assets/logos/`

---

## 2. Pandoc & Word-Export-Konformität (DOCX)

- **Echte Word-Seitenumbrüche (Page Breaks):** Kapitelübergänge und Seitenumbrüche nach formalen Seiten müssen exakt mit folgendem OpenXML-Block eingefügt werden:
  ```markdown
  ```{=openxml}
  <w:p><w:r><w:br w:type="page"/></w:r></w:p>
  ```
  ```
- **Strikte Überschriftenhierarchie:** Jede Kapiteldatei enthält genau **eine** H1-Überschrift (`# 1 Einleitung`) ganz oben. Alle Unterabschnitte folgen strikt mit H2 (`## 1.1`) und H3 (`### 1.1.1`). Niemals Hierarchie-Ebenen überspringen.
- **Keine störenden HTML-Hacks:** Keine `<div style="page-break-after:always">` oder ungeparsten HTML-Tags im Fließtext verwenden.
- **Diagramme als Bild einbinden:** Mermaid-Blöcke (` ```mermaid `) werden von Word nicht dargestellt. Diagramme müssen als PNG exportiert und im Markdown via `![](05_assets/diagramm.png)` eingebunden werden.
- **Formeln mit MathML:** Mathematische Formeln (`$...$` und `$$...$$`) werden durch den Pandoc-Schalter `--mathml` als native Word-Formeln (OMML) eingebettet.

---

## 3. Qualitätssicherung & Zitations-Guardrails

- **Nulltoleranz für Quellen-Halluzinationen:** Die KI darf unter keinen Umständen Autoren, Publikationsjahre, Zitate oder empirische Zahlen erfinden.
- **Markierungspflicht für Lücken:**
  - Aussagen, die eines Belegs bedürfen, aber noch nicht verifiziert sind, werden zwingend mit `[Quelle nötig]` gekennzeichnet.
  - Unsichere Aussagen werden mit `[Unsicher: Grund]` markiert.
- **Genaue Seitenzahlen Pflicht:**
  - Jede Zitation verlangt eine konkrete Seitenzahl (`S. [Seitenzahl]`).
  - Ist die Seitenzahl im Entwurf noch unklar, muss zwingend der Platzhalter `S. [SEITE_FEHLT: Dateiname]` verwendet werden.
- **Wissenschaftlicher Sprachstil:** Nüchtern, präzise, analytisch. Keine reißerischen Werbe-Adjektive ("bahnbrechend", "revolutionär") und kein generischer KI-Slang ("delve", "testament", "tapestry").

---

## 4. Transparenz, Dokumentation & KI-Verzeichnis (Traceability)

Nach jeder substanziellen Bearbeitungssitzung muss die KI automatisch:

1. **[01_kapitel/09_ki_erklaerung.md](file:///Users/chris/Documents/KI%20Seminar/wissenschaftliche-arbeit-template/01_kapitel/09_ki_erklaerung.md) aktualisieren:** Den Arbeitsschritt automatisch mit einem normalisierten/generalisierten Prompt, der Kategorie (A–E), dem Werkzeug (z. B. Codex, Claude Code, Antigravity, ChatGPT, Claude, NotebookLM), dem betroffenen Kapitel und der Art der menschlichen Kontrolle in die Tabelle eintragen.
2. **[offene_punkte.md](file:///Users/chris/Documents/KI%20Seminar/wissenschaftliche-arbeit-template/00_steuerung/offene_punkte.md) aktualisieren:** Status bestehender Aufgaben anpassen, neue Aufgaben ergänzen.
3. **[aenderungslog.md](file:///Users/chris/Documents/KI%20Seminar/wissenschaftliche-arbeit-template/00_steuerung/aenderungslog.md) aktualisieren:** Datum, Datei, konkrete Änderung und Begründung eintragen.
4. **Nächste Schritte benennen:** Dem Benutzer am Ende jeder Antwort 2–3 konkrete, priorisierte nächste Schritte vorschlagen.
