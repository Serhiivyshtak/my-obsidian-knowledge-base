# SQL DDL

Im Kontext von SQL ist **Data Definition Language (DDL)** eine Syntax zur Erstellung und Modifikation von Objekten wie *Datenbanken* und *Tabellen*. Es handelt sich dabei nicht um eine eigenständige Sprache, sondern um eine Sammlung von Anweisungen, die verwendet werden, um Tabellen, Spalten, Datentypen und Constraints zu deklarieren. Gängige Beispiele für DDL-Anweisungen sind `CREATE`, `ALTER` und `DROP`.

> Hinweis: Die genaue SQL-Syntax kann je nach verwendeter Umgebung variieren, daher kann nicht jeder Codeblock in diesem Kapitel in jeder Umgebung ausgeführt werden.

## Datenbankerstellung und -löschung

Um eine neue Datenbank zu erstellen, kann die Anweisung `CREATE DATABASE [DATENBANKNAME]` verwendet werden:

```sql
CREATE DATABASE my_database;
```

Um eine Datenbank zu löschen, wird in SQL das Schlüsselwort `DROP` verwendet:

```sql
DROP DATABASE my_database;
```

Falls versucht wird, eine nicht existierende Datenbank zu löschen, wird ein Fehler ausgegeben. Die Klausel `IF EXISTS` kann verwendet werden, um dies zu verhindern:

```sql
DROP DATABASE IF EXISTS my_database;
```

## Tabellenerstellung

Das Erstellen einer Tabelle ist ein etwas komplexerer Vorgang als das Erstellen einer Datenbank, da die Datentypen und Constraints für jede Spalte angegeben werden müssen. Hier ist ein Beispiel:

```sql
CREATE TABLE Humans (
    Human_Id INT PRIMARY KEY,
    Firstname VARCHAR(255) NOT NULL,
    Lastname VARCHAR(255) NOT NULL,
    Date_Of_Birth DATE NOT NULL
);
```

Dieser Code erstellt eine Tabelle namens *Humans*, die die Spalten *Human_Id*, *Firstname*, *Lastname* und *Date_Of_Birth* enthält. Die Datentypen werden direkt nach jedem Feldnamen angegeben (zum Beispiel `VARCHAR(255)` für *Firstname*). Außerdem sehen wir ein Beispiel für einen Constraint, der auf eine Spalte angewendet werden kann, nämlich `NOT NULL`. Das bedeutet, dass ein Feld mit diesem Schlüsselwort nicht leer sein darf. Jedes Mal, wenn versucht wird, einen Datensatz einzufügen, ohne dieses Feld anzugeben, wird ein Fehler ausgegeben (es sei denn, MySQL befindet sich im *Non-Strict Mode*).

Die `CREATE TABLE`-Anweisung kann auch verwendet werden, um eine neue Tabelle basierend auf einer bestehenden zu erstellen, zum Beispiel:

```sql
CREATE TABLE German_Customers AS
SELECT * FROM Customers
WHERE Country = 'Germany';
```

In diesem Fall werden die angegebenen Daten aus der Tabelle *Customers* basierend auf der Bedingung (Country = 'Germany') übernommen und in einer neuen Tabelle namens *German_Customers* gespeichert.

## Tabellenlöschung

Es gibt zwei Ansätze, um eine Tabelle in SQL zu löschen. Einer davon ist `DROP TABLE [TABELLENNAME]`. Dieser löscht sowohl die Daten als auch die Struktur, sodass die Tabelle nach der Ausführung des Befehls nicht mehr existiert:

```sql
DROP TABLE my_table;
```

Der zweite Ansatz zum Leeren einer Tabelle ist die Verwendung des Schlüsselworts `TRUNCATE`. Dieser Befehl löscht nur die Daten, ohne die Struktur der Tabelle zu entfernen. Das bedeutet, dass die Tabelle weiterhin existiert und anschließend mit neuen Daten befüllt werden kann:

```sql
TRUNCATE TABLE my_table;
```

Wie bei Datenbanken führt der Versuch, eine nicht existierende Tabelle zu löschen, zu einem Fehler. Die Klausel `IF EXISTS` kann verwendet werden, um dies zu verhindern:

```sql
DROP TABLE IF EXISTS my_table;
```

## Änderung der Tabellenstruktur

Die `ALTER TABLE`-Anweisung wird verwendet, um Spalten in einer bestehenden Tabelle hinzuzufügen, zu löschen oder zu modifizieren. Sie kann auch verwendet werden, um verschiedene Constraints einer bestehenden Tabelle hinzuzufügen oder zu entfernen. Beispiele:

```sql
ALTER TABLE my_table
ADD COLUMN new_column VARCHAR(255);
-- Fügt eine neue Spalte namens "new_column" zur Tabelle hinzu
```

```sql
ALTER TABLE my_table
DROP COLUMN old_column;
-- Löscht die Spalte "old_column"
```

```sql
ALTER TABLE my_table
RENAME COLUMN old_column TO new_column;
-- Benennt die Spalte "old_column" in "new_column" um
```

```sql
ALTER TABLE my_table
MODIFY COLUMN old_column VARCHAR(255) NOT NULL DEFAULT '***';
-- Modifiziert die Spalte "old_column" durch Festlegung eines neuen Datentyps und Standardwerts
```

```sql
ALTER TABLE my_table RENAME TO my_new_table;
-- Benennt die gesamte Tabelle in "my_new_table" um
```
