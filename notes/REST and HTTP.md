# REST and HTTP

When working with [[REST APIs]], requests are most commonly sent through [[HTTP]]. However, this raises an important question: are REST and HTTP intrinsically linked? The answer is no, but understanding why they are so often paired together helps clarify what makes an API truly "RESTful."

## What is HTTP?

**HTTP**, short for *HyperText Transfer Protocol*, is the protocol your web browser uses to access hypertext documents on the World Wide Web. The web itself is just one of many services that live on the internet, alongside others like **SMTP** for email, various instant messaging services, video streaming, and more.

## REST is Protocol-Independent

As established in the six constraints, **REST** is a set of software architecture design constraints that produce a specific type of service. There is nothing in the definition of REST that stipulates the service must run on HTTP or the web. You could just as easily create a REST service running on FTP, SMTP, or some other protocol entirely.

REST and HTTP are not linked by definition. They are simply a convenient and widely adopted pairing because the web provides an accessible, standardized infrastructure that aligns well with REST principles.

## What Makes an API "RESTful"

The term **RESTful API** has a specific meaning. When a REST service runs on the web over HTTP to provide access to a web resource, it is called a RESTful API. The web platform is what makes it RESTful.

In other words, if you send a request through HTTP to a REST service that meets all six constraints (client-server architecture, statelessness, cacheability, layered system, code on demand, and uniform interface), that service qualifies as a RESTful API. The combination of REST's architectural principles with the HTTP protocol and web infrastructure creates the RESTful APIs that power most modern web and mobile applications.

---

*Based on the LinkedIn Learning course "Learning REST APIs" by Morten Rand-Hendriksen.*
