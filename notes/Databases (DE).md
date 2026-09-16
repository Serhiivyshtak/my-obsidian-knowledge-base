# Datenbanken

Eine *Datenbank* ist ein digitales Repository zum Speichern, Verwalten und Sichern organisierter Datensammlungen. Sie bildet die Grundlage für einen Großteil der modernen IT-Infrastruktur, einschließlich Websites, Apps und Plattformen.

Unterschiedliche Arten von Datenbanken speichern Daten auf unterschiedliche Weise. *Relationale Datenbanken* speichern Daten in definierten Tabellen mit Zeilen und Spalten, während *nicht-relationale Datenbanken* Daten in einer Vielzahl von Strukturen speichern können, darunter Schlüssel-Wert-Paare, Dokumente oder Graphen. *Vektordatenbanken* speichern Daten als Zahlenreihen, ein Format, das von vielen Anwendungen der künstlichen Intelligenz verwendet wird.

Unternehmen verfügen heute über gewaltige Datenmengen zu allen möglichen Themen, von Kundentransaktionen und Produktbeständen bis hin zu internen Prozessen und Forschungsprojekten. Diese Daten müssen in einer kohärenten Datenarchitektur organisiert werden, damit Benutzer und Anwendungen bei Bedarf darauf zugreifen können. Datenbanken sind mehr als nur ein Ort, um Informationen zu speichern. Sie ermöglichen Unternehmen die zentrale Verwaltung von Daten, die Durchsetzung von Datenintegrität und Sicherheitsstandards sowie den erleichterten Datenzugriff.

## Was eine Datenbank nicht ist

Der Begriff "Datenbank" wird oft sehr frei verwendet, was zu Verwirrung führen kann. Eine Datenbank ist ein System zur Speicherung und Verwaltung von Daten, das sowohl die physische Hardware, auf der die Daten gespeichert werden, als auch die Software umfasst, die den Zugriff auf die Daten organisiert und kontrolliert.

Websites, Apps und Plattformen wie Amazon oder Google sind selbst keine Datenbanken, aber sie stützen sich auf Datenbanken, um Informationen zu verwalten. Auch Microsoft Excel ist keine Datenbank, sondern eine Tabellenkalkulationsanwendung. Eine Excel-Tabelle organisiert Daten zwar in Zeilen und Spalten, ähnlich wie eine relationale Datenbank, aber es handelt sich um eine einzelne Datei. Datenbanken hingegen sind robuste, zentral verwaltete Systeme, die viele verschiedene Datentypen in vielen verschiedenen Formaten speichern können und komplexere Abfragen unterstützen.

## Typen von Datenbanken

Unternehmen verwenden verschiedene Arten von Datenbanken, um unterschiedliche Arten von Daten zu verwalten und unterschiedliche Anwendungen zu unterstützen.

### Navigationsdatenbanken

*Navigationsdatenbanken* speichern Daten in Form von verknüpften Datensätzen. Benutzer müssen zwischen diesen Datensätzen navigieren, um die gewünschten Daten zu erreichen. *Hierarchische Datenbanken* ordnen Daten in einer baumartigen Struktur aus übergeordneten und untergeordneten Datensätzen an. Jeder untergeordnete Datensatz kann nur einen einzigen übergeordneten Datensatz haben, aber übergeordnete Datensätze können mehrere untergeordnete Datensätze haben. *Netzwerkdatenbanken* verhalten sich ähnlich, mit der Ausnahme, dass jeder untergeordnete Datensatz mit mehreren übergeordneten Datensätzen verknüpft werden kann. Navigationsdatenbanken waren früher weit verbreitet, wurden aber durch die Entwicklung des relationalen Datenmodells weitgehend abgelöst.

### Relationale Datenbanken

*Relationale Datenbanken* speichern Daten in formatierten Tabellen aus Zeilen und Spalten. Sie werden manchmal auch als "SQL-Datenbanken" bezeichnet, da viele relationale Datenbanken die Verwendung der *Structured Query Language* (SQL) zur Abfrage und Bearbeitung von Daten unterstützen.

Jede Tabelle in einer relationalen Datenbank enthält Informationen zu einem bestimmten Entitätstyp. Beispielsweise könnte ein Unternehmen eine Tabelle mit Informationen zu all seinen Kunden haben, sowie separate Tabellen, in denen die Kaufhistorie jedes einzelnen Kunden aufgeführt ist.

Der IBM-Wissenschaftler Edgar F. Codd entwickelte in den 1970er Jahren das relationale Modell. Es übertraf schnell die Popularität des Navigationsmodells, da es das Abrufen von Daten erheblich vereinfacht. Anstatt Pfade zwischen Datensätzen anzugeben, können Benutzer SQL-Anweisungen verwenden, um die gewünschten Daten zu benennen. Relationale Datenbanken reduzieren auch die Redundanz, da jeder Datenpunkt nur einmal gespeichert werden muss.

### Nicht-relationale Datenbanken (NoSQL)

*Nicht-relationale Datenbanken* oder *NoSQL-Datenbanken* sind ein Sammelbegriff für Datenbanken, die Daten nicht in einem starren Format wie einer Tabelle speichern. Sie wurden entwickelt, um unstrukturierte und halbstrukturierte Datentypen wie Freiform-Text und Bilder zu unterstützen, die nicht genau in relationale Tabellen passen.

*Graphdatenbanken* speichern Daten als "Knoten" (die Entitäten darstellen) und "Edges" (die Beziehungen zwischen ihnen darstellen). Sie werden häufig verwendet, um Beziehungen nachzuvollziehen, etwa die Verbindungen zwischen Nutzern eines sozialen Netzwerks.

