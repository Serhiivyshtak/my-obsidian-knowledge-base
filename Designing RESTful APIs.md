# Designing RESTful APIs

[[REST APIs|REST API]] design is inherently challenging because it involves a continuous series of trade-offs. The process requires deliberate decision-making at every stage. First, you must decide what functionality to expose. Then you determine how to expose it, followed by finding the best ways to do so. As real-world usage reveals flaws in your assumptions and use cases, you must adjust and improve. Finally, as you learn about your customers and their unexpected use cases, you may need to rethink fundamental aspects of your design.

API design touches on some of the hardest problems in computer science. It requires naming things well while simultaneously describing how to interact with those things. As the API encounters real-world usage, its goals and purpose will evolve, which introduces concerns around *versioning* and *backwards compatibility*.

## Understanding Affordances

An **affordance** is something that allows you to perform an action or accomplish a goal. A doorknob is an affordance that allows you to open a door. A light switch is an affordance for turning lights on and off. In API design, everything you allow a user to do is an affordance.

Three aspects come into play when considering affordances:

1. What the API allows you to do
2. What the API makes easy
3. What the user actually wants to accomplish

When these three elements do not align, you may end up with a useless API or a powerful API that fails to meet user needs. When all three are aligned, you achieve something incredibly powerful yet so intuitive that users barely notice the design.

Consider a coffee cup with a handle. The handle was designed so you can hold a hot cup without burning your hand. However, the handle also allows you to hang the cup on a hook. This represents a goal with a simple solution that enables additional use cases without requiring extra effort from the user.

## Strategies for Adding an API

There are three primary approaches for adding an API to a system.

### The Bolt-On Strategy

This approach involves adding an API to an existing application after the fact. It is often considered a brute-force method but represents the fastest way to gain value from an API since the underlying system remains functional throughout the process. This strategy takes advantage of existing code and systems, eliminating the need to rebuild foundational logic.

The drawback is that poor architectural decisions and unfortunate naming conventions made years ago tend to seep through the system and cause problems in external interfaces, helper libraries, and supporting client code. These oddities become permanent fixtures.

### The Greenfield Strategy

This approach applies when there is no underlying application or existing business logic to interact with. You have complete freedom and flexibility to design however you want. This is the strategy behind *API-first* or *mobile-first* approaches and represents the easiest scenario for developing an API.

Starting from scratch offers the opportunity to use technologies and concepts that may not have been available before, which can reinvigorate teams and expand their skills. However, this is also the hardest option because there is a significant gap between when requirements are defined and when the system delivers real business value.

### The Facade Strategy

This recommended approach sits between Greenfield and Bolt-On strategies. You take advantage of existing business systems while shaping them to meet your preferred structure and needs. Organizations commonly use this when wrapping legacy SOAP services with re-architected REST interfaces, allowing them to keep working systems in place while improving the underlying architecture.

The drawback is that without careful management, naming translation and conversion layers can easily get out of control. In some cases, completely divergent mindsets can develop within the system, making it appear inconsistent to those who can see both systems.

## Modeling Your API: Three Essential Rules

Regardless of which API strategy you follow, modeling is key to success. You must ensure that the capabilities, or *affordances*, make sense, are useful, and actually make users' lives easier.

**Do not worry about the tools.** Whether you use note cards, post-it notes, or the latest Kanban tool, choose whatever works best for your process. The specific tool matters far less than having a method for capturing and organizing your thoughts.

**Maintain a consistent process.** Documenting things the same way using the same steps reduces the likelihood of missed details, misunderstood ideas, or incomplete requirements. Involve a variety of team roles during modeling, including developers, support staff, documentation teams, and QA. Their diverse perspectives will surface questions and insights that your immediate team would not consider.

**It does not count unless it is written down.** During modeling, you will find gaps in your understanding and places where you need more information. If you do not document these, you risk losing them and potentially putting the entire project at risk. Document everything, including assumptions and tasks that can be addressed later. When team members ask why a structure was designed a certain way, documented assumptions and decisions provide shared understanding. If assumptions prove wrong, they can be corrected and adjusted much earlier in the process.

## The API Modeling Process

The API modeling process consists of five sequential steps that guide you from understanding business requirements to having a validated API design.

### Step 1: Identifying Participants

Before modeling the API itself, you need a clear understanding of your business process. Participants are the entities involved in the business process that will eventually use the API. Not all participants are humans; IoT devices, bots, and monitoring services may also participate. A participant is any entity that directly or indirectly takes action or receives actions as a result of an event.

