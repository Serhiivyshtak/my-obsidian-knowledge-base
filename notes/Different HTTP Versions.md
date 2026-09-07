# Different HTTP Versions

This summary explains the differences between **HTTP/2** and **HTTP/1.1**, as well as the role of **HTTPS** in modern web communication. Like all web technologies, [[HTTP]] continues to evolve, with newer versions introducing improvements in speed, security, and functionality.

## HTTP/2: The Current Standard

**HTTP/2** is the second major version of the HTTP protocol and represents a significant advancement over its predecessor. As of now, HTTP/2 powers between 70 and 80 percent of all transactions on the web, making it the dominant protocol for modern web communication.

The key improvements in HTTP/2 include enhanced speed and stronger security. The protocol uses *compression algorithms* to reduce the size of data being transmitted, which speeds up requests considerably. HTTP/2 also supports **multiplexing**, a feature that allows multiple files to be sent over a single connection simultaneously rather than one at a time. Additionally, HTTP/2 requires an encrypted connection between the client and server through **HTTPS**, ensuring that data transmitted between parties cannot be intercepted or read by third parties.

## HTTP/1.1: The Legacy Protocol

**HTTP/1.1** is the older version of the protocol that preceded HTTP/2. While it has largely been superseded, HTTP/1.1 remains very much alive on the web. It serves as the *fallback protocol* whenever HTTP/2 fails or is unavailable, which means you will still encounter HTTP/1.1 from time to time both now and in the future.

Compared to HTTP/2, HTTP/1.1 has several limitations. It sends *uncompressed headers*, which increases the amount of data transmitted. It can only transfer one file at a time over a connection, making page loads slower when multiple resources are needed. Furthermore, HTTP/1.1 has no default encryption, meaning data can potentially be transmitted in plain text without protection.

## HTTPS: Secure HTTP Communication

**HTTPS** (Hypertext Transfer Protocol Secure) is not a separate protocol version but rather HTTP with an added layer of encryption. When a connection uses HTTPS, the data exchanged between the client and server is encrypted, preventing eavesdropping and ensuring privacy. HTTP/2 requires HTTPS by default, which is one of the reasons it offers better security than HTTP/1.1.

## Real-World Implementation

In an ideal scenario, every HTTP transaction would occur over an encrypted HTTPS connection using the HTTP/2 protocol. In practice, most web transactions do follow this pattern. However, when HTTP/2 is unavailable or encounters issues, the connection falls back to unencrypted HTTP/1.1. While this fallback is slower and less secure, it ensures that web communication continues to function reliably across all environments and configurations.

## Key Takeaway

HTTP/2 represents the modern standard for web communication, offering faster performance through compression and multiplexing, along with mandatory encryption via HTTPS. HTTP/1.1 continues to serve as a reliable fallback when needed. Understanding the distinction between these versions helps explain why some web experiences are faster and more secure than others, and why encryption through HTTPS has become essential for contemporary web applications.

---

*Based on the LinkedIn Learning course "HTTP Essential Training" by Morten Rand-Hendriksen.*
