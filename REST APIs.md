# REST APIs

REST APIs are fundamental building blocks of modern web and mobile applications. This summary explains what they are, how they work, and why they matter, using accessible analogies and clear definitions.

## The Library Analogy

To understand REST APIs, imagine a library scenario. On one side, you have **clients**, which are the applications requesting data, such as web apps, mobile apps, smartwatches, or any device that needs access to information. On the other side sits a **data store**, typically a database or server holding the actual information. In the middle is the **REST API**, acting as the librarian who receives, processes, and handles all requests and responses between clients and the data store.

When a client submits a request, the REST API identifies the requested resource, gathers the necessary data in the appropriate format, and bundles it with a **response header** containing metadata such as the resource ID, hyperlinks to available actions, and media format information. The client then parses this data into something meaningful while the API waits for the next request.

## What REST and API Actually Mean

**REST** stands for *Representational State Transfer*, which refers to a group of software architecture design constraints that produce efficient, reliable, and scalable systems. REST is not a specific technology but rather a design methodology that delivers predictable and consistent outputs by receiving standard methods called **verbs** and returning standardized structured data, typically **JSON** or **XML**, called the **resource**.

**API** stands for *Application Programming Interface*, a set of features and rules inside a software program that enable interaction between the software and other items, including other software or hardware.

## Traditional Websites vs. REST-Based Applications

A traditional website serves individual HTML documents. Each page requires a complete document to be generated, downloaded, and rendered in the browser. This approach works but is resource-intensive.

A REST-based **web application** works differently. When a visitor first loads the site, all components are downloaded once, including the HTML framework, stylesheets, and JavaScript. The application then sends **URI** (Universal Resource Identifier) requests for data representing the next state. When navigating between views, only the data changes are transferred, not entire new files. This enables:

1. **Single Page Applications** on the web that update content without full page reloads
2. **Native mobile apps** that consume the same REST resources as their web counterparts
3. **Cross-platform consistency**, where different applications access the same data from the same REST resource

## Common REST Verbs

The API provides a collection of tools called verbs to work with REST resources:

- **GET**: Retrieve data from the server
- **POST**: Submit new data to the server
- **PUT**: Update existing data on the server
- **DELETE**: Remove data from the server

Think of the REST resource as a librarian and the API as the language you use to communicate with them. You might say "please get me the 10 most recent articles" or "please put this document in the library under a specific category."

## Why REST APIs Matter

REST APIs enable different applications to access the same data consistently. For example, when you visit LinkedIn on both your computer and smartphone, you use two different applications consuming the same data from the same REST resource. This architecture supports scalability, as the same request and response flow works whether one client or millions of clients are making requests simultaneously.

---

*Based on the LinkedIn Learning course "Learning REST APIs" by Morten Rand-Hendriksen.*
