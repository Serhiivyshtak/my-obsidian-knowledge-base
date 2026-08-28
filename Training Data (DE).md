# Trainingsdaten

Wenn Computer lernen sollen, Vorhersagen zu treffen oder Muster zu erkennen, benötigen sie **Daten**, aus denen sie lernen können. Diese Daten nennt man **Trainingsdaten**. Je nach Art des Lernverfahrens unterscheiden sich die Anforderungen an diese Daten erheblich. Diese Zusammenfassung erklärt, was Trainingsdaten sind, woher sie kommen, wie sie aufbereitet werden und welche Rolle sie in verschiedenen Arten des Maschinellen Lernens spielen.

## Überwachtes Lernen

### Was ist überwachtes Lernen?

Die häufigste Form des Maschinellen Lernens ist das **überwachte Lernen**. Der Name kommt daher, dass dem Lernalgorithmus gewissermaßen ein "Lehrer" zur Seite steht, der ihm die richtigen Antworten zeigt.

> **Definition:** Beim überwachten Lernen braucht man als Trainingsdaten Beispieldaten, die sowohl die Faktoren beinhalten, die für die Vorhersage genutzt werden können, **als auch** das korrekte Ergebnis.

### Zwei konkrete Beispiele

Um das Konzept greifbar zu machen, betrachten wir zwei Beispiele aus dem Bereich der Eisverkäufe:

**Regressionsproblem — Wie viel Eis wird verkauft?**

Bei einem Regressionsproblem soll eine Zahl vorhergesagt werden. Die Trainingsdaten enthalten historische Informationen über Faktoren wie Temperatur, Wochentag und Bewölkung. Zusätzlich enthalten sie das korrekte Ergebnis — in diesem Fall die tatsächlichen Eisabsatzzahlen an jedem Tag. Der Algorithmus lernt aus diesen Daten, welche Faktoren die Verkaufszahlen wie stark beeinflussen.

**Klassifikationsproblem — Soll der Eisstand öffnen?**

Bei einem Klassifikationsproblem soll eine Kategorie vorhergesagt werden. Hier sind die Faktoren dieselben — Temperatur, Wochentag, Bewölkung — aber das korrekte Ergebnis ist nun die Information, ob der Eisstand an diesem Tag geöffnet oder geschlossen war. Der Algorithmus lernt, unter welchen Bedingungen sich eine Öffnung lohnt.

In beiden Fällen ist die Struktur der Trainingsdaten gleich: **Faktoren für die Vorhersage** plus **korrektes Ergebnis**.

## Woher kommen Trainingsdaten?

Die Beschaffung geeigneter Trainingsdaten ist oft eine der größten Herausforderungen beim Maschinellen Lernen. Die Daten können aus sehr unterschiedlichen Quellen stammen.

### Allgemeine Datenquellen

| Quelle | Beispiele |
|--------|-----------|
| **Offene Datenquellen** | OpenStreetMap, Wikipedia, Deutscher Wetterdienst |
| **Kommerzielle Anbieter** | Spezialisierte Datenanbieter, Marktforschungsunternehmen |
| **Digitalisierte Unternehmensprozesse** | Transaktionssysteme, Kundenkarten, Customer Relationship Management, elektronische Bestellungen und Lagerverwaltung |
| **Sensoren** | Temperatur-, Bewegungs-, Drucksensoren etc. |
| **Befragungen** | Kundenumfragen, Zielgruppenbefragungen |
| **Web-Tracking** | Nutzerverhalten auf Webseiten |
| **Social Media** | Öffentliche Posts, Kommentare, Interaktionen |

### Ein konkretes Beispiel

Beim Eisstand-Beispiel kommen die Daten aus verschiedenen Quellen zusammen. Die **Wetterdaten** stammen aus einer Datenbank des Deutschen Wetterdienstes. Der **Wochentag** lässt sich automatisch aus einem Kalender ableiten. Die **Absatzzahlen** hat die Betreiberin Yvonne jeden Abend von Hand eingetragen — alternativ könnten diese Daten auch automatisch aus einem digitalen Kassensystem stammen.

Interessant ist die Information über **Öffnung oder Schließung** des Stands. Diese war ursprünglich gar nicht in den Daten vorhanden und musste nachträglich ergänzt werden. In diesem Fall geschah das automatisch durch eine einfache Regel: Der Stand galt als "geschlossen", wenn weniger als 100 Portionen verkauft wurden.

