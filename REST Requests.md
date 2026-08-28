# REST Requests

This summary explains how REST requests work, including their structure, the different [[HTTP Methods|HTTP methods]] used, and how to interact with [[REST APIs]]. These concepts apply universally to all REST APIs, regardless of the platform or technology behind them.

## Anatomy of a REST Request

At its most basic level, a REST request consists of two essential parts: a **method** and a **URI**. The *method* is one of the standard HTTP operators that tells the server what action to perform. The *URI (Uniform Resource Identifier)* points to the specific resource you want to interact with.

For example, to retrieve a list of recent posts from a WordPress site, you would send a GET request to the posts resource URI: `GET site.com/wp-json/wp/v2/posts`. Whether a particular method works on a given resource depends on how the REST API is configured and what permissions the current user has.

## Request Headers and Metadata

When submitting a request, you can include **metadata** in the request header. This metadata should include the *content type* to comply with REST's self-descriptive messages constraint. Headers can also contain information such as user agent strings, accepted language preferences, authentication credentials, and cache control directives.

When sending data to create or update a resource, the request becomes more complex because you must include the actual data. The data structure must match the content type declared in the header. For instance, if the content type is set to `application/json`, the data payload must be formatted as JSON.

## HTTP Methods (Verbs)

**HTTP methods**, also called *verbs*, are instructions that tell the server what action to perform on a resource. Every time you use a web browser, it sends HTTP methods behind the scenes. The same principles apply to REST APIs.

### GET

The **GET** method retrieves data from a resource. It is by far the most common HTTP method. Whenever you visit a webpage, click a link, or reload a page, your browser sends a GET request. In REST APIs, GET returns the requested data along with a *200 OK* status, or a *404 Not Found* status if the resource does not exist.

### POST

The **POST** method creates new resources. It is commonly used when submitting forms on websites and when adding new entries to a REST API. When you POST data to a collection resource (such as a list of products), the API creates a new subordinate resource with its own unique ID and URI.

POST requests return different status codes depending on the outcome:

- *201 Created* on success, along with a link to the new resource
- *401 Unauthorized* if you lack permission
- *409 Conflict* if the resource already exists
- *404 Not Found* if the target resource does not exist

### PUT

The **PUT** method updates an existing resource by replacing all of its contents with the new data provided. Unlike POST, a PUT request must include the ID of the resource being updated along with the complete new content. If the resource exists, its content is fully replaced. Some REST servers may allow PUT to create a new resource if the specified ID does not exist.

PUT returns *200 OK* on success, *204 No Content* if no content is present, *404 Not Found* if the ID does not exist, or *405 Method Not Allowed* if sent to a collection resource (since PUT is designed for singleton resources).

### PATCH

The **PATCH** method modifies an existing resource without necessarily replacing everything. While PUT replaces the entire content, PATCH can carry specific instructions on how to update only certain parts of the resource. It returns the same status codes as PUT.

### DELETE

The **DELETE** method removes a specified resource. It can only be used with singleton resources. Attempting to delete a collection resource returns a *405 Method Not Allowed* status, as deleting everything at once is not permitted.

### OPTIONS and HEAD

Two additional methods are occasionally useful. **OPTIONS** returns a description of the available communication options for a target resource, helping clients understand what methods and capabilities are supported. **HEAD** returns only the header section of a response without the body content, which is useful for checking metadata without downloading the full resource.

## Practical Implementation

In real-world applications, REST requests are typically handled through scripts rather than typed manually. JavaScript is the most common language for this purpose. The fetch API or libraries like jQuery AJAX handle the construction of requests, automatic inclusion of certain headers, and processing of responses, making it much easier to work with REST APIs programmatically. 

For example, here is the GET request made in plain JavaScript using XMLHttpRequest class:

```js
let xhr = new XMLHttpRequest();

xhr.open('GET', 'https://site.com/wp-json/wp/v2/posts');

xhr.onload = function() {
  console.log(xhr.responseText); // Prints received data into the console
};

xhr.send();
```

Another example showcasing POST request with a request body using jQuery AJAX:

```js
$.ajax({
  url: 'https://site.com/wp-json/wp/v2/posts',
  method: 'POST',
  data: JSON.stringify({ title: 'New Post', content: 'Post content' }), // Request body
  contentType: 'application/json',
  beforeSend: function(xhr) {
    xhr.setRequestHeader('Authorization', 'Bearer YOUR_AUTH_TOKEN');
  },
  success: function(response) {
    console.log(response);
  }
});
```

---

*Based on the LinkedIn Learning course "Learning REST APIs" by Morten Rand-Hendriksen.*
