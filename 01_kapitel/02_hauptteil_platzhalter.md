# 2 Hauptteil (Platzhalter für individuelle Fachkapitel)

> **Hinweis zur Gliederung:** Wissenschaftliche Arbeiten an der DHBW besitzen je nach Thema, Fachrichtung und methodischem Ansatz (z. B. quantitative empirische Studie, qualitative Experteninterviews, Literaturarbeit oder technischer Prototyp) eine individuelle Kapitelstruktur. 
> 
> Du kannst diesen Platzhalter durch deine eigenen modularen Kapitel-Dateien ersetzen (z. B. `02_theoretische_grundlagen.md`, `03_methodik.md`, `04_ergebnisse.md`, etc.) und diese anschließend in `build.sh` und `build.bat` eintragen.

---

## 2.1 Typischer Aufbau einer wissenschaftlichen Arbeit

Eine praxisorientierte wissenschaftliche Arbeit gliedert sich in der Regel nach folgendem Grundmuster:

1. **Theoretischer Bezugsrahmen / Stand der Forschung:**
   Definition der zentralen Fachbegriffe, Aufarbeitung des aktuellen Forschungsstands und Gegenüberstellung relevanter wissenschaftlicher Modelle oder Theorien.
2. **Methodik und Untersuchungsdesign:**
   Darstellung der empirischen oder analytischen Methode, Begründung der Fallauswahl, Stichprobenbeschreibung, Datenerhebung und Datenauswertung.
3. **Konzeption und praktische Durchführung:**
   Detaillierte Ausarbeitung des Lösungsansatzes, prototypische Implementierung oder Durchführung der Untersuchung im Kontext des Dualen Partners.
4. **Ergebnisse und empirische Befunde:**
   Objektive Darstellung der erhobenen Daten mit aussagekräftigen Abbildungen und Tabellen.
5. **Kritische Diskussion und Limitationen:**
   Interpretation der Ergebnisse im Lichte der Forschungsfragen, methodische Einschränkungen (Validität/Reliabilität) und praktische Handlungsempfehlungen für das Partnerunternehmen.
6. **Fazit und Ausblick:**
   Zusammenfassung der Kernaussagen und Aufzeigen zukünftiger Forschungsperspektiven.

## 2.2 Formatierungshinweise für Abbildungen, Tabellen und Formeln

### Abbildungen mit Beschriftung
Abbildungen werden mit Standard-Markdown eingebunden. Word und Pandoc generieren daraus automatisch zählbare Einträge für das Abbildungsverzeichnis:

![Schematischer Überblick des Untersuchungsdesigns](05_assets/logos/dhbw-logo.png){width=5.0cm}

### Tabellen mit Umbruchschutz
Tabellen werden übersichtlich in Markdown formatiert. Das Skript `scripts/table_layout_postprocess.py` sorgt automatisch dafür, dass Tabellen nicht unschön über Seitenumbrüche zerrissen werden (`cantSplit`):

| Untersuchungsschritt | Zielsetzung | Verwendete Methode | Datenbasis |
| :--- | :--- | :--- | :--- |
| Phase 1: Exploration | Problemabgrenzung | Literaturanalyse | 25 Peer-Review-Paper |
| Phase 2: Erhebung | Datengewinnung | Leitfadeninterviews | 8 Fachexperten |
| Phase 3: Synthese | Validierung | Qualitative Inhaltsanalyse | Transkripte (Anhang B) |

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```
