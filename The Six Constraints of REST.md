# The Six Constraints of REST

**Representational State Transfer**, or *[[REST APIs|REST]]*, refers to a group of software architecture design constraints that bring about efficient, reliable, and scalable systems. For a web-based API to be considered truly **RESTful**, it must meet six specific constraints. This summary explains each constraint and why it matters.

## Constraint 1: Client-Server Architecture

This constraint ensures proper **separation of concerns**. The client manages user interface concerns, while the server manages data storage concerns. This separation creates a highly portable system where one REST service can serve many different clients and interfaces without knowing or caring what those interfaces look like or what they are doing. In essence, there is a complete separation between the content and its presentation and interaction.

## Constraint 2: Statelessness

No client context or information, also known as **state**, can be stored on the server between requests. The client is responsible for keeping track of its own session state, and all requests sent from a client must be self-contained and complete.

If the client's session state is relevant, it must be sent along with the request. If the server needs to store that state, it must pass it on to a database or similar service for a specific time. For example, the server can be asked to pass on an authentication token for a set period to allow authenticated requests.

## Constraint 3: Cacheability

**Caching**, which means storing responses for a set period of time, is an integral part of web architecture and performance optimization. All REST responses must be clearly marked as cacheable or non-cacheable to ensure caching works as expected on the client end. This involves:

1. Caching responses that will not change or are unlikely to change
2. Caching rarely or periodically changed responses for reasonable periods of time
3. Blocking caching for constantly changing responses

## Constraint 4: Layered System

The system must be designed so the client cannot know and does not care whether it is connected directly to the server or to an intermediary like a mirror or a **CDN** (Content Delivery Network). This approach ensures scalability and also helps with security, as intermediary layers can provide additional protection without affecting how the client interacts with the API.

## Constraint 5: Code on Demand

Servers are allowed to transfer executable code to the client in the form of client-side JavaScript and compiled components. This extends and customizes functionality on the client side. This is a less common use of REST compared to the other constraints.

## Constraint 6: Uniform Interface

The final constraint breaks down into four sub-constraints that together define how clients and servers communicate consistently.

**Resource Identification in Requests** means that in REST systems on the web, a URI is used to send a request and that URI specifies what resource it is looking for. The key distinction is that the **resource** is the actual data sitting on the server, while what REST returns is a **representation** of that resource. This representation can have a different format from the server resource. For example, while the resource data may be stored as a table in MySQL, the returned representation may be JSON, XML, or even HTML.

**Resource Manipulation Through Representations** means that once a client has a representation of a resource, it can also modify or delete that resource. Given the right level of access, the client can control what is stored on the server.

**Self-Descriptive Messages** requires that each representation must describe its own data format. When you receive JSON, the response message will have its media type set to JSON. Without this information, the data cannot be reliably parsed. This applies to both sending and receiving REST data.

**Hypermedia as the Engine of Application State** (often abbreviated as **HATEOAS**) means that once the client has access to a REST resource, it should be able to discover all available resources and methods through the hyperlinks provided. When you request a page resource, the returned representation should include hyperlinks to all resources and methods available. The REST service essentially describes its own use with every returned resource.

## Conclusion

A web-based API can only be considered a truly RESTful API if it meets all six of these constraints. Together, they create a system that is portable, scalable, efficient, and self-describing, enabling reliable communication between diverse clients and servers across the web.

---

*Based on the LinkedIn Learning course "Learning REST APIs" by Morten Rand-Hendriksen.*
