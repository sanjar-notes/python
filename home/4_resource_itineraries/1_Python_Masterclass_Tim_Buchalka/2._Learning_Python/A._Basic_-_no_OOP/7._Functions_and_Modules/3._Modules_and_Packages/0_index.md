# 3. Modules and Packages
Created Friday 15 May 2020

#### Modules
**A module is a just a python file.**

* Every Python file is [already](https://stackoverflow.com/a/34826647/11392807) a module, its identifier(for reference elsewhere) being the file's base name without the ``.py`` extension.
* A module can be run alone, i.e it's not a requirement for them to be dumb(i.e to be devoid of runnable code).
* Python has many in-built modules, and we can create our own too.

The code written till now **did not** require importing any modules. Using modules encourages reuse, as well as abstraction.


17. Why have a new term called module, if every python file is a module?
18. Technically there's no difference. The term is **arbitrary**, it is only for communicating whether a file has implementations or not. So a file which mainly has driver code, not implementations or core logic is called a *script*, and a file having them is called a *module*.


#### Packages
**A package is a directory of modules containing an additional ``__init__.py`` file.**

* They are used to group related modules.
* Packages need to have a ``__init__.py`` file(even if it's empty), to distinguish a package from a directory that just happens to contain a bunch of Python files.
* Packages can be nested to any depth, provided that each package(including subpackages) has an ``__init__.py`` file.


#### Mental model

* module ~ file in a filesystem
* package ~ directory in a filesystem

![](pasted_image%2030.png)

#### package vs module

* The distinction between module and package holds *just* at the *file system level*. In the code, the object created by Python for module/package is the same, of type ``module``.
* Both have the same syntax for import(like include in C++) and 


