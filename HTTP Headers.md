# HTTP Headers

The **[[HTTP]] protocol** is stateless, meaning it does not store any information between requests. Each request and response is independent — the server does not remember previous interactions with a client. To overcome this limitation, both clients and servers use **HTTP headers** to pass essential information back and forth with every request and response.

An **HTTP header** is a human-readable name-value pair, separated by a colon, that is attached to an HTTP request or response. Headers can carry standard or custom information, and a single request or response can include as many headers as needed, each separated by a line break.

## Common Uses of HTTP Headers

### Authentication

When a client needs to perform an action that requires permission — such as creating a new resource on a content management system — it must first prove its identity. This is done by including an **authentication header** in the request. In its most basic form, this header contains a username and password combination. To ensure the credentials are transmitted safely and not misinterpreted as plain text, they are typically **Base64 encoded** before being sent.

### Cookies

When a server needs the client to remember certain information — such as which video the user is currently watching or whether the user is logged in — it sends a **Set-Cookie header**. This header delivers a **cookie**, which is a small piece of data stored by the client's browser.

On subsequent visits, the client automatically sends the cookie back to the server, allowing the server to restore the user's previous state. Cookies are the reason websites remember your login status and browsing preferences even after you close your browser. Many websites display cookie consent notices to inform users that cookies are being used to track their activity.

You can view and manage cookies through your browser's developer tools under application settings. Clearing your browser data removes all stored cookies, which will log you out of websites and reset any saved preferences.

### Caching

To improve performance, servers can instruct browsers to **cache** (save) certain files for a specified period of time. This is accomplished through **cache headers**. Caching reduces the amount of data transferred between the client and server on repeat visits, resulting in faster page loads.

However, when files are cached, the browser will not download updated versions until the cached files either expire or are manually cleared. Cache headers control what files to save, whether they should be updated, and how long they should be retained.

### Client and Server Information

Headers are also used to share metadata about the request or response. Common examples include:

- **Date and time information** about when the request or response was generated
- **User-Agent header** identifying the client application (such as the browser name and version)
- **Server header** identifying the software running on the server
- **Proxy information** for requests routed through intermediary servers
- **Security information** and **cross-origin resource sharing (CORS)** policies

With modern protocols like **HTTP/2**, new headers have emerged, including the **Link header**, which enables **server push** — a technique that allows servers to send files to the client before they are explicitly requested.

## The Request Header

The **request header** is the message a client sends to a server when requesting an action on a specific resource. When you type a URL into your browser, the browser constructs and sends a request header to the server.

A typical request header includes:

| Component | Purpose |
|-----------|---------|
| **Method and URL** | Specifies the HTTP method (such as GET or POST) and the address of the requested resource |
| **User-Agent** | Identifies the client application and browser being used |
| **Accept headers** | Lists the file types, languages, and encoding formats the client can process |
| **Referer** | Indicates the previous page the client came from |
| **Connection** | Specifies whether the connection should remain open for future requests |
| **Cache-Control** | Defines caching behavior for the requested resource |

The User-Agent header is also how some browsers disguise themselves as other browsers to bypass scripts that block or modify content based on browser type.

In addition to headers, an HTTP request can include a **payload** — additional data such as form submissions or uploaded files.

## The Response Header

When a server receives a valid request, it returns a **response header** along with any requested data. Even if the request fails, the server still sends a response (such as a 404 Not Found status).

A typical response header includes:

| Component | Purpose |
|-----------|---------|
| **Status code** | Indicates the result of the request (such as 200 OK) |
| **Server** | Identifies the server software handling the request |
| **Date** | Provides the date and time the response was generated |
| **Content-Type** | Specifies the format of the returned data (such as HTML, JSON, or an image) |

Following the response header comes the **payload** — the actual content being returned, such as an HTML document, an image, or data in JSON format. The client processes the payload according to the instructions provided in the response headers.

## Summary

HTTP headers are essential for enabling meaningful communication between clients and servers in a stateless protocol. They carry authentication credentials, manage cookies and caching, provide metadata about requests and responses, and ensure that both parties understand how to process the data being exchanged. Understanding headers is fundamental to web development, API integration, and troubleshooting network issues.

---

*Based on the LinkedIn Learning course "HTTP Essential Training" by Morten Rand-Hendriksen.*