For each participant, capture who they are by giving them a name (not just "a developer" but "Developer Dan" or "Developer Diane"). Determine whether they are internal or external to your organization. Finally, identify whether they are *active* (taking an action) or *passive* (waiting for an action).

Be careful about **boundaries**. If you are not cautious, you could end up modeling inventory management systems, coffee machine workflows, payment processors, and countless other systems that fall outside your scope. Define clear boundaries early. For a book ordering scenario, relevant participants might include the customer, the stock clerk who fulfills and ships orders, and customer support who handles problems.

### Step 2: Identifying Activities

Define the overarching business processes or goals involved. An activity represents the high-level objective that participants are trying to accomplish. In a coffee shop scenario, the overarching activity is ordering a cup of coffee. In an e-commerce context, the overarching activity might be ordering a book online.

At this stage, you can draw boundaries wherever you want, which is both advantageous and risky. What you want and assume might not match what your customer needs. This is not the time to guess. Go back to your end user or product manager to clarify requirements, and document the answers.

### Step 3: Breaking Activities into Steps

Once the overarching activity is defined, break it into concrete steps that clearly reference individual participants, describe what they are doing, and establish the order in which things occur along with their dependencies.

For a coffee ordering scenario, a complete breakdown would include: the patron creates an order with the cashier, the cashier passes the order to the barista, the barista acknowledges and queues the order, the cashier communicates the total, the patron provides payment which is either accepted or rejected, and finally the order is announced and delivered.

For ordering a book online, the steps might include: finding a book, adding it to a cart, checking out, providing payment, fulfilling the order, and shipping. Flag all branches, choices, and assumptions, then consult your product owner to determine priorities. Other teams may already be working on related issues with decisions already made. Do not guess; document everything and verify with stakeholders.

### Step 4: Creating API Definitions

This step requires identifying resources and mapping them to HTTP methods. **Resources** are anything someone wants to interact with in your system, essentially your *nouns*. If you have written your steps on note cards, circle the nouns to identify resources quickly.

In a book ordering scenario, the nouns include *items* (which users view and search), *carts* (collections of items), and *orders* (carts that have undergone the checkout process). Design decisions arise naturally during this process. For example, is a cart simply a collection of items, or does a separate line item resource hold each individual item?

Once nouns are identified, map them to HTTP verbs. **GET** retrieves data and should never modify information. **DELETE** removes data. **PUT** updates an existing record. **POST** serves as the catch-all for creating new records and any modification that does not directly map to other verbs.

Listing and searching are typically special cases of GET. Creating a new cart uses POST. Modifying a cart by adding items uses PUT. The checkout process uses POST since it does not map cleanly to other verbs. Viewing an order uses GET. Canceling an order uses POST to change status rather than DELETE, since the order is being updated to a canceled state rather than removed entirely.

### Step 5: Validating the API

Having a design and structure does not mean you have a finished API. The design must be tested before significant development effort is invested. There are several validation approaches.

If you have listed individual steps on note cards, examine other use cases and see if you can solve them by rearranging your cards. Everything should map together cleanly; if something does not fit, that is a red flag requiring you to revisit earlier steps.

You can write code as if your API already existed, stepping through each API call without worrying whether the code compiles. The goal is to determine if things make sense. Doing this on a whiteboard with colleagues helps find big issues and awkward structures early.

Using a **microframework** like hapi.js in Node or Slim in PHP allows you to accept incoming requests, validate corresponding verbs and URL patterns, and return static HTTP response codes and payloads. This approach lets you plug in real functionality as you build, watching everything come together incrementally.

Writing **documentation first** as if the API already existed is the most common validation approach. Describe endpoints, list parameters, include response codes, and show the fields returned. The goal is documentation that other teams can use to accomplish their goals with your API. Include curl commands or similar examples showing what calls look like.

## Critical Principles Throughout the Process

**Do not make things up.** Throughout this process, there will be things you do not know. That is not a problem and can be fixed quickly. The actual problem occurs when you invent answers instead of asking the product owner or customer. Something decided without input can accidentally become a hard requirement that the rest of your team treats as customer-dictated when it was actually an arbitrary choice.

**Document assumptions and decisions.** Flag all branches, choices, and assumptions, then consult your product owner as soon as possible to determine priorities. Other teams may already be working on related issues with decisions already made.

**The fastest error to fix is the one you do not create.** Early validation through any of these methods prevents costly corrections weeks or months into development.

---

*Based on the LinkedIn Learning course "Designing RESTful APIs" by Keith Casey.*
