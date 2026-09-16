# REST APIs and AI

[[REST APIs]] were traditionally a topic of interest mainly for front-end and back-end web developers who built applications interacting with data sources. The introduction of generative AI has dramatically changed this landscape, widening and deepening the scope of people interested in learning about REST APIs.

## REST as the Universal AI Protocol

Every major AI provider uses REST as their API protocol. Their API endpoints and properties are rapidly standardizing, making it easy for users to switch between AI models and providers without rewriting their entire codebase. While detailed accounts of the internal decision processes at AI companies are not publicly available, several factors make REST a natural fit for AI services.

## Why REST Works for AI

### Handling Nondeterministic Responses

The **nondeterministic nature of AI** is a primary reason for choosing REST. When you make a request to a full-featured AI API, the response may include a wide variety of properties such as completions, images, tool calls, streaming data, and more. REST's default behavior of returning all available data is exactly what developers need. This allows them to build custom software that sorts through responses and handles the unpredictability of AI outputs in a clean, controlled way.

### Streaming with Server-Sent Events

The broad feature set of REST accommodates another crucial AI requirement: streaming responses. In a library analogy, an AI API would be like a writer sitting in the library typing out custom text based on your requests. This process takes far more time than simply retrieving existing data, and users rarely have the patience to stare at a blank page while waiting for text to be fully generated.

The solution is **Server-Sent Events (SSE)**, a REST-compatible streaming mechanism that every major AI service provider has adopted. Using the standard `text/event-stream` content type, AI APIs stream responses word by word, creating the typing effect that became familiar with the introduction of ChatGPT.

### Simplified Authentication

Authentication for AI APIs typically requires only a standard **bearer key** passed in the Authorization header. This contrasts sharply with the industry standard of complex multi-step OAuth flows. The simplified approach removes virtually all friction when experimenting with AI services, though it introduces security complexities in production environments since passing keys in request headers is not inherently secure. The tradeoff clearly favored developer simplicity over production security, and the industry is already beginning to shift toward more secure, though more cumbersome, authorization approaches.

### Statelessness Aligns with AI Architecture

The most important factor is likely how well REST's **stateless nature** aligns with how AI services operate. Many AI models have no session or state when accessed through an API, so each request must include the complete context needed to generate a response.

This means the same REST API endpoint can be used to send unique one-off requests or to mimic statefulness by passing in the entire conversation history with each new prompt, all without actually managing state on the server. While this approach represents a step backward from traditional stateful session management, it places control over behavior and user experience squarely in the hands of the developer. For a nondeterministic system, this is often the only practical solution.

## The Revival of REST

The principles that made REST the go-to protocol for traditional web applications have coincidentally made it the ideal solution for AI services:

1. Clear resource modeling
2. Stateless interactions
3. Standard HTTP semantics

For anyone building AI-powered applications, having a solid understanding of REST is now essential. In a very real sense, generative AI has resurrected REST and elevated it to an even higher position in the world of software development.

---

*Based on the LinkedIn Learning course "Learning REST APIs" by Morten Rand-Hendriksen.*