*Dokumentendatenbanken* speichern Daten als Dokumente in Formaten wie JSON, XML oder BSON. Sie sind in Content-Management-Systemen weit verbreitet.

*Schlüssel-Wert-Datenbanken* speichern Informationen als Schlüssel-Wert-Paare, wobei die Schlüssel eindeutige Kennungen sind und die Werte Datenfelder darstellen.

*Datenbanken mit breiten Spalten* verwenden Zeilen und Spalten ähnlich wie relationale Datenbanken, wobei jede Zeile jedoch ihren eigenen Satz von Spalten haben kann.

### Objektorientierte Datenbanken

*Objektorientierte Datenbanken* speichern Daten als Objekte im Sinne der objektorientierten Programmierung. Objekte sind Bündel von Informationen und zugehörigem Code. Jedes Objekt stellt eine Entität dar, ist in Klassen gruppiert und verfügt über Attribute, die seine Eigenschaften beschreiben, sowie Methoden, die sein Verhalten definieren. Ein Objekt der Kategorie "Katze" könnte beispielsweise die Attribute "Farbe" und "Gewicht" sowie die Methoden "Schnurren" und "Jagen" haben.

### Vektordatenbanken

*Vektordatenbanken* speichern Informationen als Zahlenreihen, die als "Vektoren" bezeichnet werden und nach Ähnlichkeit gruppiert werden. Ein Wettermodell könnte etwa die Tiefst-, Mittel- und Höchsttemperaturen für einen Tag in Vektorform speichern: [16, 22, 29]. Vektoren können auch komplexe Objekte wie Wörter, Bilder, Videos und Audio darstellen. Hochdimensionale Vektordaten sind unerlässlich für maschinelles Lernen, Verarbeitung natürlicher Sprache und andere KI-Aufgaben.

### Cloud-Datenbanken

*Cloud-Datenbanken* sind Datenbanken, die in der Cloud gehostet werden. Jede Art von Datenbank kann eine Cloud-Datenbank sein. Es gibt zwei Haupttypen: selbstverwaltete Datenbanksysteme, die in der Cloud laufen, und *Database as a Service* (DBaaS), ein Cloud-Computing-Service, der es Benutzern ermöglicht, auf Datenbanksoftware zuzugreifen, ohne das System selbst verwalten zu müssen. Cloud-Datenbanken sind besser skalierbar als On-Premises-Datenbanken.

## Funktionsweise einer Datenbank

Ein Datenbanksystem besteht aus zwei Schlüsselkomponenten: dem *Datenspeichersystem*, das die Daten physisch oder logisch beherbergt, und dem *Datenbankmanagementsystem* (DBMS), das es Benutzern ermöglicht, mit den gespeicherten Datensätzen zu interagieren.

### Datenbank-Hardware

Datenbanken müssen ihre Daten auf irgendeiner Art von Hardware speichern. Die meisten Datenbanksysteme bestehen aus einer Datenbanksoftware, die auf einem Computer, Server oder einem anderen Gerät ausgeführt wird. Der Computer stellt die physische Hardware bereit, während die Software die logische Anordnung der Daten übernimmt.

Eine Datenbank und die Anwendungen, die sie nutzen, können auf derselben Hardware laufen, aber heutzutage verwenden die meisten Datenbanksysteme eine mehrschichtige Architektur, die Anwendungsserver und Datenbankserver voneinander trennt. Diese Anordnung bietet mehr Skalierbarkeit und Zuverlässigkeit.

### Datenbankmanagementsysteme (DBMS)

Ein *Datenbankmanagementsystem* (DBMS) ist eine Software, die es Datenbankadministratoren, Benutzern und Anwendungen ermöglicht, auf Daten in einer Datenbank zuzugreifen. Mit DBMS können Benutzer wichtige Aufgaben der Datenverwaltung ausführen, etwa Datenbanken formatieren, Metadaten verwalten, Datensätze abfragen sowie Daten hinzufügen, aktualisieren oder löschen.

Zu den gängigen Datenbankverwaltungssystemen gehören *MySQL* (häufig für E-Commerce-Websites und Web-Apps verwendet), *PostgreSQL* (bekannt für Erweiterbarkeit und Transaktionszuverlässigkeit), *Microsoft SQL Server*, *Oracle Database* und *IBM Db2*.

### Datenbanksprachen

*Datenbanksprachen* sind spezielle Programmiersprachen, mit denen Menschen mit Datenbanken interagieren. Die am häufigsten verwendete Datenbanksprache ist die *Structured Query Language* (SQL), die von den meisten relationalen Datenbanken verwendet wird. SQL wurde in den 1970er Jahren von IBM-Wissenschaftlern entwickelt und unterstützt Aufgaben wie Datendefinition, Zugriffskontrolle, Datenfreigabe, Datenintegration und analytische Abfragen.

## Die Struktur einer relationalen Datenbank

Eine relationale Datenbank besteht aus mehreren Komponenten, die hierarchisch organisiert sind.

Die *Tabelle* ist ein Datenbankobjekt, das eine Datensammlung für ein bestimmtes Thema enthält. Tabellen bestehen aus Zeilen und Spalten. Die *Spalte* ist die vertikale Komponente einer Datenbanktabelle. Sie hat einen Namen und einen bestimmten Datentyp, etwa Zeichen, Dezimalzahlen oder ganze Zahlen. Die *Zeile* ist die horizontale Komponente einer Tabelle und besteht aus einer Sequenz von Werten, einem für jede Spalte der Tabelle.

---

*Quellen:*

- IBM Think: [Was ist eine Datenbank?](https://www.ibm.com/de-de/think/topics/database)
- IBM Docs: [Struktur relationaler Datenbanken](https://www.ibm.com/docs/de/mci/7.6.2?topic=design-relational-database-structure)
