# HTTP Terminology

This summary provides clear definitions of the most commonly used terms when discussing **[[HTTP]] (Hypertext Transfer Protocol)** and web communication. Understanding this vocabulary is essential for anyone working with web technologies or trying to comprehend how the internet functions.

## Browser

A **browser** is an application used to access and navigate between HTML documents. While the most familiar browsers are the visual applications on smartphones, tablets, and computers, browsers come in many varieties. These include text-to-speech audio browsers for accessibility, text-only browsers, and browsers designed for virtual reality (VR), augmented reality (AR), mixed reality (MR), and extended reality (XR) environments.

## User Agent

A **user agent** is an application that acts on behalf of the user, essentially serving as a literal agent for the user. It is also commonly called a *client application*. In the context of HTTP, the user agent is whatever application transports information from the user to a server and back. While this role typically falls to the browser, it is not limited to browsers. Middleware, services like search engines, or even other servers can function as user agents.

## TCP (Transmission Control Protocol)

**TCP** stands for *Transmission Control Protocol*. It is one of the main internet protocols used by the World Wide Web, email, FTP (File Transfer Protocol), and remote administration systems. When you connect to any service over the internet, you are most likely using a TCP connection to ensure reliable data transmission.

## IP (Internet Protocol)

**IP** stands for *Internet Protocol*, which is the protocol used to actually transfer data between computers over a network. Every computer connected to the internet has a dedicated **IP address** that serves as its unique identifier, allowing other computers to locate and connect to it.

## URL (Universal Resource Locator)

A **URLs|URL** is a *Universal Resource Locator*, a universally understood address that points to a resource somewhere on the web. URLs are human-readable addresses stored in **Domain Name Servers (DNS)** and configured to point to the IP addresses of web servers. When you type a web address into your browser, the address is automatically prefixed with either `http` or `https`, indicating that you are using the Hypertext Transfer Protocol to access the resource at that location.

## Server

A **server** is a computer on the internet running some form of data storage and sharing application. Most commonly, this is a web server application that allows users to access its data through the HTTP protocol. HTTP is fundamentally a *client-server protocol*, meaning clients (user agents, typically browsers) send requests to servers, and servers send responses back to clients.

## Proxy

A **proxy** is a service, either software or hardware, that acts as an intermediary between clients and servers. Proxies serve several purposes, including hiding the IP address of a server or enabling communication when a server or client sits behind a network barrier like a firewall. The proxy literally hands data back and forth between the two parties.

## Request and Response

Clients and servers communicate over HTTP using **request-response pairs**. Whenever a client talks to a server, it sends an **HTTP request**. This request contains a *request method* describing what action is requested, an address pointing to a resource, and other information about the client. If the client needs to send data to the server, that data is packaged in the request as a *payload*.

The **response** is the server's answer to the request. It contains a *status response code* explaining what happened, information about how the response was handled, and any requested data if the operation was successful.

## Headers

Both requests and responses use **HTTP headers** to identify themselves and communicate their intent. Every request and response has a header, and some also include payloads (the actual data being transferred). Headers contain metadata that facilitates communication between clients and servers.

The header of an HTTP request always contains a **request method** (also called a *verb*). These methods are descriptive words like GET (to retrieve something), PUT (to place or replace something), POST (to submit something), and DELETE (to remove something).

The header of an HTTP response always contains a **status response code**. These are numerical codes ranging from 100 to 599 that describe the outcome of the request. Common examples include *200 OK* (success), *404 Not Found* (resource does not exist), and *500 Server Error* (something went wrong on the server).

## Cache

Web servers and clients can **cache** data, meaning they store it for a specified length of time to improve transfer speeds and overall performance. For example, when you visit a website, your browser typically downloads the CSS stylesheet once and stores it in its cache. When you navigate to another page on the same site or return later, the browser uses the cached file instead of downloading it again. Websites and servers can instruct clients to cache files, clear cached files, or update specific cached files through instructions passed in a **cache header**.

## Stateless Protocol and Cookies

HTTP is a **stateless protocol**, which means there is no inherent link between two requests sent between a client and server. Each request is independent and the server has no memory of previous interactions.

When a stateful session is needed, HTTP uses **cookies**. Cookies are small pieces of information passed back and forth between the client and server in the HTTP header. They notify each party of the state the other is in. This mechanism is how you stay logged into a service after signing in. The server places a cookie in your browser's cache, and when you visit the site again, that cookie is sent back to the server, essentially saying "we have already met and you trust me, so let me in."

## Key Takeaway

Understanding HTTP terminology provides the foundation for comprehending how web communication works. From the browser that initiates requests to the servers that respond, from the protocols that ensure reliable data transfer to the cookies that maintain session state, each component plays a vital role in the seamless functioning of the World Wide Web.

---

*Based on the LinkedIn Learning course "HTTP Essential Training" by Morten Rand-Hendriksen.*
