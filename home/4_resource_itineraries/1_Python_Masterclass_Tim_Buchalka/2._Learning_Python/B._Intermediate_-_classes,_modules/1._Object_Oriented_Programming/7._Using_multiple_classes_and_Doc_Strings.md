# 7. Using multiple classes and Doc Strings
Created Friday 22 May 2020
[./song.py](song.py)


* They are defined just below the class, method definition, function, modules.
* They are used by help() and various other documentation processing systems.



1. Doc strings describe:
	1. What it does?
	2. How to use it?
	3. Corner cases, most probable errors.
2. How to access?

To access, docs for the description of something, we use the __doc__ special attribute:

1. For the whole class, do ClassName.__doc__
2. For a method, ClassName.methodName.__doc__
3. For a variable, ClassName.variableName.__doc__ - This is pretty useless, it returns doc for the type, e.g int info, string info.


3. How to write them:
	1. Create triple-double quotes
	2. Don't use the u prefix as all strings in Python 3 are already unicode.
	3. For multiline docstrings, have a subject line, a blank line and then the description.
	4. Indentation - The quotes are considered part of the docstring, keep them same as the next top-level code.
	5. For things
		1. For classes, write documentation for the attributes and methods.
		2. For function, write the process overview and return value
		3. For module, write the function and classes.
		4. For a package, in __init__.py, Write about the packages and sub-packages.

@__doc__

