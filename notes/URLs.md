# URLs

## Overview

This document explains the structure and function of **URLs** (Universal Resource Locators), which are the addresses used to locate and access information on the internet. Every time you type a web address into your browser or click a link, you are using a URL to tell the internet exactly where to find the content you want.

## What is a URL?

A **URL** is a human-readable address that describes precisely where a resource is located on the web and on which server it resides. Think of it as a postal address for the internet: just as a street address tells a mail carrier where to deliver a letter, a URL tells your browser where to find a specific webpage, image, or file.

## The Two Main Components of a URL

Every URL consists of two fundamental parts:

1. **Protocol Declaration** — Specifies how the resource will be accessed, using methods like HTTP or HTTPS and the underlying transport layer.
2. **URN (Universal Resource Name)** — Provides the actual location of the resource on the web.

## Breaking Down the URN

The URN itself contains several distinct elements that work together to pinpoint the exact location of the requested resource.

### The Host

The **host** is the domain name (such as `linkedin.com`) that is registered with a **DNS** (Domain Name Service). The DNS acts like a phone book for the internet, translating human-friendly domain names into numerical **IP addresses** that identify specific servers on the web.

### The Port

The **port** specifies which communication channel on the server should be accessed. Ports are usually invisible because standard defaults are assumed. For regular **HTTP** connections, the default port is **80**. For secure **HTTPS** connections, it is **443**. If a server uses a non-standard port, such as 8080, this must be explicitly declared in the URL using a colon (for example, `localhost:8080`).

### The Resource Path

The **resource path** indicates the specific file location within the server's directory structure. When you request a folder without specifying a filename, the server automatically searches for default files such as `index.html`, `default.html`, or `index.php` and returns them. If the file has a different name, such as `about.html` or `contact.php`, the full filename must be included in the path (for example, `mysite.com/folder/about.html`).

### The URL Query

The **URL query** is an optional component appended to the end of the resource path. It allows additional instructions or data to be sent to the server. Common uses include tracking user sessions, filtering content, or triggering specific server-side actions.

A query begins with a **question mark** (`?`), followed by one or more argument-value pairs in the format `argument=value`. Multiple queries can be combined using the **ampersand symbol** (`&`). For example: `?u=1234&filter=recent`.

## Summary of URL Structure

A complete URL can be visualized as follows:

https://example.com:443/folder/page.html?query=value


| Component       | Example               | Description                                                                 |
|-----------------|-----------------------|-----------------------------------------------------------------------------|
| **Protocol**    | `https://`            | Defines how the resource is accessed (HTTP or HTTPS)                        |
| **Host**        | `example.com`         | The domain name registered with a DNS, pointing to a server IP address      |
| **Port**        | `:443`                | The connection port on the server (443 for HTTPS, 80 for HTTP by default)   |
| **Resource Path** | `/folder/page.html` | The file location within the server's directory structure                   |
| **URL Query**   | `?query=value&filter=recent` | Optional parameters sent to the server, separated by `&`             |

Each part plays a specific role in directing your browser to the exact location of the requested resource on the web.

---

*Based on the LinkedIn Learning course "HTTP Essential Training" by Morten Rand-Hendriksen.*