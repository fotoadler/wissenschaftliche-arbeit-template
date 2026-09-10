# Die 11 Kern-Prompts für wissenschaftliches Arbeiten

Diese Prompts sind exakt auf die Markdown- und Pandoc-Architektur dieser Arbeitsumgebung abgestimmt.

---

### Prompt 1: Kapitel kritisch auf Substanz & Methodik prüfen
```text
Lies die Datei [01_kapitel/XX_kapitelname.md] vollständig.
Führe ein kritisches wissenschaftliches Gutachten durch:
1. Wo sind Argumentationslücken oder unbelegte Thesen?
2. Wo ist die Begrifflichkeit unpräzise?
3. Welche Gegenargumente werden übersehen?
4. Welche Passagen tragen nicht direkt zur Beantwortung der Forschungsfrage bei?
Gib mir konkrete, priorisierte Verbesserungsvorschläge mit Zeilenbezug.
```

---

### Prompt 2: Akademischer Feinschliff & Entschlackung
```text
Überarbeite den folgenden Textabschnitt aus [01_kapitel/XX_kapitelname.md]:
[Text einfügen]

Kriterien:
1. Entferne Füllwörter und Passiv-Verschachtelungen.
2. Schärfe die wissenschaftliche Präzision ohne reißerische Adjektive.
3. Behalte alle Zitate [^N] und Fachbegriffe strikt unverändert bei.
4. Zeige mir nach dem Text stichpunktartig, was du geändert hast und warum.
```

---

### Prompt 3: Quellenbedarf markieren
```text
Analysiere die Datei [01_kapitel/XX_kapitelname.md].
Finde alle Aussagen, Definitionen, Zahlenangaben oder Behauptungen, die einer wissenschaftlichen Quelle bedürfen, aber noch unbelegt sind.
Füge an den entsprechenden Stellen exakt das Tag [Quelle nötig: Welcher Beleg wird gebraucht?] ein.
```

---

### Prompt 4: Argumentationsprüfung (Advocatus Diaboli)
```text
Nimm die Rolle eines extrem kritischen Erstgutachters ein.
Prüfe meine Argumentationskette im Abschnitt [Abschnittsname / Text]:
1. Wo begehe ich Zirkelschlüsse oder falsche Kausalitätsannahmen?
2. Wie könnte ein Prüfungsgremium diese These angreifen?
3. Welche konkrete empirische Evidenz fehlt, um die Kritik abzuwehren?
```

---

### Prompt 5: Prüfung des roten Fadens
```text
Lies [00_steuerung/projektbriefing.md] und vergleiche die dort formulierte Forschungsfrage mit den Kapiteln [01_einleitung.md] und [07_fazit.md].
1. Beantwortet das Fazit exakt die in der Einleitung aufgeworfenen Fragen?
2. Gibt es im Hauptteil Kapitel, die vom roten Faden abweichen?
3. Wo fehlen verbindende Übergangssätze zwischen den Kapiteln?
```

---

### Prompt 6: Redundanzen und Dopplungen aufspüren
```text
Vergleiche [01_kapitel/02_theoretische_grundlagen.md] und [01_kapitel/04_konzeption_umsetzung.md].
Welche Definitionen, Sachverhalte oder Literaturstellen werden mehrfach erläutert?
Schlage vor, wo gekürzt werden kann und wo ein präziser Querverweis ("siehe Kapitel 2.X") ausreicht.
```

---

### Prompt 7: Executive Summary erstellen
```text
Erstelle eine einseitige Executive Summary / Zusammenfassung der Arbeit auf Basis von Kapitel 1, 5 und 7:
1. Problemstellung & Praxisrelevanz (2 Sätze)
2. Methodischer Ansatz (2 Sätze)
3. Zentrale empirische Befunde (4–5 Bulletpoints mit Zahlen)
4. Fazit & Handlungsempfehlung (2 Sätze)
```

---

### Prompt 8: Finale Konsistenzprüfung vor Abgabe
```text
Prüfe die gesamte Arbeit auf formale und inhaltliche Einheitlichkeit:
1. Werden Fachbegriffe durchgängig einheitlich geschrieben?
2. Stimmt das Abkürzungsverzeichnis mit den im Text verwendeten Kürzeln überein?
3. Sind alle Tabellen- und Abbildungsbeschriftungen vollständig?
4. Sind noch offene Platzhalter ([Quelle nötig], [Unsicher], [SEITE_FEHLT]) im Text?
```

---

### Prompt 9: Exportvorbereitung & Syntaxcheck (Pandoc)
```text
Prüfe alle Markdown-Dateien in 01_kapitel/ auf Konformität mit dem Pandoc-Word-Export:
1. Endet jede formale Seite und jedes Kapitel mit dem OpenXML-Seitenumbruch-Block?
2. Gibt es unzulässige HTML-Tags oder unescapte Zeichen?
3. Ist die Überschriften-Hierarchie (H1 nur einmal ganz oben, dann H2, dann H3) fehlerfrei?
```

---

### Prompt 10: Seitenzahlen auflösen aus Volltext-Markdowns
```text
Durchsuche die Volltextdateien in 03_quellen/ nach dem folgenden Zitat / Beleg:
"[Zitat oder Kernpassage]"

Ermittle die genaue Seitenzahl im Quellendokument und ersetze den Platzhalter [SEITE_FEHLT: Dateiname] in der Fußnote durch die reale Seitenzahl "S. XX".
```

---

### Prompt 11: Rohnotizen in strukturierten Fließtext überführen
```text
Hier sind meine unstrukturierten Notizen und Stichpunkte zu Unterkapitel [X.X]:
[Notizen einfügen]

Formuliere daraus einen ersten Entwurf für den Fließtext:
- Akademischer, neutraler Sprachstil im Präsens.
- Klare Gedankenführung vom Allgemeinen zum Spezifischen.
- Kennzeichne offene Belege mit [Quelle nötig].
```
