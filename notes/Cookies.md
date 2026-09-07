# Cookies

The **[[HTTP]] protocol** is stateless, meaning it does not retain any information between requests. However, many web applications require the ability to remember users — for example, to keep them logged in or to track where they left off. **Cookies** solve this problem by allowing servers and clients to pass state information back and forth, effectively creating **sessions** between them.

## What Are Cookies?

A **cookie** is a small piece of data that a server sends to a client's browser. The browser stores this data and automatically includes it in future requests to the same server. Cookies typically contain a unique **token** — a string of characters that identifies the user or their session.

## How Cookie Authentication Works

Consider a website with a login panel. When a user visits the site for the first time, they are presented with a login form. After entering their username and password, the server verifies the credentials and grants access.

At this point, the server performs two actions:

1. It generates a unique token and stores it in its own database, associating it with the logged-in user.
2. It includes a **Set-Cookie response header** in its response to the browser, containing that same unique token.

The browser receives the cookie and stores it in memory. From this point forward, every time the user sends a request to the server — whether viewing a new page, leaving a comment, or performing any other action — the browser automatically includes a **Cookie header** in the request, sending the stored token back to the server.

When the server receives the request, it extracts the token from the cookie, checks it against its database, and if the token matches a valid session, processes the request and returns the appropriate data. This mechanism allows the user to remain authenticated without having to log in repeatedly.

## Viewing Cookies in the Browser

You can inspect the cookies stored by any website using your browser's **developer tools**. Under the **Network** tab, selecting a request will reveal a **Cookies** tab alongside the headers. This displays all cookies the website has stored in your browser, including those used for authentication and other purposes.

If you view the **raw headers** of a request, you will see the **Cookie header** containing all the tokens being sent back to the server.

## Common Uses of Cookies

Cookies serve a variety of purposes beyond authentication:

- **Session persistence** — Keeping users logged in across multiple visits
- **State restoration** — Returning users to where they left off, such as a specific page or video timestamp
- **Behavior tracking** — Recording user activity for analytics or personalization

## Privacy Concerns and Cookie Warnings

Because cookies can be used by advertisers to track users across multiple websites, privacy regulations have emerged to protect consumers. The **European Union** and various companies now require websites that use cookies to explicitly inform users about tracking practices.

This is why you encounter cookie consent banners on most websites today. These warnings exist to give users transparency and control over how their browsing behavior is monitored — and have nothing to do with actual baked goods.

## Summary

Cookies are a fundamental mechanism for maintaining state in the stateless HTTP protocol. They enable features like persistent logins and personalized experiences by allowing servers to store small pieces of identifying information in the user's browser. Understanding how cookies work is essential for web developers, security professionals, and anyone who wants to understand how modern websites remember who you are.

---

*Based on the LinkedIn Learning course "HTTP Essential Training" by Morten Rand-Hendriksen.*