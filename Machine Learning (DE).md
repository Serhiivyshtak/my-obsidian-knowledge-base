# Maschinelles Lernen

**Maschinelles Lernen** beschreibt den Prozess, bei dem Computer selbstständig aus Daten lernen, um Vorhersagen oder Entscheidungen zu treffen. Anstatt einem Computer explizit zu sagen, was er tun soll, zeigt man ihm Beispiele — sogenannte **Trainingsdaten** — aus denen er Muster und Regelmäßigkeiten erkennt. Diese Zusammenfassung erklärt das Konzept anhand eines anschaulichen Beispiels: der Entscheidung, ob ein Eisstand geöffnet werden soll oder nicht.


## Das Beispiel: Soll der Eisstand öffnen?

Stellen Sie sich vor, Sie betreiben einen Eisstand. An manchen Tagen verkaufen Sie viel Eis, an anderen fast gar nichts. Das Problem ist: Bei kleinen Verkaufsmengen ist der Stand **nicht rentabel**. Angenommen, es lohnt sich erst ab **100 verkauften Portionen**, den Stand zu öffnen.

Sie möchten nun ein System entwickeln, das Ihnen jeden Morgen sagt, ob Sie den Stand öffnen sollten oder nicht. Dafür schauen Sie sich vergangene Tage an und notieren für jeden Tag die **Bewölkung**, die **Temperatur** und ob der Stand an diesem Tag rentabel war (also mehr als 100 Portionen verkauft wurden).

Diese historischen Daten nennt man **Trainingsdaten**. Das Ziel ist es, daraus ein **Modell** zu erstellen, das für zukünftige Tage vorhersagen kann: *"offen"* oder *"geschlossen"*.

> **Wichtig:** Bei dieser Aufgabe handelt es sich nicht um *Regression* (Vorhersage einer Zahl), sondern um **Klassifikation** — die Vorhersage, welche von mehreren vordefinierten Kategorien (hier: "offen" oder "geschlossen") zutrifft.


## Was ist ein Entscheidungsbaum?

Ein **Entscheidungsbaum** ist eine der einfachsten und anschaulichsten Formen eines maschinell gelernten Modells. Er funktioniert wie ein Flussdiagramm: An jedem Punkt wird eine Frage gestellt, und je nach Antwort folgt man einem bestimmten Pfad, bis man zu einer Entscheidung gelangt.

### Aufbau eines Entscheidungsbaums

Ein Entscheidungsbaum besteht aus drei Elementen:

| Element | Beschreibung |
|---------|--------------|
| **Wurzel (Wurzelknoten)** | Der oberste Punkt des Baums, an dem die erste Frage gestellt wird |
| **Knoten (Verzweigungen)** | Punkte im Baum, an denen weitere Fragen gestellt werden |
| **Blätter** | Die Endpunkte des Baums, an denen die finale Entscheidung steht (z.B. "offen" oder "geschlossen") |

### Ein konkretes Beispiel

Ein fertiger Entscheidungsbaum für das Eisstand-Problem könnte so aussehen:

```
                    Temp. ≤ 20°?
                    /          \
                ja           nein
                /              \
            Werktag?           offen
            /      \
        ja       nein
        /          \
    Temp ≤ 10°?     geschlossen
    /     \
    ja      nein
    /         \
geschlossen offen
```


Der Baum liest sich so: Zuerst prüft man, ob die Temperatur 20 Grad oder weniger beträgt. Falls **nein** (also bei mehr als 20 Grad), öffnet der Stand. Falls **ja**, prüft man als nächstes, ob es ein Werktag ist. Falls es **kein Werktag** ist (also Wochenende), bleibt der Stand geschlossen. Falls es **doch ein Werktag** ist, schaut man auf die Temperatur: Bei 10 Grad oder weniger bleibt geschlossen, bei mehr als 10 Grad öffnet der Stand.


## Wie lernt der Computer einen Entscheidungsbaum?

