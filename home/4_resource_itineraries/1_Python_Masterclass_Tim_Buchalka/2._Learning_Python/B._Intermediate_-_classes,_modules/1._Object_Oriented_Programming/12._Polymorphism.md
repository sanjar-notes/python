# 12. Polymorphism
Created Thursday 28 May 2020

![](pasted_image%2013.png)

* The print() function is a very good example of polymorphism.
* Python is not statically typed, so method overloading is absent in Python. It is not necessary either. Polymorphism is achieved using inheritance.
* We use default arguments to indicate the type of the object required.
* My understanding: 
	1. In Java/C++, we go search for the relevant function according to the type of argument. In other words, We have many options for the different arguments. All these are standalone function, are overloads of each other. The compiler decides.

![](pasted_image007.png)
![](pasted_image002%205.png)
![](pasted_image003%203.png)
![](pasted_image004%202.png)
![](pasted_image005%201.png)
![](pasted_image006%201.png)

2. Each function calls the String.**valueOf **method to get the string methods.
3. valueOf method is also overloaded, it does work out the value from the object, instead, it asks for the string representation from the object itself.

![](pasted_image008.png)
![](pasted_image009.png)

4. So if we want to print an int, the method calls the Integer class' toString method. Similarly for Long, Float and Double, the toString method's called to get the string representation of the object. It's the same for the other types too, they just wouldn't fit on the screen. the valueOf method delegates the task of deciding what the string representation of each class should be, to the **class itself**.
5. Now if valueOf **just** delegates the task to the class, it doesn't really need to know what class it's dealing with. Whatever it gets, it could just call the toString method and return the result. And that's exactly the approach that Python takes. i.e **overloading is not a necessity**.


*****

Python takes a very different approach: It focuses on what something does instead of what type it is.
the **toString()** is equivalent to **__str__()**

* As everything is a new style class in Python, anything(everything is an object) has the __str__ method, atleast from the **object **class, the topmost base class. This makes **everything printable**. This **__str__ **returns a string conatining the name of the class with a hashcode of the memory address for the object.
* **Inheritance isn't the only way to implement polymorphism. Allowing duck typing can also help, **i.e composition.


*****

But what about other cases(except print, where there is no guarantee), e.g we have to give an Enemy object, but we give some other of kind of object? The given arg maynot contain relevant functions? What will happen?

1. In Java/C++ this is simply not possible, even if the relevant funtions are present. Compilation Error.
2. Python is interested in what the object does , i.e in the behavior, it does not care about the type. So if relevant functions are present, it runs fine. If they are absent, we simply get an Attribute Error.

This is called Duck Typing, in dynamically typed languages. It is **another way **to implement polymorphism.

