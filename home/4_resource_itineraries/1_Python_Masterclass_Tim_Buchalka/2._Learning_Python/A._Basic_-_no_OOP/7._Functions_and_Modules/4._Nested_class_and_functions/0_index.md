# 7. Nested functions
Created Friday 22 May 2020


* Python allows functions to be nested inside one another(an **embedded function**), this is to top level helper functions which are disjoint. Keeping the recursive part inside the helper.[Nesting_functions.py](nesting_functions.py)
* There's an issue with this, the recursive function must be defined before calling it. It may have some params that we do not pass to the recursive function, and want to use inside it. There are two ways to do this:
	1. Define such terms before the recursive function. Clumsy.
	2. Define such terms after the recursive function, but tag the terms **nonlocal **inside the recursive function. Non local variables must exist in the nearest enclosing scope. 

Note: 

1. The **nonlocal** variable needs to be defined, as it'll be searched for in the enclosing scope. This is because the scope of creating is undefined.
2. The **global **variable can create variables too, although we cannot do this in one line. This is allowed because global variables are accessible everywhere, i.e traceable.
3. Creating variables like this is not a good practice though.
4. This type of should be used from **out-to-in **scopes, and not the other way around.


#### Details about class/function nesting

1. Nesting is mostly to one level, rarely being 2 leveled.
2. As python is executed line by line, we can have a variable in a function which is not a variable before the definition. **Not like** C++. C++ is visually scoped, simple. Python is flow oriented/scripting.

![](pasted_image002%209.png) same as ![](pasted_image003%206.png)

