# Resources and Representations

This summary explains two fundamental concepts in [[REST APIs|REST]] architecture: *resources* and *representations*. These terms are essential for understanding how modern web APIs communicate and exchange data.

## Resources: The Core Abstraction

A **resource** is the key abstraction of information in REST. According to Fielding, any information that can be named can be a resource. This includes documents, images, services (such as today's weather in a specific city), collections of other items, or even real-world objects like a person.

The critical insight is that a resource is a *conceptual mapping* to a set of entities, not the actual entity itself at any given moment. Think of it like a label pointing to something rather than the thing itself. For example, if you have a library cubby labeled "red book in cubby number four," that label is the resource. If someone swaps the book for a different one, the resource still points to whatever is currently in that location.

Resources come in two forms:

1. **Singleton resources** point to a single item (e.g., one specific book)
2. **Collection resources** point to multiple items (e.g., all red books in a library)

## URI Structure and Specificity

REST APIs typically use **URI (Uniform Resource Identifier)** routes that allow you to narrow requests from broad collections to specific singletons. The more specific the path, the more focused the result. For instance, a path like `/bookcase` returns everything, while `/bookcase/books/red/four` returns only the red book in cubby four. This hierarchical structure makes APIs intuitive and predictable.

## Representations: Copies, Not Originals

A **representation** captures the current or intended state of a resource and is what gets transferred between the server and the client. Rather than accessing the actual underlying data, clients receive a representation, which is effectively a copy of the resource formatted for their needs.

This distinction has important practical implications. Unlike a physical library where you check out the actual book, a REST server generates a unique copy of the data for each request. This is why the same resource can serve multiple clients simultaneously, and why different clients can receive the data in different formats. The underlying data might be stored as XML, but the representation sent to one client could be JSON while another client receives HTML.

## Key Takeaway

The **resource** is the conceptual pointer to where data lives, while the **representation** is the actual data you receive when you access that resource. This separation is what makes REST flexible, scalable, and capable of serving diverse clients with varying format requirements.

---

*Based on the LinkedIn Learning course "Learning REST APIs" by Morten Rand-Hendriksen.*
