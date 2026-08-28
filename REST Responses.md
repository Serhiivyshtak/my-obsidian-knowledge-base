# REST Responses

This summary explains how [[REST APIs]] communicate back to clients after receiving requests. Understanding response headers, HTTP status codes, and authorization levels is essential for working effectively with any REST API.

## The Structure of a REST Response

Every REST API response consists of two parts: a **head section** and the content provided by the resource. The head section contains metadata about the response and is typically processed by the client application rather than displayed to users. While every response includes a head section, its contents vary depending on the HTTP method used and the type of resource requested.

A typical response header begins with the protocol used (such as HTTP 1.1) followed by the **HTTP status message** (for example, *200 OK*). Below this, you find metadata including the date and time of delivery, content type, server information, transfer encoding, connection details, and caching data. This information tells the client how to handle the incoming data. For instance, if the *content type* is defined as `application/json`, the client knows to parse the data as JSON. If the header specifies `content-encoding: gzip`, the client must decompress the content before processing it.

To retrieve only the head section without the response body, you can send a **HEAD request** to any resource. This is useful for checking resource metadata without downloading the full content.

## HTTP Response Status Codes

The **HTTP response status code** appears at the top of the response header and immediately tells the client whether the request succeeded or failed. Clients use these codes to identify outcomes and automatically determine next steps. Status codes are organized into five main categories.

### 100 Series: Informational

These codes inform the client about the server's status, typically indicating that processing is ongoing or that the connection is ready. They are rarely encountered in everyday REST API usage.

### 200 Series: Success

Success codes confirm that the request was processed correctly:

- *200 OK* indicates the request was successful
- *201 Created* confirms a new resource was successfully created
- *204 No Content* means the server processed the request but returned no content

### 300 Series: Redirection

Redirection codes tell the client to look elsewhere for the resource. This category includes *301 Moved Permanently* (use the new URI for all future requests), *302 Found* (resource temporarily redirected), *303 See Other* (the response is at a different URI), *307 Temporary Redirect*, and *308 Permanent Redirect*. The 300 series can be confusing because several codes have overlapping meanings, so careful attention is required when handling or generating redirect responses.

### 400 Series: Client Errors

Client error codes indicate problems with the request itself:

- *400 Bad Request* means the request is malformed or otherwise invalid
- *401 Unauthorized* indicates missing or invalid authentication credentials
- *403 Forbidden* means the server refuses the request, typically due to insufficient permissions
- *404 Not Found* indicates the requested resource does not exist
- *405 Method Not Allowed* occurs when using an HTTP method that the resource does not support

### 500 Series: Server Errors

Server error codes indicate problems on the server side:

- *500 Internal Server Error* means something went wrong on the server
- *502 Bad Gateway* indicates the server, acting as a gateway or proxy, received an invalid response from an upstream server
- *503 Service Unavailable* occurs when the server is overloaded or temporarily down

## Authorization and Access Levels

Most REST APIs implement **leveled access**, meaning different users have different permissions based on their authorization status. Unauthenticated users typically can only submit GET, HEAD, and OPTIONS requests. Authenticated users with elevated privileges may also submit POST requests, while users with full administrative access can use PUT, PATCH, and DELETE methods.

The response headers reflect these permission levels. When sending an unauthenticated HEAD request, the *Allow* header might show only `GET`. When the same request includes valid authentication credentials, the Allow header might expand to include `GET, POST, PUT, PATCH, DELETE`, granting full control over the resource.

Authentication methods vary in complexity and security. **Basic authentication** transmits credentials in plain text and is only suitable for local development or testing environments. Production REST APIs typically use more robust protocols such as **JSON Web Tokens (JWT)** or **OAuth 2.0**, which provide encryption and multiple levels of authorization to protect sensitive data.

## Key Takeaway

REST API responses provide structured information that enables clients to understand what happened with their request and how to proceed. The status code offers immediate feedback on success or failure, the headers contain metadata for parsing and handling the response, and authorization levels determine what actions each user can perform. Understanding these elements is fundamental to building applications that interact reliably with REST APIs.

---

*Based on the LinkedIn Learning course "Learning REST APIs" by Morten Rand-Hendriksen.*
