# 3. Aggregation
Created Thursday 28 May 2020

Aggregarion - a weak(not strongly linked) form of composition.

* In composition, tag, head, body etc are useful only if Htmldoc exists.
* Focus on what we want to do, as anything's possible here - don't get lost.


**Compositon**: Owns(i.e creates all the components when it is created). Of the Composedclass is destroyed, all the components are also destroyed, by the garbage collector.
**Aggregation**: Does not own the componnets, uses existing components. This way, even if the aggregate class is destroyed, none of the components are affected. i.e the components are independent.

Both are HAS A relationship.
Note: If we were using Java/C++, we'd have to write the HTML Doc function again. But this is bypassed easily in Python, as we can access all the attributes directly.

*****

When to use Aggregation/Composition? Is there a preference?

1. It depends.
	1. If we use a web view, we should use aggregation internally. Swapping things.
	2. When picking up weapons, we'll use aggregation. As our player will swap, or acquire weapons. Use the property method to make intent public.


![](equation005.png)

