# HTTP Status Codes

Every time you send a request to a web server using the **[[HTTP]] protocol**, the server responds with a message. This response always begins with an **HTTP status code** — a three-digit number that explains what happened on the server and how your request was processed. These codes allow browsers and applications to automatically identify whether a request succeeded or failed and determine what to do next.

## The Five Categories of Status Codes

HTTP status codes are organized into five main groups, each representing a different type of response. The first digit of the code indicates its category.

### 1xx — Informational

Status codes beginning with **1** are informational messages. They are rarely encountered in everyday browsing and are used to communicate the current state of the server during a request.

| Code | Meaning |
|------|---------|
| **100 Continue** | The server has received the request headers and is ready to receive the rest of the request body. This typically occurs when sending POST requests with large amounts of data. |
| **102 Processing** | The server is still processing the request and the client should wait. |

### 2xx — Success

Status codes beginning with **2** indicate that the request was successfully received, understood, and processed by the server.

| Code | Meaning |
|------|---------|
| **200 OK** | The request was successful and the server returned the requested data. |
| **201 Created** | The request was successful and a new resource was created on the server. |
| **204 No Content** | The server processed the request successfully but returned no content in the response. |

### 3xx — Redirection

Status codes beginning with **3** indicate that the client must take additional action to complete the request, usually by following a new URL provided by the server.

| Code | Meaning |
|------|---------|
| **301 Moved Permanently** | The resource has been permanently moved to a new URI. All future requests should use the new address. |
| **302 Found** | The resource is temporarily redirected to another URI. In practice, this code is often used similarly to 303. |
| **303 See Other** | The response to this request can be found at a different URI. |
| **307 Temporary Redirect** | The resource is temporarily available at a different URI, but future requests should still use the original address. |
| **308 Permanent Redirect** | The resource has permanently moved to a new URI, similar to 301. |

### 4xx — Client Errors

Status codes beginning with **4** indicate that something went wrong with the request sent by the client. These errors are typically caused by malformed requests, missing authentication, or attempting to access resources that do not exist.

| Code | Meaning |
|------|---------|
| **400 Bad Request** | The request is malformed, too large, or otherwise unprocessable by the server. |
| **401 Unauthorized** | The client lacks proper authentication credentials to access the resource. |
| **403 Forbidden** | The server refuses to fulfill the request, typically because the client is not logged in or does not have the necessary permissions. |
| **404 Not Found** | The requested resource does not exist at the specified address. |
| **405 Method Not Allowed** | The HTTP method used (such as POST) is not supported by the target resource. |

### 5xx — Server Errors

Status codes beginning with **5** indicate that the server encountered an error while attempting to process a valid request. These errors are not caused by the client.

| Code | Meaning |
|------|---------|
| **500 Internal Server Error** | Something went wrong on the server, but no specific details are provided. |
| **502 Bad Gateway** | The server, acting as a gateway or proxy, received an invalid response from an upstream server it was trying to reach. |
| **503 Service Unavailable** | The server is temporarily unable to handle the request, often due to overload or maintenance. |

## Summary

HTTP status codes provide a standardized way for servers to communicate the outcome of a request. Codes in the **1xx** range are informational, **2xx** indicates success, **3xx** signals redirection, **4xx** points to client-side errors, and **5xx** reveals server-side problems. Recognizing these codes is essential for web development, debugging, and understanding how browsers and servers interact.

---

*Based on the LinkedIn Learning course "HTTP Essential Training" by Morten Rand-Hendriksen.*