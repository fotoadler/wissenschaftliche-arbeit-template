# Wissenschaftliche Arbeit: Modernes Markdown- & Git-Template

Ein praxiserprobtes Template für Bachelorarbeiten, Projektarbeiten und Masterarbeiten. Entwickelt für die nahtlose Zusammenarbeit mit KI-Assistenten (Coder, Claude Code, Cursor) und eine robuste Build-Pipeline nach Word (.docx).

---

## 1. Die Architektur-Philosophie

Klassisches Arbeiten in Word führt bei umfangreichen wissenschaftlichen Arbeiten häufig zu Frustration: zerschossene Formatierungen, unberechenbare Seitenumbrüche, fehlerhafte Verzeichnisse und das ständige Risiko von Datenverlust.

Dieses Template trennt **Inhalt** und **Layout** konsequent:

```text
+-----------------------+      +-----------------------+      +-----------------------+
|   Schreiben in        | ---> |     Build-Pipeline    | ---> |     Word-Export       |
|   modularen           |      |   (Pandoc + Python    |      |  (Perfekt formatiert  |
|   Markdown-Dateien    |      |    OpenXML Postproc)  |      |   nach Richtlinie)    |
+-----------------------+      +-----------------------+      +-----------------------+
            |
            v
+-----------------------+
|  Git-Versionskontrolle|
|  (Lückenlose Historie |
|  & Auto-Nacht-Backup) |
+-----------------------+
```

### Warum dieses Setup?
1. **Markdown-First:** Du konzentrierst dich vollkommen auf Text, Argumentation und Quellen. Jedes Kapitel ist eine eigenständige, übersichtliche Datei.
2. **Versionskontrolle via Git:** Jede Änderung wird versioniert. Du hast eine lückenlose Historie und kannst jederzeit auf ältere Stände zurückspringen.
3. **Automatisches Nacht-Backup:** Alle Änderungen werden nachts automatisch geloggt, committet und zu GitHub gepusht – ohne dass du Git-Befehle auswendig lernen musst.
4. **Hochschulkonformer DOCX-Export:** Das Build-Skript erzeugt per Knopfdruck ein Word-Dokument mit:
   - 4-stufiger Paginierung: Titelblatt ohne Zählung, Verzeichnisse römisch (I, II, III...), Hauptteil arabisch ab Seite 1 (1, 2, 3...), Erklärungen ohne Zählung.
   - Automatischer Feldaktualisierung (TOC, Abbildungs- und Tabellenverzeichnis beim Öffnen).
   - Umbruchschutz für Tabellen (`cantSplit`) und optimierten Spaltenbreiten.
   - Mathematischen Formeln als native Word-Gleichungen (MathML/OMML).

---

## 2. Schnelleinstieg in 3 Schritten

### Schritt 1: Repository klonen oder als Template nutzen
```bash
git clone <dein-repo-url>
cd <dein-projektname>
```

### Schritt 2: Onboarding mit deinem KI-Copilot starten
Öffne das Projekt in deiner bevorzugten KI-Umgebung (z. B. **Coder**, **Claude Code** oder **Cursor**).
Übergib der KI den Onboarding-Prompt (siehe unten) oder sage:
> *"Lies FRAGENKATALOG.md und gehe die Fragen Schritt für Schritt mit mir durch, um das Projekt einzurichten."*

Die KI fragt dich nach deinen Basisdaten, deiner Forschungsfrage und deinen Rahmenbedingungen und passt anschließend `00_steuerung/projektbriefing.md`, das Titelblatt und die Kapitelstruktur für dich an.

### Schritt 3: Erstes Dokument kompilieren
```bash
./build.sh
```
Das fertige Word-Dokument findest du unter:  
`02_export/Wissenschaftliche_Arbeit.docx`

---

## 3. Verzeichnisstruktur