## Was ist Annotation?

> **Definition:** Die nachträgliche Ergänzung von Merkmalen in Daten nennt sich **Annotation**. Häufig handelt es sich dabei um das Merkmal, das gelernt werden soll.

Annotation ist ein zentraler Schritt bei der Vorbereitung von Trainingsdaten für überwachtes Lernen. Ohne die Information, was das "richtige" Ergebnis ist, kann ein Algorithmus nicht lernen.

### Wie funktioniert Annotation?

Es gibt verschiedene Wege, Daten zu annotieren:

**Manuelle Annotation durch Experten** ist oft der zuverlässigste, aber auch aufwendigste Weg. Fachleute beurteilen beispielsweise medizinische Bilder (Hautkrebs ja/nein), kategorisieren Pflanzen auf Fotos, unterscheiden Hunde von Katzen oder transkribieren gesprochene Sprache in Text.

**Implizite Annotation durch Nutzerverhalten** entsteht automatisch durch die Reaktion von Nutzern oder Systemen. Wenn ein Kunde ein Produkt kauft oder nicht kauft, ist das eine implizite Bewertung. Wenn ein Nutzer die Ausgabe einer Spracherkennung korrigiert, liefert er damit Trainingsdaten für Verbesserungen. Wenn eine Maschine nach einer bestimmten Aktion weiterläuft oder ausfällt, ist auch das eine Form von Feedback.

**Annotation durch Schwellwerte** geschieht automatisch durch Überschreiten eines definierten Grenzwerts — wie im Eisstand-Beispiel, wo Verkaufszahlen unter 100 automatisch als "nicht rentabel" markiert wurden.

**Crowdsourcing** nutzt die kollektive Arbeit vieler Menschen. Auf spezialisierten Plattformen werden Laien für einfache Annotationsaufgaben bezahlt. Ein besonders bekanntes Beispiel ist **Google reCAPTCHA**: Wenn Sie beweisen müssen, dass Sie kein Roboter sind, indem Sie alle Bilder mit Ampeln oder Zebrastreifen anklicken, annotieren Sie gleichzeitig Trainingsdaten für Bilderkennungssysteme. Dies ist gewissermaßen eine "unfreiwillige" Form des Crowdsourcings — die Bezahlung erfolgt indirekt dadurch, dass man einen Dienst nutzen darf.

> **Wichtig:** Von Menschen annotierte Daten sind besonders wertvoll. Sie sind potentiell Trainingsdaten für Probleme, die bisher noch eher von Menschen erledigt werden — und damit der Schlüssel zur Automatisierung komplexer Aufgaben.

## Nicht überwachtes Lernen

### Was ist nicht überwachtes Lernen?

Beim nicht überwachten Lernen fehlt der "Lehrer" — es gibt kein vorgegebenes korrektes Ergebnis.

> **Definition:** Beim nicht überwachten Lernen wird dem Lernalgorithmus kein gewünschtes Ergebnis vorgegeben. Die Trainingsdaten enthalten also kein "korrektes" Ergebnis.

Der Algorithmus versucht stattdessen, selbstständig **Muster und Strukturen** in den Daten zu entdecken. Dies ist besonders nützlich, wenn noch nicht bekannt ist, was überhaupt als "korrekt" gelten soll.

### Arten des nicht überwachten Lernens

Es gibt drei wichtige Arten des nicht überwachten Lernens:

| Art | Beschreibung | Anwendungsbeispiel |
|----|--------------|-------------------|
| **Clusteranalyse (Clustering)** | Finden von Gruppen ähnlicher Datenpunkte | Kundentypen ermitteln, ungewöhnliche Ereignisse finden |
| **Assoziationsregeln** | Finden von Merkmalen, die miteinander zusammenhängen | Empfehlungssysteme: "Wer X kauft, kauft auch Y" |
| **Dimensionalitätsreduktion** | Vereinfachen von Datenmengen | Visualisierung komplexer Daten, Vorbereitung für überwachtes Lernen |

### Clustering im Detail

> **Definition:** Das Zuordnen von Daten zu Gruppen, die Gemeinsamkeiten aufweisen, nennt sich **Clustering**. Die gefundenen Gruppen werden als **Cluster** bezeichnet.

