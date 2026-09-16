# HTTP Methods

When your browser or application communicates with a web server via [[HTTP]], every request includes an **HTTP method** (also called a **verb**). This method tells the server what kind of action you want to perform. While there are several methods available, most standard web interactions rely on just a few of them. Understanding these methods is fundamental to grasping how data flows between clients and servers on the internet.

## Content Methods

These methods are used to retrieve, create, modify, or delete resources on a server.

### GET

The **GET** method is by far the most frequently used HTTP method. It requests data from a server without making any changes. When you load a webpage, your browser sends a GET request to retrieve that page.

A basic GET request only needs the method and a URL. However, if the resource is protected, the request may also require an **authorization header** (containing encrypted credentials) or a **cookie** with an authentication token.

**Response statuses for GET requests:**

| Status Code | Meaning |
|-------------|---------|
| **200 OK** | The request succeeded and the data is returned |
| **404 Not Found** | The resource does not exist at the specified address |
| **403 Forbidden** | The resource is blocked by the server |
| **405 Not Allowed** | The user lacks proper authorization |

### POST

The **POST** method sends data from the client to the server to create a new resource. This is the method used when you submit a form on a website. The server assigns an ID to the newly created resource for future retrieval. Because POST modifies server data, it typically requires an authorization header.

**Response statuses for POST requests:**

| Status Code | Meaning |
|-------------|---------|
| **201 Created** | The resource was successfully created; a link to the new resource ID is returned |
| **409 Conflict** | The resource already exists |
| **404 Not Found** | The target location cannot create new resources |

### PUT

The **PUT** method updates an existing resource by replacing some or all of its content. Unlike POST, a PUT request must include both the resource ID and the new content. If the resource exists, its content is replaced. If it does not exist, some servers may create a new resource with the specified ID, while others will return an error.

**Response statuses for PUT requests:**

| Status Code | Meaning |
|-------------|---------|
| **200 OK** | The resource was successfully updated |
| **204 No Content** | The request succeeded but there is no content on the server |
| **404 Not Found** | No resource matches the provided ID |
| **405 Method Not Allowed** | The target resource cannot be updated |

### PATCH

The **PATCH** method modifies an existing resource without fully replacing it. While PUT replaces content entirely, PATCH can carry instructions on how to alter specific parts of the resource. It also requires an authorization header and returns the same status codes as PUT.

### DELETE

The **DELETE** method removes a specified resource from the server. It requires both the resource ID and an authorization header. What happens on the server varies by implementation — some systems permanently remove the data, while others simply change the resource's status without deleting the actual content.

If you attempt to delete a resource you are not authorized to remove, the server returns a **405 Method Not Allowed** status.

## Informational Methods

These methods retrieve metadata or diagnostic information from the server without affecting the actual content.

| Method | Purpose |
|--------|---------|
| **HEAD** | Returns only the header section of the response, without the body content |
| **OPTIONS** | Returns a description of the communication options available for the target resource |
| **TRACE** | Creates a loop-back of the request message, showing where the request ended up |

## Summary

HTTP methods define the intent behind every request sent to a server. **GET** retrieves data, **POST** creates new resources, **PUT** and **PATCH** update existing resources, and **DELETE** removes them. Understanding these methods and their associated response codes is essential for web development, API design, and troubleshooting network issues.

---

*Based on the LinkedIn Learning course "HTTP Essential Training" by Morten Rand-Hendriksen.*