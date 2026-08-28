# REST API Clients

When discussing how [[REST APIs]] work, the term "clients" frequently appears. This summary explains what REST clients actually are, what it means to "consume" an API, and how access control works in practice.

## What is a REST Client?

A common misconception is that the **client** refers to the human user interacting with a website or application. In reality, the client is the website or application itself. Humans are merely the operators of these REST clients. The client consumes the REST API by creating and sending requests, then receiving and parsing responses.

## The REST API Does Not Care Who You Are

One of the fundamental characteristics of REST APIs is their indifference to the identity of the client, as long as that client follows the rules. The REST API's job is simply to receive requests, process data, and send responses. Where those requests originate and where the responses are delivered is relatively irrelevant to the API itself.

This means that if you have an open REST API, such as one for a WordPress site, anyone can access it. Once connected, they can discover how to access its methods and resources thanks to the REST constraints, particularly the self-describing nature of RESTful services. With that information, they can send valid requests to access the API's resources.

This accessibility is precisely the purpose of having a REST API. You provide an interface for your data to be literally consumed by whatever client comes knocking.

## Access Control and Rate Limiting

Not all REST APIs are completely open, and users cannot do whatever they want with the data. Most REST APIs impose strict limits on who can access what, which capabilities they are granted, and how many requests they can make within a set time period.

Social media platforms provide excellent examples of this. Twitter, for instance, has several open REST APIs. For an app to gain access, the operator of that client (the human being) must first authenticate themselves with a username and password. This ensures Twitter knows who is using the REST API and can monitor their behavior.

Once access is granted, strict **rate limits** are imposed to prevent clients from overusing the service. If you have used a third-party client for a social media platform, you may have encountered warnings like "API limit reached." This is the rate limiting mechanism at work on the backend.

## Key Takeaway

You, as a human, do not interact with the REST API directly. Communication with the REST API is handled by the client, which can be virtually anything: a website, a mobile application, or even an Internet of Things device. The REST API does not distinguish between them. It simply receives requests, processes data, and sends responses, all of which are consumed by the REST client on your behalf.

---

*Based on the LinkedIn Learning course "Learning REST APIs" by Morten Rand-Hendriksen.*
