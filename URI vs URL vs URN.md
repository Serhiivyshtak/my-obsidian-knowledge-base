# URI vs URL vs URN

When working with web development and [[REST APIs]], you will frequently encounter the acronyms URI, [[URLs|URL]], and URN. These terms are related but have distinct meanings. This summary clarifies the differences and explains how they connect to one another.

## What is a URI?

A **URI**, or *Universal Resource Identifier*, is officially described as a compact sequence of characters that identifies an abstract or physical resource. It provides a simple and extensible means for identifying a resource. The URI is the most generic method for naming and locating a web resource. Any sequence of characters that identifies a resource is considered a URI.

## What is a URL?

A **URL**, or *Universal Resource Locator*, is a subset of the URI. The URL not only identifies a resource but also explains how to access that resource by providing an explicit method such as **HTTP** or **FTP**. In other words, all URLs are URIs, but not all URIs are URLs. The URL tells you both what something is and where to find it.

## What is a URN?

A **URN**, or *Universal Resource Name*, is another subset of URIs that is less commonly discussed. The URN refers to both URIs under the URN scheme and to any other URI with the properties of a name.

The classic way to understand the difference between a URN and a URL is through a person analogy. A URN is like a unique name identifier. There are many people named Morten, but only one person named Morten Rand-Hendriksen. Refer to someone by their full name and anyone who knows them understands who you mean, even if that person is not present and their current location is unknown. The URL, by contrast, provides an actual physical location, such as a specific country, state, city, and street address.

On the web, a URN can take several forms:

1. An explicit URN using the URN scheme, such as `oasis:names:specification:docbook`
2. A resource name like `linkedin.com/learning/instructors/morten-rand-hendriksen`
3. A URL, though this is not required

## How They All Relate

The relationship between these identifiers can be summarized as follows: a URL might also be a URN, and both URLs and URNs are types of URIs. The URI is the umbrella term that encompasses all methods of identifying web resources.

## Why This Matters for REST APIs

When working with REST APIs, developers typically use the generic term **URI** to refer to how resources are accessed. This is because within code, you might use URLs, URNs, or a combination of both. Using the term URI covers all possibilities and remains accurate regardless of which specific identifier type is employed in a given situation.

---

*Based on the LinkedIn Learning course "Learning REST APIs" by Morten Rand-Hendriksen.*