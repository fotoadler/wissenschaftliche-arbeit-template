# Erklärung und Nutzungsdokumentation zum Einsatz von KI-basierten Werkzeugen {.unnumbered .unlisted}

---

## Erklärung

Zur Verwendung KI-gestützter Werkzeuge erkläre ich in Kenntnis des Hinweisblatts *„Hinweise zum Einsatz von KI-basierten Werkzeugen bei der Anfertigung wissenschaftlicher Arbeiten, u. a. im prüfungsrechtlichen Kontext“* Folgendes:

- Ich habe mich aktiv über die Leistungsfähigkeit und Beschränkungen der in meiner Arbeit eingesetzten KI-Werkzeuge informiert.
- Bei der Anfertigung der Arbeit habe ich durchgehend eigenständig und beim Einsatz KI-gestützter Werkzeuge maßgeblich steuernd gearbeitet.
- Insbesondere habe ich die Inhalte entweder aus wissenschaftlichen oder anderen zugelassenen Quellen entnommen und diese gekennzeichnet oder diese unter Anwendung wissenschaftlicher Methoden selbst entwickelt.
- Mir ist bewusst, dass ich als Verfasser/in der Arbeit die volle Verantwortung für die in ihr gemachten Angaben, Daten und Aussagen trage.
- Soweit ich KI-gestützte Werkzeuge zur Erstellung der Arbeit eingesetzt habe, sind diese jeweils mit dem Produktnamen, den formulierten Eingaben (Prompts), der Einsatzform sowie der entsprechenden Bereichsreferenzierung auf die Arbeit im nachfolgenden KI-Verzeichnis vollständig ausgewiesen und im Text belegt.

[Ort], den [Datum]

__________________________________

[Vorname Nachname des Verfassers]

---

## KI-Verzeichnis

Das Verzeichnis dokumentiert den Einsatz KI-gestützter Werkzeuge nach Einsatzkategorien. Je Eintrag sind das verwendete Werkzeug, der konkrete Verwendungszweck, ein repräsentativer Prompt, der betroffene Bereich der Arbeit sowie die Form der menschlichen Qualitätskontrolle angegeben.

| Kategorie / Phase | Eingesetztes Werkzeug & Modell | Zweck & Art des Einsatzes | Repräsentativer Prompt / Eingabe | Betroffener Bereich | Grad der menschlichen Kontrolle / Modifikation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **A: Themenfindung & Scoping** | ChatGPT Plus (GPT-4o) | Brainstorming möglicher Forschungsfragen und Strukturierung der Problemstellung | *„Ich untersuche Thema X im Kontext von Y. Welche 3 Forschungsfragen grenzen das Untersuchungsfeld präzise ab?“* | Kap. 1.2 | Vorschläge kritisch gefiltert, mit betrieblicher Praxis abgeglichen und eigenständig geschärft. |
| **B: Recherche & Literatur** | Google NotebookLM | Identifikation von Schwerpunkten und Synthese vorliegender Fachpublikationen | *„Analysiere die hochgeladenen 15 PDFs: Wo stimmen die Autoren überein, wo existieren Widersprüche bezüglich Methodik Z?“* | Kap. 2 (Theorie) | Alle abgeleiteten Aussagen anhand der Original-PDFs auf Belegtreue und korrekte Seitenzahlen geprüft. |
| **C: Datenanalyse & Coding** | Claude 3.5 Sonnet | Erstellung von Python- und Pandoc-Skripten für die Word-Build-Pipeline und Datenbereinigung | *„Erstelle ein Python-Skript mit lxml, das in Word-DOCX Tabellen das Attribut cantSplit setzt.“* | `scripts/` & Anhang B | Code manuell getestet, debuggt und in die lokale Entwicklungsumgebung integriert. |
| **D: Sprachliches Lektorat** | Claude 3.5 Sonnet | Auffinden von Schachtelsätzen, Füllwörtern und unpräzisen Formulierungen im Rohentwurf | *„Überarbeite folgenden Rohentwurf: Streiche Füllwörter, forme Passivkonstruktionen in Aktiv um, behalte Fachbegriffe bei.“* | Kap. 1 bis 3 | Jeder Korrekturvorschlag einzeln manuell gegengelesen; keine ungeprüfte Textübernahme. |
| **E: Visualisierung** | ChatGPT (DALL-E / Python) | Generierung von schematischen Vektordiagrammen zur Veranschaulichung des Modellablaufs | *„Erstelle ein horizontales Ablaufdiagramm mit 4 Schritten: Input -> Validierung -> Synthese -> Output.“* | Kap. 2.2, Abb. 1 | Fachliche Korrektheit der Beschriftung überprüft und Layout manuell angepasst. |

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

