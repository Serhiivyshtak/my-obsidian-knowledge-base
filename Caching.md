# Caching

## What is Caching?

Caching is a technique used to improve website performance by storing copies of files locally so they do not need to be downloaded repeatedly. When a browser or server *caches* a file, it saves that file for later use. On subsequent visits, the stored version is used instead of fetching a fresh copy from the server. This dramatically speeds up page load times and reduces bandwidth consumption.

## Types of Website Content and Caching Needs

Not all website content changes at the same rate, which affects how caching should be applied:

- **Rarely updated content** such as JavaScript and CSS files can be cached for long periods.
- **Occasionally updated content** like standard web pages may need shorter cache durations.
- **Frequently updated content** such as front pages or news sections should either not be cached or have very short cache lifetimes.

## How Caching Works in HTTP

Both servers and clients (browsers) can instruct each other to cache files through [[HTTP]]. This communication happens via the **Cache-Control header**, which contains specific instructions called *directives*. These directives tell the browser how long to store files and under what conditions cached files can be replaced.

Common Cache-Control directives include **max-age**, **no-cache**, **no-store**, **public**, and **private**.

## The max-age Directive

The most commonly used directive is **max-age**, which specifies how long a file should be stored before the browser considers it expired. For example, setting `Cache-Control: max-age=31536000` tells the browser to store the file for one year (31,536,000 seconds) without checking with the server for updates.

During this period, the browser will use the cached version instead of downloading a new one. The file remains in cache until it expires or the user manually clears the browser cache.

## The Caching Problem

While aggressive caching improves performance, it introduces a challenge: once a file is cached, the server cannot force the browser to download an updated version until the cache expires. This is why developers sometimes cannot see their latest CSS or JavaScript changes reflected in the browser, even after refreshing the page or restarting the browser.

There are several strategies to address this issue:

1. Use the **no-cache** directive, which tells the browser to check with the server for a newer version before using the cached file.
2. Explicitly instruct the browser not to cache certain files at all.
3. Reduce the **max-age** value to a shorter duration, such as one day or 30 days.
4. Implement a technique called **cache busting**, where each version of a file has a unique filename. When a file is updated, it is uploaded with a new name, ensuring the browser treats it as an entirely new resource and downloads it fresh.

---

*Based on the LinkedIn Learning course "HTTP Essential Training" by Morten Rand-Hendriksen.*