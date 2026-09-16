# REST API Questions

### What happens if I don't specify the Content-Type header inside of my REST request? Which Content-Type will be used by default?

If you don't specify the Content-Type header inside of your REST request, the behavior of the client and of the server depends on the context in which this request was made.

If you send a simple GET request to retrieve or a **DELETE** request to delete a resource, there is no need for Content-Type header. Request will be executed without any issue. If you send a **POST**, **PUT** or PATCH request without specifing type of the content, most clients will set a default value as text/plain, text/plain;charset=UTF-8 or application/x-www-form-urlencoded. Axios and fetch() function in JavaScript often auto-set this header to `application/json` if a JavaScript object is passed. And finally, if you send a request using cURL, it won't set any header unless you specify it.

What is going to happen, if a server receives a request with no Content-Type header? Well, it depends on how the REST API is configured. It can either try to parse data based on the body provided, or return a 415 Unsupported Media Type error. Best practice is to always set Content-Type header to avoid unexpected results.

### There are a few ways of sending data to the server: request body, request headers and query parameters. What are the differences and the use cases for each of these approaches?

The main differences between these three approaches lie in how the data is sent to the server and which types of data can be sent.

Query parameters are appended to the URL, which means that the data can be seen in the browser history, Referer header when visiting external sites, shared URLs, screenshots, etc. Therefore, they are only used for non-sensitive data like filtering, pagination, sorting, preferred language, and so on. Additionally, there is a data length limitation, since URLs can maximally be around 2000 characters long. Values can only be strings.

Request headers are more secure than query parameters since they are not exposed in browser history, logs, or the Referer header. Usually, they are used to send metadata like caching settings, content type, user agent, timestamps, etc. Beyond that, request headers can be used to send authorization tokens to the server. However, they are still very limited in terms of data length and types since their form is simple key-value pairs.

The request body is the most versatile way of sending data and it supports a huge variety of content types like JSON, XML, images, PDFs, etc. It's typically used to create new resources via POST requests or to update existing ones via PUT or PATCH.

### How to protect Cookies from being stolen?

### What does SOAP stand for?

### What are the microframeworks?

### How to use ETags for checking wether a resource was changed on the server?

### What is Server-Sent Event (SSE)?