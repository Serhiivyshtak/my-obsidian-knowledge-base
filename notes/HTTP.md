# HTTP

This summary explains **HTTP (Hypertext Transfer Protocol)**, the fundamental protocol that enables all communication on the World Wide Web. Whether you are browsing websites, submitting forms, or interacting with web applications, HTTP is working behind the scenes to make it happen.

## What is HTTP?

**HTTP** stands for *Hypertext Transfer Protocol*. To understand this term, we need to break it down into its components. A **protocol** is a system of rules that allows different entities, such as computers, to communicate and exchange information. **Hypertext** is a somewhat dated term for text displayed on a computer screen that contains links to other text, essentially what we now call web documents. Together, HTTP is the set of rules that servers and browsers use to transfer web documents back and forth across the internet. This is why every URL you type into a browser begins with `http` or `https`.

## Core Principles of HTTP

### Human Readable

One of the defining characteristics of HTTP is that it uses plain language that humans can understand. HTTP request methods use simple verbs like GET, POST, PUT, and DELETE. Even without technical knowledge, these terms convey their meaning clearly. When you see an HTTP request or response, you can read it and make sense of what is happening.

### Stateless but Not Sessionless

HTTP is a **stateless protocol**, meaning each request is completely independent and has no memory of previous requests. If you visit a photo gallery and see the first picture, then reload the page, HTTP treats this as an entirely new request and shows you the first picture again because it does not remember your previous interaction.

However, HTTP is not *sessionless*. To overcome the limitations of statelessness, HTTP supports **sessions** through mechanisms like **cookies**. When you navigate through a photo gallery, your browser and the server exchange cookies containing information about your position in the sequence. When you reload the page, the browser sends a cookie telling the server where you left off, allowing continuity despite the underlying stateless nature of the protocol.

### Extensible

HTTP is highly extensible through the use of **headers**. When requests and responses travel over HTTP, they can include additional information in headers. These headers can carry details about the client making the request, server configuration, timestamps, data format specifications, caching instructions, and the cookies used for session tracking. This extensibility allows HTTP to adapt to countless use cases beyond basic document retrieval.

### Request/Response Pairs

Every HTTP transaction follows a **request/response pattern**. The process begins with a client sending a request using one of the HTTP methods and concludes with the server returning a response. The response includes an HTTP status code indicating what happened, along with headers and any requested content.

## How HTTP Works: A Practical Analogy

Imagine the entire web as a library where each cubby on a shelf represents a website. A website can contain various resources such as documents, images, videos, stylesheets, and JavaScript files. When you want to access content from a website, you make a request to a librarian (representing the server). You say, in essence, "Can I get the content from cubby number four?" The librarian retrieves the relevant pieces that match your request and hands them back along with a response status indicating whether the request was successful.

## The HTTP Transaction Flow

An HTTP transaction follows a specific sequence of steps:

1. **Connection establishment**: The browser opens a TCP connection to the server. TCP ensures that data can travel reliably across the network and arrive intact. When using HTTPS (the secure version), TLS certificates are exchanged so that only the browser and server can encrypt and decrypt the transmitted data, preventing eavesdropping.

2. **Request transmission**: The browser sends an HTTP message containing the HTTP method (such as GET or POST), the URL of the requested resource, and optionally headers (like cookies or authentication data) and a data payload if submitting information to the server.

3. **Server processing and response**: The server performs the requested action and sends back a response. This response includes an HTTP status message, headers with metadata about the response, and the requested data (which could be an HTML document, stylesheet, JavaScript file, image, or other content type).

4. **Connection closure**: Once the response is fully received, the TCP connection closes. Because HTTP is stateless, the slate is wiped clean and any subsequent request starts fresh.

## HTTP/2 and Performance Improvements

The newer **HTTP/2** protocol introduces significant performance enhancements. It supports **multiplexing**, which allows multiple transactions to occur simultaneously over a single TCP connection rather than requiring separate connections for each resource. HTTP/2 also enables **server push**, where the server can proactively send resources that it knows the browser will need. For example, when a browser requests an HTML document, the server can push the associated CSS and JavaScript files at the same time without waiting for additional requests. These features substantially reduce page load times and improve overall web performance.

## Key Takeaway

HTTP is the invisible foundation that makes the web function seamlessly. Its human-readable design, stateless architecture with session support, extensibility through headers, and consistent request/response pattern provide a robust framework for all web communication. Understanding HTTP gives you insight into how every interaction on the web actually works, from clicking a link to submitting a form to loading complex web applications.

---

*Based on the LinkedIn Learning course "HTTP Essential Training" by Morten Rand-Hendriksen.*
