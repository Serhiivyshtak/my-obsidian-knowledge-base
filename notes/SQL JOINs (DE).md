# SQL JOINs

In relationalen Datenbanken sind Informationen häufig auf mehrere Tabellen verteilt. Um diese Daten sinnvoll miteinander zu verknüpfen, stellt [[SQL (DE)|SQL]] die *JOIN-Klausel* bereit. Ein JOIN kombiniert Datensätze aus zwei oder mehr Tabellen auf Basis einer gemeinsamen Spalte und ermöglicht so komplexe Abfragen über zusammenhängende Daten.

## Was ist ein SQL JOIN?

Ein *JOIN* ist eine SQL-Anweisung, die Zeilen aus verschiedenen Tabellen zusammenführt. Die Verknüpfung erfolgt über eine Bedingung, die in der *ON-Klausel* definiert wird. Typischerweise werden dabei Spalten verglichen, die in beiden Tabellen existieren, etwa ein Primärschlüssel in der einen und ein Fremdschlüssel in der anderen Tabelle.

Stellen Sie sich zwei Tabellen vor: Eine enthält Kundendaten, die andere Bestellungen. Jede Bestellung verweist über eine Kunden-ID auf den zugehörigen Kunden. Mit einem JOIN lassen sich beide Tabellen so verbinden, dass zu jeder Bestellung auch die Kundeninformationen angezeigt werden.

## Die Grundsyntax

Die allgemeine Struktur einer JOIN-Abfrage sieht folgendermaßen aus:

~~~SQL
SELECT [ATTRIBUTE_NAMES]
FROM [FIRST_TABLE_NAME]
JOIN [SECOND_TABBLE_NAME]
ON [FIRST_TABLE_NAME].[ATTRIBUTE_NAME] = [SECOND_TABBLE_NAME].[ATTRIBUTE_NAME];
~~~

Die linke Tabelle steht in der *FROM-Klausel*, die rechte Tabelle folgt nach dem *JOIN-Schlüsselwort*. Die *ON-Klausel* definiert die Verknüpfungsbedingung.

## Die vier grundlegenden JOIN-Typen

SQL unterscheidet vier Haupttypen von JOINs, die sich darin unterscheiden, welche Datensätze in das Ergebnis aufgenommen werden.

### INNER JOIN

Der *INNER JOIN* ist der am häufigsten verwendete JOIN-Typ. Er gibt ausschließlich Datensätze zurück, bei denen die Verknüpfungsbedingung in beiden Tabellen erfüllt ist. Zeilen ohne passende Entsprechung in der jeweils anderen Tabelle werden verworfen.

~~~SQL
SELECT mitarbeiter.name, abteilung.bezeichnung
FROM mitarbeiter
INNER JOIN abteilung
ON mitarbeiter.abteilung_id = abteilung.id;
~~~

Diese Abfrage zeigt alle Mitarbeiter mit ihrer zugehörigen Abteilung. Mitarbeiter ohne zugewiesene Abteilung oder Abteilungen ohne Mitarbeiter erscheinen nicht im Ergebnis.

Das Schlüsselwort *INNER* ist optional. Ein einfaches *JOIN* ohne weitere Angabe entspricht einem INNER JOIN.

### LEFT JOIN

Der *LEFT JOIN* (auch *LEFT OUTER JOIN* genannt) behält alle Datensätze aus der linken Tabelle, unabhängig davon, ob eine Übereinstimmung in der rechten Tabelle existiert. Für Zeilen ohne Entsprechung werden die Spalten der rechten Tabelle mit *NULL-Werten* gefüllt.

~~~SQL
SELECT kunde.name, bestellung.bestellnummer
FROM kunde
LEFT JOIN bestellung
ON kunde.id = bestellung.kunde_id;
~~~

Das Ergebnis enthält alle Kunden. Kunden, die noch keine Bestellung aufgegeben haben, erscheinen ebenfalls, jedoch mit NULL in der Spalte für die Bestellnummer.

Dieser JOIN-Typ eignet sich besonders, wenn die linke Tabelle die maßgebliche Datenbasis darstellt und optionale Zusatzinformationen aus der rechten Tabelle angehängt werden sollen.

### RIGHT JOIN

Der *RIGHT JOIN* (auch *RIGHT OUTER JOIN* genannt) funktioniert spiegelbildlich zum LEFT JOIN. Er behält alle Datensätze aus der rechten Tabelle und ergänzt passende Daten aus der linken Tabelle. Fehlende Übereinstimmungen werden mit NULL-Werten aufgefüllt.

