# Datenmodelle und Relationenmodelle

In der heutigen digitalen Welt werden täglich enorme Mengen an Daten erzeugt, gespeichert und verarbeitet. Ob Online-Einkäufe, Bankgeschäfte, soziale Netzwerke oder Unternehmensanwendungen: Überall fallen Informationen an, die strukturiert und effizient verwaltet werden müssen. [[Databases (DE)|Datenbanken]] bilden dabei das Fundament nahezu jeder modernen Softwareanwendung.

Doch bevor Daten in einer Datenbank gespeichert werden können, muss zunächst festgelegt werden, wie diese Daten organisiert und miteinander in Beziehung gesetzt werden sollen. Genau hier kommen *Datenmodelle* ins Spiel. Sie beschreiben die Struktur der Daten und dienen als Bauplan für den Aufbau einer Datenbank.

## Was sind Datenmodelle?

Ein *Datenmodell* ist eine Beschreibung, wie Daten strukturiert, organisiert und gespeichert werden. Alle Menschen begegnen täglich Datenmodellen, ohne es zu wissen.

Beispiele für ein Datenmodell:

- Die Auflistung der Einkäufe, die erledigt werden müssen.
- Ein Fahrplan des ÖPNV an der Bushaltestelle.
- Schaubilder und Grafiken in Lehrbüchern.

Wie anhand der oben beschriebenen Beispiele sichtbar ist, lebt ein Datenmodell nicht unbedingt in einem Computer. Jedoch ist die erste und wichtigste Aufgabe eines Datenbankentwicklers beim Entwickeln einer Datenbank, sich ein Datenmodell zu überlegen, das die Anforderungen der Applikation erfüllt und ein sinnvolles sowie nachhaltiges Abspeichern von Daten ermöglicht.

Nachhaltig müssen Datenbanken sein, weil sie oft eine längere Lebensdauer haben als die Systeme, die auf ihnen basieren. Man kann auf einer Webseite beispielsweise das Aussehen des Anmeldeformulars ändern, die Datenbank bleibt aber erhalten. Daher ist es extrem wichtig, von Anfang an ein gut strukturiertes, nachhaltiges und sinnvolles Datenmodell zu wählen.

Angenommen, es gibt folgende Informationen, die Sie abspeichern möchten:

> Österreich hat den Ländercode AT. Die Hauptstadt von Österreich ist Wien. Die Fläche von Österreich beträgt 84. Ägypten hat den Ländercode EG. Die Hauptstadt von Ägypten ist Kairo. Die Fläche von Ägypten beträgt 1001. Deutschland hat den Ländercode DE. Die Hauptstadt von Deutschland ist Berlin. Die Fläche von Deutschland beträgt 357.

Es gibt mehrere Möglichkeiten, diese Information grafisch darzustellen. Ein Beispiel wäre in Form einer verschachtelten Auflistung:

- Datensatz 1
  - Land: Österreich
  - Ländercode: AT
  - Hauptstadt: Wien
  - Fläche: 84
- Datensatz 2
  - Land: Ägypten
  - Ländercode: EG
  - Hauptstadt: Kairo
  - Fläche: 1001
- Datensatz 3
  - Land: Deutschland
  - Ländercode: DE
  - Hauptstadt: Berlin
  - Fläche: 357

Ein weiteres Beispiel mit Verwendung einer Tabelle:

| Land | Ländercode | Hauptstadt | Fläche |
| - | - | - | - |
| Österreich | AT | Wien | 84 |
| Ägypten | EG | Kairo | 1001 |
| Deutschland | DE | Berlin | 357 |

## Arten der Datenmodelle