```text
.
|-- FRAGENKATALOG.md             # Schritt-für-Schritt Onboarding für die KI
|-- AGENTS.md                    # System-Anweisung für KI-Assistenten (DHBW-Regeln)
|-- README.md                    # Diese Anleitung & Architekturübersicht
|-- build.sh / build.bat         # 1-Klick-Build (Markdown -> Word .docx)
|-- scripts/
|   |-- reference.docx           # Word-Formatvorlage (DHBW Arial 11pt / 1,5-zeilig)
|   |-- pagenum_postprocess.py   # 4-stufige Paginierung (Römisch / Arabisch)
|   |-- table_layout_postprocess.py # Tabellen-Umbruchschutz (cantSplit) & 9pt
|   |-- auto_sync.sh             # Automatisches Git-Backup & Push zu GitHub
|   |-- setup_nightly_cron.sh    # Richtet nächtlichen Cronjob (23:00 Uhr) ein
|   `-- ci/build-docx.yml        # GitHub Action: Baut das DOCX in der Cloud
|-- 00_steuerung/
|   |-- projektbriefing.md       # Basisdaten, Forschungsfragen & Rahmenbedingungen
|   |-- arbeitsregeln.md         # Verbindliche Arbeits- und Zitationsregeln
|   |-- offene_punkte.md         # Aufgaben-Backlog mit IDs und Prioritäten
|   |-- aenderungslog.md         # Audit-Log aller vorgenommenen Änderungen
|   `-- ki_prompts.md            # 11 spezialisierte Prompts für das Schreiben
|-- 01_kapitel/                  # Modulare Textkapitel
|   |-- 00_titelblatt.md         # DHBW-Titelblatt im OpenXML-Format (anonymisiert)
|   |-- 00a_sperrvermerk.md      # Offizieller DHBW-Sperrvermerk
|   |-- 00b_verzeichnisse.md     # Inhalts-, Abkürzungs-, Abb.- & Tabellenverzeichnis
|   |-- 01_einleitung.md         # Problemstellung & Forschungsfragen
|   |-- 02_hauptteil_platzhalter.md # Platzhalter & Anleitung für eigene Fachkapitel
|   |-- 07_literaturverzeichnis.md # Alphabetisches Literaturverzeichnis
|   |-- 08_anhang.md             # Anhang-Übersicht & Verweise auf Rohdaten
|   |-- 09_ki_erklaerung.md      # DHBW-Erklärung & 6-spaltiges KI-Verzeichnis
|   `-- 10_eigenstaendigkeitserklaerung.md # Offizielle DHBW-Selbstständigkeitserklärung
|-- 02_export/                   # Generierte Word- und PDF-Exporte (in .gitignore)
|   `-- anhang/                  # Rohdaten, Fragebögen, digitale Exporte
|-- 03_quellen/                  # Literatur- und Quellenverwaltung
|   |-- pdf/                     # PDF-Volltexte der Primärliteratur
|   |-- markdown/                # Markdown-Exzerpte und Quellenzusammenfassungen
|   |-- literatur.bib            # BibTeX-Datenbank
|   `-- quellen_inventar.md      # Übersicht über alle erfassten Quellen
|-- 04_richtlinien/              # Offizielle Hochschul-Richtlinien
|   |-- Richtlinien_wiss_Arbeiten_Wirtschaft_2.0.pdf # Verbindliche Original-Richtlinie
|   |-- Richtlinien_wiss_Arbeiten_Wirtschaft_2.0.md  # Volltext zur Prüfung durch KI
|   `-- richtlinien_hinweise.md  # Wichtige Formalia auf einen Blick
`-- 05_assets/
    `-- logos/                   # DHBW-Logo und Partner-Logo-Platzhalter
```

---

## 4. Git-Automatisierung: Sorgenfreies Backup

Du musst keine komplexen Git-Befehle lernen.

### Manuelles Backup mit einem Befehl:
```bash
./scripts/auto_sync.sh
```
Das Skript prüft, welche Dateien du verändert hast, formatiert eine sprechende Commit-Nachricht mit Zeitstempel, dokumentiert die Änderung im `aenderungslog.md` und pusht alles zu GitHub.

### Nächtliche Vollautomatisierung aktivieren (macOS / Linux):
```bash
./scripts/setup_nightly_cron.sh
```
Damit wird auf deinem Rechner ein täglicher Job registriert, der jeden Abend um 23:00 Uhr automatisch den aktuellen Stand sichert.

---

## 5. Voraussetzungen für den lokalen Build

- **Pandoc:** (z. B. via `brew install pandoc` auf macOS oder Download von [pandoc.org](https://pandoc.org))
- **Python 3:** mit dem Paket `lxml` (`pip install lxml`)

*Hinweis:* Falls du Pandoc oder Python nicht lokal installieren möchtest, baut die enthaltene **GitHub Action** (`.github/workflows/build-docx.yml`) bei jedem Push zu GitHub das Word-Dokument automatisch in der Cloud. Du kannst es dort jederzeit als fertige Datei herunterladen.