~~~SQL
SELECT mitarbeiter.name, projekt.bezeichnung
FROM mitarbeiter
RIGHT JOIN projekt
ON mitarbeiter.projekt_id = projekt.id;
~~~

Diese Abfrage zeigt alle Projekte, auch solche, denen noch kein Mitarbeiter zugeordnet ist.

In der Praxis wird der RIGHT JOIN selten verwendet. Die meisten Entwickler bevorzugen es, die Tabellenreihenfolge umzukehren und stattdessen einen LEFT JOIN zu schreiben, da dies besser lesbar ist.

### FULL OUTER JOIN

Der *FULL OUTER JOIN* (oder einfach *FULL JOIN*) kombiniert die Funktionsweise von LEFT und RIGHT JOIN. Er gibt alle Datensätze aus beiden Tabellen zurück. Übereinstimmende Zeilen werden zusammengeführt, nicht übereinstimmende Zeilen aus beiden Tabellen erscheinen mit NULL-Werten in den jeweils fehlenden Spalten.

~~~SQL
SELECT kunde.name, lieferant.firmenname
FROM kunde
FULL OUTER JOIN lieferant
ON kunde.region = lieferant.region;
~~~

Dieser JOIN-Typ ist besonders nützlich beim Abgleich zweier Datenquellen, etwa um festzustellen, welche Datensätze nur in einer der beiden Tabellen existieren.

Wichtiger Hinweis: MySQL unterstützt FULL OUTER JOIN nicht direkt. Als Workaround kann eine Kombination aus LEFT JOIN und RIGHT JOIN mit UNION verwendet werden.

## Vergleich der JOIN-Typen

| JOIN-Typ | Übereinstimmende Zeilen | Nicht übereinstimmende Zeilen links | Nicht übereinstimmende Zeilen rechts |
| - | - | - | - |
| INNER JOIN | werden angezeigt | werden verworfen | werden verworfen |
| LEFT JOIN | werden angezeigt | werden angezeigt (mit NULL) | werden verworfen |
| RIGHT JOIN | werden angezeigt | werden verworfen | werden angezeigt (mit NULL) |
| FULL OUTER JOIN | werden angezeigt | werden angezeigt (mit NULL) | werden angezeigt (mit NULL) |

## Häufige Fehlerquellen

Bei der Arbeit mit JOINs treten bestimmte Probleme immer wieder auf. Ein typischer Fehler ist das versehentliche Umwandeln eines LEFT JOIN in einen INNER JOIN. Dies geschieht, wenn eine Filterbedingung für die rechte Tabelle in der *WHERE-Klausel* statt in der *ON-Klausel* steht. Da NULL-Werte die WHERE-Bedingung nicht erfüllen, werden die entsprechenden Zeilen ausgeschlossen.

Ein weiteres Problem entsteht beim Verbinden von Spalten mit unterschiedlichen Datentypen. Implizite Typumwandlungen können dazu führen, dass vorhandene Indizes nicht genutzt werden und die Abfrage deutlich langsamer wird.

## Praktische Anwendungsfälle

JOINs sind in nahezu jeder datenbankbasierten Anwendung unverzichtbar. Im E-Commerce werden sie verwendet, um Bestellungen mit Kundendaten und Produktinformationen zu verknüpfen. In Personalsystemen verbinden sie Mitarbeiterdaten mit Abteilungen, Projekten und Gehaltsinformationen. Banken nutzen JOINs, um Kontodaten mit Transaktionen und Kundeninformationen zusammenzuführen.

Die Wahl des richtigen JOIN-Typs hängt von der konkreten Fragestellung ab. Sollen nur vollständig verknüpfte Datensätze erscheinen, ist INNER JOIN die richtige Wahl. Soll eine Seite vollständig erhalten bleiben, kommen LEFT oder RIGHT JOIN zum Einsatz. Für einen vollständigen Abgleich zweier Datenquellen eignet sich FULL OUTER JOIN.

---

*Quellen: [GeeksforGeeks – SQL Joins](https://www.geeksforgeeks.org/sql/sql-join-set-1-inner-left-right-and-full-joins/), [LearnSQL.de – SQL JOIN-Typen erklärt](https://learnsql.de/blog/sql-join-typen-erklaert/)*
