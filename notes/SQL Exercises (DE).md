# SQL Übungen

Hier sind [[SQL (DE)|SQL]]-Übungen, die dazu dienen, die SQL-Kenntnisse zu vertiefen und das Schreiben von eigentlichem Code auf praktischen Beispielen zu üben.

Diese Übungen basieren auf der öffentlichen Datenbank von W3Schools. Um die Abfragen selbst auszuprobieren, kann der [W3Schools SQL Editor](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all) verwendet werden. Dort steht eine vollständige Beispieldatenbank mit Tabellen wie *Customers*, *Orders*, *Products*, *Employees* und weiteren zur Verfügung.

## Übungen zum SELECT

### Übung 1

> *Selektiere alle Waren, die 10 Euro oder weniger kosten, und sortiere diese aufsteigend nach dem Preis*

<details>
<summary>Lösung</summary>

~~~SQL
SELECT * FROM Products
WHERE Price <= 10
ORDER BY Price;
~~~

</details>

### Übung 2

> *Selektiere alle Mitarbeitenden, die vor dem ersten Oktober 1960 geboren sind*

<details>
<summary>Lösung</summary>

~~~SQL
SELECT * FROM Employees
WHERE BirthDate < '1960-10-01';
~~~

</details>

### Übung 3

> *Selektiere alle Mitarbeitenden, deren Vor- oder Nachname mit dem Buchstaben „l" anfängt*

<details>
<summary>Lösung</summary>

~~~SQL
SELECT * FROM Employees
WHERE FirstName LIKE 'l%' OR LastName LIKE 'l%';
~~~

</details>

### Übung 4

> *Selektiere alle Lieferanten, die ihren Sitz entweder in den USA, Japan oder Sweden haben*

<details>
<summary>Lösung</summary>

~~~SQL
SELECT * FROM Suppliers
WHERE Country IN ('USA', 'Japan', 'Sweden');
~~~

</details>

### Übung 5

> *Selektiere alle Waren, die in Flaschen angeboten werden*

<details>
<summary>Lösung</summary>

~~~SQL
SELECT * FROM Products
WHERE Unit LIKE '%bottles%';
~~~

</details>

## Übungen zu den JOINs

### Übung 1

> *Schreibe eine SQL-Anweisung, die die Tabellen ***Orders*** und ***OrderDetails*** vereinigt*

<details>
<summary>Lösung</summary>

~~~SQL
SELECT * FROM Orders
JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID;
~~~

</details>

### Übung 2

> *Vereinige die Tabellen ***Suppliers*** und ***Products***, sodass zu sehen ist, welcher Lieferant für welche Waren zuständig ist. Das Ergebnis soll die Attribute ProductID, ProductName und SupplierName zurückgeben*

<details>
<summary>Lösung</summary>

~~~SQL
SELECT ProductID, ProductName, SupplierName FROM Products
JOIN Suppliers ON Products.SupplierID = Suppliers.SupplierID;
~~~

</details>

### Übung 3

> *Vereinige die Tabellen ***Orders*** und ***Customers***, sodass zu sehen ist, welcher Kunde welche Bestellungen gemacht hat. Das Ergebniss soll nur die Datenätze zurückgeben, die im Jahr 1997 gemacht wurden*

<details>
<summary>Lösung</summary>

~~~SQL
SELECT * FROM Orders
JOIN Customers ON Orders.CustomerID = Customers.CustomerID
WHERE OrderDate >= '1997-01-01' AND OrderDate <= '1997-12-31';
~~~

Oder alternativ:

~~~SQL
SELECT * FROM Orders
JOIN Customers ON Orders.CustomerID = Customers.CustomerID
WHERE YEAR(OrderDate) = 1997;
~~~

</details>

### Übung 4

> *Selektiere alle Produkte die zur Kategorie ***Beverages*** gehören. Das Ergebnis soll die Attribute ProductID, ProductName, Price und CategoryName zurückgibt*

<details>
<summary>Lösung</summary>

~~~SQL
SELECT ProductID, ProductName, Price, CategoryName FROM Products
JOIN Categories ON Products.CategoryID = Categories.CategoryID
WHERE CategoryName = 'Beverages';
~~~

