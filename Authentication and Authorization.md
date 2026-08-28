# Authentication and Authorization

When designing [[REST APIs]], certain common patterns help tie together all the fundamental concepts like resources (nouns) and HTTP methods (verbs). Among the most critical of these patterns are **authentication** and **authorization**, often abbreviated as *authn* and *authz* respectively.

## The Difference Between Authentication and Authorization

Authentication and authorization are frequently confused, but they serve distinct purposes.

**Authentication** is the process of establishing who you are. This happens every time you log into a website with a username and password. When you access your banking website and enter your credentials, you are authenticating yourself, proving your identity to the system.

**Authorization** determines what you are allowed to do once your identity is established. After logging into your bank, the system only shows you your own accounts because those are the ones you are authorized to see. If you could see another person's bank account, that would constitute a serious security breach.

The same principles apply to APIs. Many APIs implement tiers of access based on various factors such as the user's role, group membership, whether they are a regular or admin user, their payment or subscription level, and other criteria.

## Approaches to Implementing Authentication and Authorization

### API Keys

An **API key** is a long string issued by the API provider that is either appended to the URL or included as a header in the request. This approach is by far the simplest and easiest to implement from any programming language, framework, or even command-line tools like curl.

However, there are two significant downsides to consider. First, if the key is included in the URL, it will be captured and logged by every cache, router, and device between the client and the API itself, which is not secure. Moving the key to the headers improves security, but a second problem remains: if the key is compromised, it cannot be rotated easily. Updating all applications that use the key may require redeployment across multiple environments.

### Custom Protocols

Building your own authentication protocol offers no real benefits. Hundreds and even thousands of developers have struggled with security implementations, failed, succeeded, failed again, and eventually developed solid solutions that work. If you build your own encryption or security scheme and it becomes compromised, the consequences can be severe for your career and organization.

Custom protocols also create training burdens. If you have a proprietary authentication scheme, every new team member, customer, and partner will encounter it for the first time and require training before they can do anything useful. Furthermore, you will not have access to existing tools, developer communities, or established libraries. All the resources that normally accelerate development simply do not exist for custom solutions. It is comparable to a mechanic who insists on building their own wrenches rather than using standard tools.

### OAuth

**OAuth** is the most common approach for API authentication and is actually an authorization protocol. It does not define how you authenticate, only that you must authenticate with a trusted entity. The access token returned from the authentication process describes or internally maps to a description of what actions you are and are not allowed to perform. This is where authorization comes into play.

**OAuth 2.0** is the recommended approach for modern APIs. While it is not always well understood, it is widely established and used by major APIs across the industry. A massive ecosystem of tools, libraries, documentation, and training resources exists around OAuth 2.0.

The tradeoffs are that OAuth is not always the easiest or fastest solution to implement. Building an OAuth implementation from scratch is not advisable. Numerous commercial and open-source solutions are available, and leveraging these existing implementations is strongly recommended over attempting to create one independently.

## Key Takeaways

Understanding the distinction between authentication (proving identity) and authorization (defining permissions) is fundamental to API security design. While API keys offer simplicity, they come with security limitations. Custom protocols should be avoided entirely due to the risks and overhead they introduce. OAuth 2.0 represents the industry standard, providing robust security through a well-established ecosystem, though it requires more initial setup than simpler approaches.

---

*Based on the LinkedIn Learning course "Designing RESTful APIs" by Keith Casey.*