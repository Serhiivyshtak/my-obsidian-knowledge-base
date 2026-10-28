# SQLite

**SQLite** ist eine *relationale [Databases (DE)|Datenbank]-Engine*, die als freie und quelloffene Software verfügbar ist. Im Gegensatz zu herkömmlichen Datenbanksystemen wie MySQL oder PostgreSQL handelt es sich bei SQLite nicht um eine eigenständige Anwendung mit einem separaten Serverprozess. Stattdessen ist SQLite eine *Programmbibliothek*, die Softwareentwickler direkt in ihre Anwendungen einbetten. Der Name setzt sich aus "SQL" (Structured Query Language, der standardisierten Datenbanksprache) und "lite" (englisch für "leicht") zusammen.

Die Software wurde in der Programmiersprache C geschrieben und ist mit einer Groesse von nur etwa 699 KiB aussergewoehnlich kompakt. SQLite steht unter einer *Public-Domain-Lizenz*, was bedeutet, dass der Quellcode vollstaendig frei und ohne jegliche Einschraenkungen verwendet werden kann.

## Architektur und Funktionsweise

Das *serverlose Design* ist das zentrale Merkmal von SQLite. Waehrend klassische Datenbanksysteme einen separaten Serverprozess benoetigen, der Anfragen von Client-Anwendungen entgegennimmt, wird SQLite direkt in die Anwendung eingebunden. Die Kommunikation erfolgt ueber einfache Funktionsaufrufe, was die Latenz erheblich reduziert.

SQLite wird haeufig als *Zero-Configuration-Datenbank* bezeichnet. Konfigurationsaufgaben wie Dienstverwaltung, Startskripte oder passwortbasierte Zugriffskontrolle entfallen vollstaendig. Die Zugriffskontrolle wird stattdessen ueber die Dateisystemberechtigungen der Datenbankdatei geregelt.

Eine SQLite-Datenbank speichert alle Definitionen, Tabellen, Indizes und Daten in einer einzigen *plattformuebergreifenden Datei*. Mehrere Prozesse oder Threads koennen gleichzeitig auf dieselbe Datenbank zugreifen. Waehrend Lesevorgaenge parallel ausgefuehrt werden koennen, sind Schreibvorgaenge serialisiert, da die Datenbankdatei waehrend des Schreibens gesperrt wird.

## Technische Merkmale

SQLite implementiert den Grossteil des SQL-92-Standards und unterstuetzt wichtige Funktionen des relationalen Modells, einschliesslich *Transaktionen* mit ACID-Eigenschaften (Atomicity, Consistency, Isolation, Durability). Die Syntax orientiert sich an PostgreSQL, wobei SQLite standardmaessig keine strikte Typpruefung durchfuehrt. Das bedeutet, dass beispielsweise eine Zeichenkette in eine als Integer definierte Spalte eingefuegt werden kann.

SQLite verwendet ein ungewoehnliches *dynamisches Typsystem*: Anstatt einer Spalte einen festen Datentyp zuzuweisen, werden Typen den einzelnen Werten zugeordnet. Dies bietet Flexibilitaet, ist jedoch nicht auf andere SQL-Produkte uebertragbar.

Weitere unterstuetzte Funktionen umfassen:

- Volltextsuche ueber die FTS5-Erweiterung
- JSON-Unterstuetzung mit der json1-Erweiterung
- JSONB-Unterstuetzung seit 2024 fuer effizientere Verarbeitung

## Verbreitung und Einsatzgebiete

SQLite gilt als eine der am weitesten verbreiteten Datenbank-Engines weltweit. Die Software ist standardmaessig in zahlreichen Betriebssystemen integriert:

- Android
- iOS
- macOS (seit Mac OS X 10.4)
- Windows 10 und Windows 11
- NetBSD und verschiedene Linux-Distributionen

Auch alle gaengigen Webbrowser nutzen SQLite intern fuer verschiedene Zwecke. Google Chrome, Opera, Safari und der Android Browser ermoeglichen die Speicherung von Daten in SQLite-Datenbanken. Mozilla Firefox und Thunderbird speichern Konfigurationsdaten wie Lesezeichen, Cookies und Kontakte in internen SQLite-Datenbanken.

Viele Programmiersprachen bieten Schnittstellen zur SQLite-Bibliothek an, was die Integration in unterschiedlichste Anwendungen erleichtert. Ein eigenstaendiges Kommandozeilenprogramm namens *sqlite3* ermoeglicht die direkte Verwaltung von SQLite-Datenbanken.

## Qualitaetssicherung

SQLite zeichnet sich durch umfangreiche automatisierte Tests aus. Vor jeder Veroeffentlichung werden ueber 2 Millionen Tests durchgefuehrt. Waehrend die SQLite-Bibliothek selbst etwa 156.000 Zeilen Quellcode umfasst, enthalten die Testsuiten insgesamt 92 Millionen Zeilen Testcode. Seit August 2009 erreicht SQLite eine 100-prozentige Branch-Testabdeckung.

---

*Quelle: [Wikipedia - SQLite](https://en.wikipedia.org/wiki/SQLite)*