Das **konzeptuelle Datenmodell** stellt eine abstrakte, fachliche Darstellung der relevanten Objekte und ihrer Beziehungen dar, vollkommen unabhängig von technischen Details. In dieser Phase wird beispielsweise festgelegt, dass ein Online-Shop die Konzepte "Kunde", "Produkt" und "Bestellung" benötigt und dass ein Kunde mehrere Bestellungen aufgeben kann. Die beiden Datenmodelle aus dem vorherigen Kapitel sind Beispiele für ein konzeptuelles Datenmodell. Zur Darstellung werden häufig *Entity-Relationship-Diagramme* (ER-Diagramme) verwendet, die Entitäten als Rechtecke, Attribute als Ovale und Beziehungen als Rauten visualisieren. Auch die *Unified Modeling Language* (UML) mit ihren Klassendiagrammen kommt in dieser Phase zum Einsatz. Das Ziel ist eine gemeinsame Verständigungsgrundlage zwischen Fachexperten und Entwicklern, ohne dass technisches Vorwissen erforderlich ist.

Das **logische Datenmodell** bietet eine detailliertere Beschreibung mit Datentypen, Schlüsseln und konkreten Strukturen. Hier wird etwa definiert, dass ein Kunde die Attribute Kundennummer (Ganzzahl), Name (Text, maximal 100 Zeichen) und E-Mail-Adresse (Text) besitzt. In dieser Phase wird das konzeptuelle Modell in ein konkretes Datenbankmodell überführt, beispielsweise in das *Relationenmodell* mit seinen Tabellen, Primärschlüsseln und Fremdschlüsseln. Das Ergebnis ist ein detailliertes Tabellenschema, das alle Beziehungen, Datentypen und Constraints definiert, jedoch noch unabhängig von einem spezifischen Datenbankmanagementsystem bleibt.

Das **physische Datenmodell** beschreibt schließlich die technische Umsetzung und legt fest, wie die Daten tatsächlich in einer Datenbank gespeichert werden, einschließlich Indexstrukturen und Speicheroptimierungen. Die Implementierung erfolgt durch *SQL-Skripte* (insbesondere Data Definition Language), die Tabellen erstellen, Indizes anlegen und Speicherparameter konfigurieren. Hier werden auch DBMS-spezifische Optimierungen vorgenommen, etwa die Wahl des Speicherformats, die Partitionierung großer Tabellen oder die Definition von Stored Procedures und Triggern. Das physische Modell berücksichtigt die konkreten Eigenschaften des verwendeten Datenbankmanagementsystems wie MySQL, PostgreSQL oder Oracle und ist auf maximale Leistung und Effizienz ausgerichtet.

## Relationenmodelle

Das **Relationenmodell** ist das am weitesten verbreitete Datenmodell zur Organisation von Daten, das in Datenbanken verwendet wird. Im Relationenmodell werden Daten in *Tabellen* gespeichert, die als *Relationen* bezeichnet werden. Jede Tabelle besteht aus Zeilen und Spalten. Die *Zeilen* (auch *Tupel* genannt) entsprechen einzelnen Datensätzen, während die *Spalten* (auch *Attribute* genannt) die Eigenschaften dieser Datensätze beschreiben.

Ein wichtiges Element des Relationenmodells ist der *Primärschlüssel* (Primary Key). Dies ist ein Attribut oder eine Kombination von Attributen, das jeden Datensatz eindeutig identifiziert.

Wenn wir also unsere Tabelle aus dem ersten Kapitel nehmen und eine Spalte namens *Id* hinzufügen, erhalten wir ein folgendes Relationenmodell:

| Id | Land | Ländercode | Hauptstadt | Fläche |
| - | - | - | - | - |
| 1 | Österreich | AT | Wien | 84 |
| 2 | Ägypten | EG | Kairo | 1001 |
| 3 | Deutschland | DE | Berlin | 357 |

In diesem Fall könnten wir auch das Attribut *Ländercode* als Primärschlüssel nutzen, da Ländercodes meistens für jedes Land einzigartig sind. Außerdem könnte die Kombination aus den Attributen *Land* und *Hauptstadt* als Primärschlüssel dienen.