Ein anschauliches Beispiel verdeutlicht, wie Clustering funktioniert — und auch seine Grenzen. Stellen Sie sich eine Tabelle mit Tieren vor, die verschiedene Merkmale enthält: Farbe, Fortbewegungsart, ob das Tier Pelz hat und wie es atmet. Ein Clustering-Algorithmus könnte diese Tiere automatisch in Gruppen einteilen.

Dabei zeigt sich jedoch ein wichtiges Problem: Die Qualität des Clusterings hängt stark von den **gewählten Merkmalen** ab. Das Merkmal "Farbe" ist beispielsweise wenig hilfreich, wenn man hofft, durch Clustering Säugetiere von Fischen zu trennen — beide Gruppen enthalten graue Tiere. Das Merkmal "Atmung" (Lunge vs. Kiemen) wäre hier viel aussagekräftiger. Auch "Pelz" ist nicht optimal: Ein Wal hat keinen Pelz, ist aber trotzdem ein Säugetier. Das Merkmal "Haare" wäre hilfreicher, da auch Wale feine Haare besitzen.

**Vorteile des Clusterings:**

Das Clustering ermöglicht die Entdeckung von Gruppen mit ähnlichen Merkmalen — insbesondere dann, wenn diese Gruppen vorher nicht bekannt sind und daher kein überwachtes Lernen möglich wäre.

**Nachteile des Clusterings:**

Die Ergebnisse hängen sehr stark von den in den Trainingsdaten vorhandenen Merkmalen ab. Außerdem muss bei einigen Algorithmen zumindest die Anzahl der gesuchten Cluster im Voraus festgelegt werden — was problematisch ist, wenn man nicht weiß, wie viele Gruppen es gibt.

## Reinforcement Learning

### Was ist Reinforcement Learning?

Reinforcement Learning — auf Deutsch **verstärkendes Lernen** — unterscheidet sich fundamental von den beiden anderen Ansätzen.

> **Definition:** Beim Reinforcement Learning gibt es vorher keine Trainingsdaten. Die Daten zum Lernen werden erst während des Trainings gesammelt.

Das System startet gewissermaßen "von null". Es gibt keine historischen Beispiele mit korrekten Antworten. Stattdessen lernt das System durch **Ausprobieren**: Es führt Aktionen aus und erhält dafür entweder eine Belohnung (bei guten Ergebnissen) oder eine Bestrafung (bei schlechten Ergebnissen). Durch diese Rückmeldungen lernt es nach und nach, welche Aktionen in welchen Situationen am besten sind.

Ein typisches Beispiel ist ein Algorithmus, der lernt, Schach zu spielen. Er beginnt ohne jegliches Wissen über das Spiel, probiert Züge aus, verliert anfangs ständig und lernt durch die Niederlagen, welche Strategien erfolgversprechender sind. Die "Trainingsdaten" entstehen erst durch das Spielen selbst.

## Zusammenfassung: Trainingsdaten in verschiedenen Lernverfahren

| Lernverfahren | Trainingsdaten enthalten | Besonderheit |
|---------------|-------------------------|--------------|
| **Überwachtes Lernen** | Faktoren + korrektes Ergebnis | Ergebnis muss bekannt sein (ggf. durch Annotation) |
| **Nicht überwachtes Lernen** | Nur Faktoren (Merkmale) | Kein korrektes Ergebnis; Algorithmus findet selbst Muster |
| **Reinforcement Learning** | Keine vorab; entstehen während des Trainings | Lernen durch Belohnung und Bestrafung |

Die Wahl des richtigen Lernverfahrens hängt stark davon ab, welche Daten verfügbar sind und welches Problem gelöst werden soll. Wenn korrekte Ergebnisse bekannt und in ausreichender Menge vorhanden sind, ist überwachtes Lernen meist der effektivste Ansatz. Wenn man Strukturen in Daten entdecken möchte, ohne zu wissen, wonach genau man sucht, eignet sich nicht überwachtes Lernen. Und wenn man ein System durch Interaktion mit seiner Umgebung lernen lassen möchte — etwa bei Spielen oder Robotersteuerung — ist Reinforcement Learning der richtige Ansatz.

---

*Quelle: "Trainingsdaten" von Dr. Antje Schweitzer, Universität Stuttgart, Institut für Maschinelle Sprachverarbeitung / Institut für Software Engineering. Lizenziert unter CC BY 4.0.*
