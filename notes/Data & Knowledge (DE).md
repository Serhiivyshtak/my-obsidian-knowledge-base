# Daten und Wissen

In der heutigen Welt spielen **Daten** eine zentrale Rolle — nicht nur in der Wissenschaft und Technik, sondern auch im Alltag. Doch Daten allein sind noch nicht besonders nützlich. Ihr wahrer Wert entfaltet sich erst, wenn wir **Wissen** aus ihnen gewinnen. Diese Zusammenfassung erklärt anhand eines einfachen Beispiels — der Vorhersage von Eisverkäufen — wie der Weg von Daten zu Wissen funktioniert und welche verschiedenen Ansätze es dafür gibt.

> **Kernaussage:** Daten enthalten Wissen. Es muss nur zugänglich gemacht werden — zum Beispiel durch Abstraktion.

## Das Beispiel: Eisverkäufe vorhersagen

Stellen Sie sich vor, Sie betreiben einen Eisstand und möchten wissen, wie viel Eis Sie für morgen bestellen sollten. Sie haben verschiedene Möglichkeiten, diese Frage zu beantworten. Interessanterweise lassen sich diese Möglichkeiten in **drei grundlegende Strategien** einteilen, die jeweils unterschiedliche Wege beschreiben, wie Menschen (und Computer) aus Daten lernen können.

## Strategie 1: Expert\*innen befragen

Der erste und vielleicht naheliegendste Ansatz ist, jemanden zu fragen, der sich auskennt. **Expert\*innen** haben durch ihre Arbeit über Jahre hinweg Erfahrungen gesammelt. Sie wurden dabei ständig mit Fakten und Situationen konfrontiert und haben gelernt, darin Regelmäßigkeiten zu erkennen.

### Wie Expert\*innen zu ihrem Wissen kommen

Expert\*innen gewinnen ihr Wissen auf zwei Wegen. Erstens sammeln sie durch ihre praktische Arbeit **direkte Erfahrungen** — sie beobachten, was funktioniert und was nicht. Zweitens erhalten sie Wissen in bereits **abstrahierter Form** von anderen Expert\*innen, etwa durch Fachliteratur, Theorien oder Ausbildung. Dieses Wissen basiert wiederum auf den Daten und Erfahrungen der ursprünglichen Expert\*innen.

### Wie Expert\*innen ihr Wissen weitergeben

Expert\*innen können ihr Wissen in verschiedenen Formen ausdrücken — etwa als **Regeln**, **Anweisungen** oder **Schaubilder**. Ein erfahrener Eisverkäufer könnte beispielsweise folgende Regel formulieren:

> *"Bis 10 Grad: nichts bestellen. 10 bis 20 Grad: 50 Portionen. 20 bis 30 Grad: 100 Portionen. Über 30 Grad: 200 Portionen. Bei Sonne die Bestellung verdoppeln."*

Solches abstrahiertes Wissen nennt man ein **Modell**. Ein Modell ist eine *vereinfachte Beschreibung der Realität*, die das Wesentliche erfasst, ohne jeden Einzelfall berücksichtigen zu müssen.

## Strategie 2: Daten analysieren

Anstatt Expert\*innen zu befragen, kann man auch direkt die **vorhandenen Daten** untersuchen. Bei diesem Ansatz gibt es zwei unterschiedliche Vorgehensweisen, die sich fundamental in ihrer Herangehensweise unterscheiden.

### Variante A: Regelmäßigkeiten in den Daten entdecken

Bei dieser Variante durchsucht man die Daten systematisch nach **Mustern und Regelmäßigkeiten**. Das Ergebnis ist abstrahiertes Wissen, das dem Expertenwissen ähnelt — etwa Regeln wie *"Im Sommer bei sehr heißem Wetter 200 Portionen bestellen, sonst 150 Portionen"* oder sogar einfache Formeln wie *"Bestellmenge = Temperatur mal 10"*.

Der wichtige Unterschied zum Expertenwissen ist, dass dieses Wissen **nur aus einer Datenquelle** gewonnen wird, während Expert\*innen typischerweise auf vielfältigere Erfahrungen und zusätzliche Theorien zurückgreifen können.

Wenn ein **Computer** diese Analyse durchführt, spricht man von **Maschinellem Lernen**. Maschinelles Lernen extrahiert also Wissen aus Daten. Das dabei entstehende abstrahierte Wissen nennt man ebenfalls **Modell** — zur Abgrenzung von menschlich erstellten Modellen spricht man manchmal explizit von **KI-Modellen** oder **Machine Learning-Modellen**.

### Variante B: Ähnliche Fälle in der Vergangenheit suchen

Die zweite Variante verzichtet bewusst auf jede Abstraktion. Stattdessen sucht man in den historischen Daten nach einem **Tag mit möglichst ähnlichen Bedingungen** (etwa ähnliche Temperatur und Bewölkung) und übernimmt einfach die damalige Bestellmenge.

Dieser Ansatz wird als **Instanzbasiertes Lernen** bezeichnet — im Englischen auch *"instance-based learning"* oder *"lazy learning"* genannt. Der Begriff "lazy" (faul) kommt daher, dass keine aufwendige Abstraktion im Voraus stattfindet; die eigentliche Arbeit wird auf den Moment der Vorhersage verschoben.

## Strategie 3: Versuch und Irrtum

