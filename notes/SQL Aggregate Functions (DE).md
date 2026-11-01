# SQL-Aggregatfunktionen

**Aggregatfunktionen** sind spezielle SQL-Funktionen, die mehrere Werte aus einer oder mehreren Zeilen verarbeiten und daraus einen einzelnen Ergebniswert berechnen. Sie werden hauptsächlich verwendet, um Daten zusammenzufassen, statistisch auszuwerten oder Kennzahlen zu ermitteln und sie sind ein wichtiger Bestandteil der [[SQL (DE)|SQL]] Sprache.

In der Praxis kommen Aggregatfunktionen häufig in Berichten, Dashboards, Geschäftsanalysen und Datenanalysen zum Einsatz. Anstatt jede einzelne Zeile einer Tabelle zu betrachten, ermöglichen sie einen kompakten Überblick über größere Datenmengen.

Beispiele für typische Fragestellungen sind:

- Wie viele Kunden sind in der Datenbank gespeichert?
- Wie hoch ist der durchschnittliche Produktpreis?
- Welcher Mitarbeiter erhält das höchste Gehalt?
- Wie hoch ist der gesamte Umsatz eines Monats?

Für solche Aufgaben bieten SQL-Aggregatfunktionen eine einfache und effiziente Lösung.

Aggregatfunktionen arbeiten typischerweise auf einer bestimmten Spalte einer Tabelle und ignorieren dabei in den meisten Fällen automatisch **NULL-Werte**.

## COUNT()

Die Funktion **`COUNT()`** zählt die Anzahl von Datensätzen.

Sie wird häufig verwendet, um die Größe eines Datenbestands zu ermitteln oder festzustellen, wie viele Datensätze bestimmte Kriterien erfüllen.

Beispiele:

```SQL
SELECT COUNT(*) FROM employees;
-- Gibt die Gesamtzahl aller Zeilen der Tabelle zurück

SELECT COUNT(salary) FROM employees;
-- Zählt nur die Datensätze, bei denen die Spalte salary keinen NULL-Wert enthählt
```

## SUM()

Die Funktion **`SUM()`** berechnet die Summe aller Werte einer numerischen Spalte.

Sie eignet sich besonders für finanzielle Auswertungen und Kennzahlen.

Beispiel:

```SQL
SELECT SUM(salary) FROM employees;
-- Ergebnis entspricht der Summe aller Gehälter
```

## AVG()

Die Funktion **`AVG()`** berechnet den Durchschnitt einer numerischen Spalte.

Beispiel:

```SQL
SELECT AVG(salary) FROM employees;
-- Ergebnis zeigt das durchschnittliche Gehalt aller Mitarbeiter
```

## MIN()

Die Funktion **`MIN()`** liefert den kleinsten Wert einer Spalte.

Beispiel:

```SQL
SELECT MIN(salary) FROM employees;
-- der Befehl gibt das niedrigste Gehalt zurück
```

## MAX()

Die Funktion **`MAX()`** liefert den größten Wert einer Spalte.

Beispiel:

```SQL
SELECT MAX(salary) FROM employees;
-- Das Ergebnis zeigt das höchste Gehalt in der Tabelle
```

## Aggregatfunktionen mit WHERE

Aggregatfunktionen können mit der **`WHERE`**-Klausel kombiniert werden. Dadurch werden nur die Datensätze berücksichtigt, die eine bestimmte Bedingung erfüllen. Zum Beispiel:

```SQL
SELECT AVG(salary)
FROM employees
WHERE department = 'Sales';
```

Hier wird nur das durchschnittliche Gehalt der Mitarbeiter aus der Vertriebsabteilung berechnet.

Durch die Kombination von Aggregatfunktionen und Filterbedingungen lassen sich sehr gezielte Analysen durchführen.

## Zusammenfassung

**SQL-Aggregatfunktionen** dienen dazu, mehrere Datensätze zu einem einzelnen aussagekräftigen Ergebniswert zusammenzufassen. Sie gehören zu den wichtigsten Werkzeugen der Datenanalyse und Berichterstellung.

Die wichtigsten Funktionen sind:

| Funktion | Beschreibung |
| - | - |
| `COUNT()` | zählt Datensätze |
| `SUM()` | Berechnet die Summe |
| `AVG()` | Berechnet den Durchschnitt |
| `MIN()` | Liefert den kleinsten Wert |
| `MAX()` | Liefert den größten Wert |

In Kombination mit **`WHERE`** ermöglichen Aggregatfunktionen leistungsfähige Analysen großer Datenmengen. Sie bilden die Grundlage vieler Berichte, Kennzahlen und Business-Intelligence-Anwendungen und sind daher ein zentraler Bestandteil jeder SQL-Kenntnis.