Das **Training** eines Entscheidungsbaums erfolgt in einem systematischen, schrittweisen Prozess. Der Computer führt dabei genau die folgenden Schritte aus:

### Schritt 1: Das beste Merkmal finden

Der Computer probiert verschiedene Merkmale (z.B. Temperatur, Bewölkung, Wochentag) durch und sucht dasjenige, das die Trainingsdaten am besten in **zwei Gruppen mit möglichst ähnlichen Klassen** aufteilt. Das Ziel ist, dass nach der Aufteilung in jeder Gruppe möglichst nur noch Datenpunkte derselben Klasse sind — also entweder nur "offen" oder nur "geschlossen".

Im Eisstand-Beispiel stellt der Computer fest, dass die Frage *"Ist die Temperatur 20 Grad oder weniger?"* die Daten gut aufteilt: Alle Tage mit mehr als 20 Grad waren rentabel ("offen"), während bei den kälteren Tagen gemischte Ergebnisse vorliegen.

### Schritt 2: Knoten einfügen und Daten aufteilen

Sobald das beste Merkmal gefunden ist, fügt der Computer einen **Knoten** für dieses Merkmal ein. Die Trainingsdaten werden dann gemäß diesem Merkmal in **zwei Untermengen** aufgeteilt — eine für den linken Zweig (z.B. "ja, Temperatur ≤ 20°") und eine für den rechten Zweig (z.B. "nein, Temperatur > 20°").

### Schritt 3: Blätter oder weitere Knoten einfügen

Nun betrachtet der Computer jede Untermenge einzeln:

- Wenn **fast alle Datenpunkte** eines Zweigs dieselbe Klasse haben, wird ein **Blatt** mit dieser Klasse eingefügt. Der Zweig ist damit abgeschlossen.
- Wenn die Datenpunkte **gemischt** sind (also sowohl "offen" als auch "geschlossen" enthalten), wird ein **neuer Knoten** eingefügt und der Prozess beginnt für diese Untermenge wieder bei Schritt 1.

Dieser Prozess wiederholt sich **rekursiv**, bis alle Zweige in Blättern enden.

## Warum funktioniert das nicht immer perfekt?

In den Trainingsdaten kann es vorkommen, dass **identische Bedingungen** zu unterschiedlichen Ergebnissen führen. Zum Beispiel könnten zwei Tage mit exakt gleicher Temperatur und Bewölkung unterschiedliche Verkaufszahlen haben.

Dies kann zwei Ursachen haben:

- **Zufall** spielt eine Rolle (z.B. zufällig viele Touristen an einem Tag)
- **Unbekannte Faktoren** beeinflussen das Ergebnis, die nicht in den Daten erfasst sind (z.B. ein Feiertag, eine Veranstaltung in der Nähe)

Deshalb sind Vorhersagen durch maschinelles Lernen praktisch **nie perfekt** — sie sind jedoch oft gut genug, um nützliche Entscheidungen zu treffen.

## Zusammenfassung der wichtigsten Begriffe

| Begriff | Bedeutung |
|---------|-----------|
| **Maschinelles Lernen** | Computer lernen aus Daten, anstatt explizit programmiert zu werden |
| **Trainingsdaten** | Historische Daten, aus denen das Modell lernt |
| **Klassifikation** | Vorhersage einer Kategorie aus einer begrenzten Menge (z.B. "offen" vs. "geschlossen") |
| **Entscheidungsbaum** | Ein Modell in Baumstruktur, das durch Ja/Nein-Fragen zu einer Entscheidung führt |
| **Wurzel** | Der oberste Knoten des Baums (erste Frage) |
| **Knoten / Verzweigung** | Ein Punkt im Baum, an dem eine Frage gestellt wird |
| **Blatt** | Ein Endpunkt des Baums mit der finalen Entscheidung |

---

*Quelle: "Maschinelles Lernen – Beispiel Entscheidungsbaum" von Dr. Antje Schweitzer, Universität Stuttgart, Institut für Maschinelle Sprachverarbeitung / Institut für Software Engineering. Lizenziert unter CC BY 4.0.*
