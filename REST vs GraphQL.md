# REST vs GraphQL

When building modern web applications, developers have two major options for accessing data from servers: [[REST APIs|REST]] and GraphQL. This summary explains both approaches, their differences, and when each one makes sense.

## What is GraphQL?

**GraphQL**, short for *Graph Query Language*, was created by Facebook to provide a more flexible and bandwidth-efficient alternative to REST. It was open-sourced in 2015 and has since become a popular choice for data-driven web applications, particularly JavaScript-based front-end frameworks that need to communicate with back-end data sources.

## Core Differences Between REST and GraphQL

The fundamental distinction lies in how you access data and what data is returned.

With **REST**, your data selection is defined by which **endpoint** you access. A REST API typically has multiple endpoints for different levels of data granularity. When you access an endpoint, all the data at that endpoint is returned. While some REST APIs allow filtering for more specificity, the response will always match the form and structure of the data at the resource.

With **GraphQL**, your data selection is defined by a **query** you send to a single endpoint. The GraphQL API uses your query to find the relevant data and returns only what you specified, structured to match your original query. This is what makes GraphQL *bandwidth-aware*: when used correctly, you receive only the data you requested and nothing else.

## The Library Analogy

Imagine two different library systems to understand these approaches:

A **REST library** organizes books in sections based on format, category, author, and other attributes. The librarian must visit each section separately to gather what you need, making multiple trips.

A **GraphQL library** stores all books in a large warehouse. The librarian controls a system that ingests your entire reading list and returns exactly what you asked for in one trip, including only the specific pages you requested if your query is that detailed.

## Practical Example: Checking Borrowed Books

Consider a simple task: finding out which books you currently have on loan from the library.

### The REST Approach

With REST, you need to make multiple requests. First, you send a request to the users endpoint with your ID to get your profile, which contains a list of checked-out books.

```
GET /users/987654
```

The API responds with your entire user profile, including data you did not ask for such as your address, phone number, and fine balance.

```JSON
{
  "userId": 987654,
  "name": "Morten Rand-Hendriksen",
  "email": "morten@example.com",
  "memberSince": "2006-04-15",
  "checkedOutBooks": [9780743273565, 9780452284234, 9780061120084],
  "fineBalance": 0,
  "address": "5432 Street",
  "phoneNumber": "5555555555"
}
```

Next, you must send separate requests for each book using their ISBN numbers. 

```
GET /books/9780743273565
GET /books/9780452284234
GET /books/9780061120084
```

This results in three separate responses, each containing complete book information including publisher, page count, genre, and physical location, even if you only wanted the titles and authors.

```json
{
  "isbn": 9780743273565,
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "publisher": "Scribner",
  "year": 1925,
  "pages": 180,
  "genre": "Fiction",
  "location": "3rd Floor, A-12"
}

{
  "isbn": 9780452284234,
  "title": "1984",
  "author": "George Orwell",
  "publisher": "Signet Classic",
  "year": 1949,
  "pages": 328,
  "genre": "Dystopian Fiction",
  "location": "3rd Floor, B-07"
}

{
  "isbn": 9780061120084,
  "title": "To Kill a Mockingbird",
  "author": "Harper Lee",
  "publisher": "Harper Perennial",
  "year": 1960,
  "pages": 324,
  "genre": "Fiction",
  "location": "3rd Floor, A-15"
}
```

This demonstrates how the relative rigidity of REST often results in more data than actually needed.

### The GraphQL Approach

With GraphQL, you send a single query specifying not only what to search for but also exactly what data you want returned and how it should be structured. For instance, you can request only your name and the titles, authors, and due dates of your checked-out books.

```GraphQL
query {
  user(id: 987654) {
    name
    checkedOutBooks {
      isbn
      title
      author
      dueDate
    }
  }
}
```

The response contains only the requested fields, structured exactly as specified in your query. No extra trips to the server, no unnecessary data transferred.

```json
{
  "data": {
    "user": {
      "name": "Morten Rand-Hendriksen",
      "checkedOutBooks": [
        {
          "isbn": 9780743273565,
          "title": "The Great Gatsby",
          "author": "F. Scott Fitzgerald",
          "dueDate": "2024-04-01"
        },
        {
          "isbn": 9780452284234,
          "title": "1984",
          "author": "George Orwell",
          "dueDate": "2024-04-05"
        },
        {
          "isbn": 9780061120084,
          "title": "To Kill a Mockingbird",
          "author": "Harper Lee",
          "dueDate": "2024-04-03"
        }
      ]
    }
  }
}
```

## Which Approach is Better?

Neither REST nor GraphQL is universally superior. They solve different problems for different use cases.

**REST** remains the standard for several reasons:

1. Easy implementation
2. Broad support across platforms and languages
3. Built-in cacheability for improved performance

**GraphQL** excels in scenarios requiring speed, efficiency, and reduced data loads, particularly for data-heavy applications like mobile apps and dynamic web applications.

When new services such as AI APIs come online, they almost always start with a REST API, with GraphQL as a potential future addition. This pattern reflects how REST continues to serve as the foundational approach, while GraphQL complements it for specific high-efficiency needs.

---

*Based on the LinkedIn Learning course "Learning REST APIs" by Morten Rand-Hendriksen.*