Die dritte Strategie unterscheidet sich grundlegend von den ersten beiden: Hier beginnt man ohne Vorwissen und lernt **durch eigene Erfahrungen**. Dieser Ansatz ist dem menschlichen Lernen sehr ähnlich — denken Sie an ein Kind, das durch Ausprobieren lernt, wie die Welt funktioniert.

### Wie Lernen durch Versuch und Irrtum funktioniert

Am Anfang ist es fast wie ein Ratespiel: Man trifft eine Entscheidung, beobachtet das Ergebnis und passt seine Strategie entsprechend an. Jeder Versuch erzeugt dabei **neue Erfahrungen** — und Erfahrungen sind letztlich nichts anderes als neue Daten.

Ein Eisverkäufer könnte beispielsweise so beginnen: Er bestellt zunächst immer 100 Portionen. Nach einigen Tagen bemerkt er, dass er bei schlechtem Wetter zu viel, bei gutem Wetter zu wenig bestellt. Also passt er seine Regel an: *"Bei schlechtem Wetter 100 Portionen, sonst 300 Portionen."* Später fügt er vielleicht noch hinzu: *"Im Winter 200 Portionen weniger bestellen."* Mit jedem Fehler wird die Regel besser.

### Verstärkendes Lernen (Reinforcement Learning)

Wenn Computer auf diese Weise lernen, spricht man von **Verstärkendem Lernen** oder **Reinforcement Learning**. Das System startet meist *"bei Null"* und lernt durch die Konsequenzen seiner Aktionen.

Ein wichtiges Merkmal des Reinforcement Learning ist, dass das Feedback oft **indirekt** erfolgt. Beim Schachspielen beispielsweise erfährt das System nicht nach jedem einzelnen Zug, ob dieser gut oder schlecht war. Stattdessen lernt es erst am Ende einer Partie, welche Aktionen möglicherweise zum Sieg beigetragen haben — manchmal liegt die entscheidende Aktion viele Züge zurück.

Die lernende Komponente eines solchen Systems bezeichnet man oft als **Agenten**. Der Agent interagiert mit seiner Umgebung, sammelt Erfahrungen und verbessert kontinuierlich seine Strategie.

## Was ist ein Modell?

Der Begriff **Modell** ist in diesem Zusammenhang zentral und verdient eine genauere Betrachtung.

> **Definition:** Ein Modell ist eine abstrahierte — also vereinfachte — Beschreibung der Realität.

Ein gutes Modell erfasst die wesentlichen Zusammenhänge, ohne sich in unwichtigen Details zu verlieren. Es ermöglicht Vorhersagen für Situationen, die man so noch nie gesehen hat, indem es allgemeine Prinzipien formuliert. Mit einfachen Worten Modelle ermöglichen zwei Sachen — besseres Verständnis der Daten und das Generieren der Vorhersagen.

Modelle können sehr unterschiedliche Formen annehmen:

| Form | Beispiel |
|------|----------|
| Einfache Regeln | *"Bei Regen bleibt der Stand geschlossen"* |
| Bedingte Anweisungen | *"Wenn Temperatur > 25°, dann 200 Portionen bestellen"* |
| Mathematische Formeln | *"Bestellmenge = Temperatur × 10"* |
| Komplexe Regelwerke | Kombinationen aus mehreren Faktoren mit Ausnahmen |
| Schaubilder und Diagramme | Visuelle Darstellung von Zusammenhängen |

Ein wichtiger Unterschied besteht zwischen Modellen, die von **Menschen** erstellt wurden, und solchen, die durch **Maschinelles Lernen** entstanden sind. Letztere basieren häufig auf weniger Daten — insbesondere auf *weniger diversen Daten* — als Modelle, die von erfahrenen Expert\*innen entwickelt wurden. Expert\*innen können zusätzlich theoretisches Wissen, gesunden Menschenverstand und Erfahrungen aus völlig anderen Bereichen einbringen.

## Zusammenfassung: Drei Wege von Daten zu Wissen

Die drei vorgestellten Strategien lassen sich wie folgt gegenüberstellen:

| Strategie | Datenquelle | Abstraktion | Fachbegriff im ML |
|-----------|-------------|-------------|-------------------|
| Expert\*innen befragen | Vielfältige Erfahrungen + theoretisches Wissen | Ja | — |
| Regelmäßigkeiten in Daten finden | Eine spezifische Datenquelle | Ja | **Maschinelles Lernen** |
| Ähnliche Fälle suchen | Eine spezifische Datenquelle | Nein | **Instanzbasiertes Lernen** |
| Versuch und Irrtum | Selbst erzeugte Erfahrungen | Ja | **Reinforcement Learning** |

Jeder dieser Ansätze hat seine Berechtigung. Expert\*innen-Wissen ist oft robust und vielseitig, aber nicht immer verfügbar oder skalierbar. Maschinelles Lernen kann riesige Datenmengen verarbeiten, ist aber nur so gut wie die zugrunde liegenden Daten. Instanzbasiertes Lernen ist einfach und transparent, funktioniert aber nur gut, wenn genügend ähnliche Fälle in den Daten vorhanden sind. Reinforcement Learning eignet sich besonders für Situationen, in denen man durch Interaktion mit einer Umgebung lernen kann — etwa bei Spielen oder bei der Steuerung von Robotern.

---

*Quelle: "Daten und Wissen" von Dr. Antje Schweitzer, Universität Stuttgart, Institut für Maschinelle Sprachverarbeitung / Institut für Software Engineering. Lizenziert unter CC BY 4.0.*
