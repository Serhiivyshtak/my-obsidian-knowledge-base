# CRUD in SQL

**CRUD** ist ein Akronym für die vier grundlegenden Operationen, die auf Daten in einer Datenbank ausgeführt werden können:

- **Create (Erstellen)**
- **Read (Lesen)**
- **Update (Aktualisieren)**
- **Delete (Löschen)**

Diese vier Aktionen bilden das Fundament der Datenverwaltung in relationalen Datenbanken und gehören zu den wichtigsten Konzepten beim Erlernen von SQL. Nahezu jede Anwendung, die Daten speichert und verarbeitet, verwendet CRUD-Operationen. Dazu zählen beispielsweise Webanwendungen, Unternehmenssysteme, mobile Apps und Analyselösungen.

Wer mit Datenbanken arbeitet, muss Daten anlegen, abrufen, ändern und entfernen können. CRUD beschreibt genau diese grundlegenden Aufgaben in einer klaren und standardisierten Form.

Das Verständnis von CRUD hilft dabei:

- neue Datensätze anzulegen,
- bestehende Informationen abzurufen,
- Daten zu korrigieren oder zu aktualisieren,
- nicht mehr benötigte Daten zu entfernen.

Für Datenanalysten, Entwickler und Datenbankadministratoren bildet CRUD die Basis für nahezu alle weiteren SQL-Konzepte.

## Create (Erstellen)

**Create** bezeichnet das Anlegen neuer Datensätze in einer Datenbank.

In SQL wird dafür hauptsächlich die Anweisung **`INSERT`** verwendet. Mit ihr können neue Informationen in eine Tabelle eingefügt werden.

Die Create-Operation wird genutzt, um:

- neue Kunden anzulegen,
- Produkte zu erfassen,
- Bestellungen zu speichern,
- Stammdaten erstmals in die Datenbank einzutragen.

Syntax:

```SQL
INSERT INTO [TABLE_NAME] (...[TABLE_ATTRIBUTES]) VALUES (...[NEW_VALUES]);
```

Beispiel:

```SQL
INSERT INTO employees (employee_id, employee_firstname) VALUES (1, 'James');
```

## Read (Lesen)

**Read** steht für das Auslesen oder Abfragen von Daten.

Die SQL-Anweisung hierfür lautet **`SELECT`**. Sie ermöglicht es, gespeicherte Informationen anzuzeigen, ohne sie zu verändern.

Die Read-Operation wird verwendet, um:

- Datensätze anzuzeigen,
- Berichte zu erstellen,
- Analysen durchzuführen,
- bestimmte Informationen zu suchen oder zu filtern.

Syntax:

```SQL
SELECT [TABLE_ATTRIBUTES] FROM [TABLE_NAME]
```

Beispiele:

```sql
SELECT * FROM employees; 
-- '*' bedeutet, dass alle Spalten der Tabelle ausgegeben werden.

SELECT employee_id, employee_firstname, employee_birthdate FROM employees;
-- Hier werden 3 bestimmte Spalten ausgegeben
```

Die Read-Operation ist besonders wichtig für Datenanalysten. Sie ermöglicht das Extrahieren von Informationen für Berichte, Dashboards, statistische Auswertungen und Geschäftsentscheidungen.

## Update (Aktualisieren)

**Update** beschreibt das Ändern bereits vorhandener Daten.

Hierfür wird die SQL-Anweisung **`UPDATE`** verwendet.

Mit Update können:

- Fehler korrigiert,
- Preise angepasst,
- Adressänderungen gespeichert,
- bestehende Datensätze ergänzt werden.

Syntax:

```SQL
UPDATE [TABLE_NAME]
SET [TABLE_ATTRIBUTE] = [NEW_VALUE]
WHERE [TABLE_ATTRIBUTE] = [SPECIFIC_VALUE];
```

Beispiel:

```SQL
UPDATE clients
SET client_address = "Hauptstraße 12"
WHERE client_id = 10093;
```

> Wichtig: Die Verwendung einer **`WHERE`**-Klausel ist besonders wichtig. Ohne sie würden alle Datensätze der Tabelle aktualisiert werden.

## Delete (Löschen)

**Delete** dient zum Entfernen von Datensätzen aus einer Datenbank.

Dafür wird die SQL-Anweisung **`DELETE`** verwendet.

Datensätze werden gelöscht, wenn sie:

- veraltet sind,
- fehlerhaft sind,
- nicht mehr benötigt werden,
- die Datenqualität beeinträchtigen.

Syntax:

```SQL
DELETE FROM [TABLE_NAME]
WHERE [TABLE_ATTRIBUTE] = [SPECIFIC_VALUE];
```

Beispiel:

```SQL
DELETE FROM employees
WHERE employee_id = 10024;
```

> Wichtig: Auch bei Löschvorgängen sollte fast immer eine **`WHERE`**-Klausel verwendet werden. Andernfalls könnten sämtliche Datensätze einer Tabelle gelöscht werden.

## Zusammenfassung

**CRUD** beschreibt die vier grundlegenden Datenbankoperationen **Create, Read, Update und Delete**. Sie bilden die Basis jeder Datenverwaltung und gehören zu den ersten Konzepten, die beim Erlernen von SQL verstanden werden sollten.

Die entsprechenden SQL-Befehle sind:

- **`INSERT`** für das Erstellen neuer Datensätze
- **`SELECT`** für das Lesen von Daten
- **`UPDATE`** für das Aktualisieren bestehender Datensätze
- **`DELETE`** für das Löschen von Datensätzen

Wer CRUD sicher beherrscht, verfügt über die grundlegenden Werkzeuge, um Datenbanken effizient zu verwalten, Anwendungen zu entwickeln und Datenanalysen durchzuführen.