</details>

## Übungen zum GROUP BY

### Übung 1

> *Schreibe eine SQL-Abfrage, die die Anzahl der Lieferanten für jedes einzelne Land berechnet. Das Ergebnis soll den Namen des Landes und die Anzahl der Lieferanten zurückgeben*

<details>
<summary>Lösung</summary>

~~~SQL
SELECT Country, COUNT(*) AS SuppliersCount FROM Suppliers
GROUP BY Country;
~~~

</details>

### Übung 2

> *Schreibe eine SQL-Abfrage, die berechnet, wie viele Kunden aus jedem einzelnen Land kommen, und das Ergebnis nach Anzahl der Kunden absteigend sortiert*

<details>
<summary>Lösung</summary>

~~~SQL
SELECT Country, COUNT(*) AS CustomersCount FROM Customers
GROUP BY Country
ORDER BY CustomersCount DESC;
~~~

</details>

### Übung 3

> *Schreibe eine SQL-Abfrage, die die Anzahl der Produkte für jede einzelne Kategorie berechnet und die Datensätze nach Anzahl absteigend sortiert*

<details>
<summary>Lösung</summary>

~~~SQL
SELECT CategoryName, COUNT(*) AS ProductsCount FROM Products
JOIN categories ON Products.CategoryID = Categories.CategoryID
GROUP BY CategoryName
ORDER BY ProductsCount DESC
~~~

</details>

### Übung 4

> *Schreibe eine SQL-Abfrage, die die Anzahl der Bestellungen pro Mitarbeiter berechnet. Das Ergebnis soll den Identifier des Mitarbeiters, Vornamen, Nachnamen und die Anzahl der Bestellungen zurückgeben*

<details>
<summary>Lösung</summary>

~~~SQL
SELECT Employees.EmployeeID, FirstName, LastName, COUNT(*) AS OrdersCount FROM Orders
JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
GROUP BY Employees.EmployeeID, FirstName, LastName;
~~~

</details>

### Übung 5

> *Schreibe eine SQL-Abfrage, die berechnet, wie vie Umsatz jeder einzelne Mitarbeiter gemacht hat. Das Ergebnis soll den Identifier des Mitarbeiters, Vornamen, Nachnamen und den Umsatz zurückgeben*

<details>
<summary>Lösung</summary>

~~~SQL
SELECT Employees.EmployeeID, FirstName, LastName, SUM(price) AS Revenue FROM Orders
JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
JOIN Products ON OrderDetails.ProductID = Products.ProductID
GROUP BY Employees.EmployeeID, FirstName, LastName
ORDER BY Revenue DESC;
~~~

</details>

<!-- ## Komplexe Übungen

### Übung 1

> *Schreibe eine SQL-Abfrage, die den ältesten Mitarbeiter bzw. die älteste Mitarbeiterin findet.*

<details>
<summary>Lösung</summary>

~~~SQL
SELECT TOP 1 * FROM Employees
ORDER BY BirthDate DESC;
~~~

</details>

### Übung 4

> *Schreibe eine SQL-Abfrage, die berechnet, wie viel Umsatz insgesamt gemacht wurde und wie viele Artikel verkauft wurden.*

<details>
<summary>Lösung</summary>

~~~SQL
SELECT SUM(OrderDetails.Quantity * Products.Price) AS TotalRevenue, SUM(OrderDetails.Quantity) AS ItemsSold FROM OrderDetails
JOIN Orders ON OrderDetails.OrderID = Orders.OrderID
JOIN Products ON OrderDetails.ProductID = Products.ProductID;
~~~

</details>

### Übung 5

> *Schreibe eine SQL-Abfrage, die die Top 5 Kunden mit dem höchsten Umsatz zurückgibt. Das Ergebnis soll den Namen des Kunden, den Gesamtumsatz sowie die Anzahl der Bestellungen enthalten.*

<details>
<summary>Lösung</summary>

~~~SQL
SELECT TOP 5 CustomerName, COUNT(Orders.OrderID) AS OrdersAmount, SUM(Price) AS Revenue FROM Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID
INNER JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID
GROUP BY Customers.CustomerName
ORDER BY Revenue DESC;
~~~

</details> -->
