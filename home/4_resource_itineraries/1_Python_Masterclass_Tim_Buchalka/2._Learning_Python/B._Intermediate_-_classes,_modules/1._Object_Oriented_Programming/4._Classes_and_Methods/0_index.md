# 4. Classes and Methods
Created Friday 22 May 2020


* Encapsulation - Data and methods of a class are tied together to be used together. Abstraction is used to provide a working way.



1. Have a docstring in every class. Coming up ahead.
2. When accessing data members/methods from inside the class, we have to use **self.**method_name() .    [class_1.py](class_1.py) or use ClassName.method_name(self)

This is definitely different from C++, where this can be omitted if we are inside the class.

3. We should make the data attributes which should be private have a single **underscore** before their names, this indicates that they shouldn't be accessed directly.


*****

Static methods: They are defined before the **init **method in the class. [static_methods.py](static_methods.py)

1. They have no **self** argument.
2. We have to annotate it as a static method.

![](pasted_image%203.png)

3. We should place an **underscore** before the static method name to indicate that it a static method. **Convention.**
4. In code, use the Class name before the static method, to indicate that we're dealing with a static variable. Both are valid though for accessing the static method.

![](assets/pasted_image002.png) ![](pasted_image001%201.png) 

@staticmethod

