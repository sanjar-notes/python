# 2. Importing - Syntax
Created Friday 15 May 2020

This a demo about the **import **command(in various forms).
There are 4 variations of ``import`` in Python 3:

#### **Version 1 - Import whole module, use with reference**
	import myModule
	
	print(myModule.variableX) # variable
	myModule.functionY() # function
	barObject = myModule.classZ(1,2) # class

**Details** - [turtledemo_version_1.py](turtledemo_version_1.py)

* imports *everything* from myModule.
* Dot notation is used for accessing objects in the module.


#### **Version 2 - Selective import, use without reference**
	from import_module import thing_1, thing_2
	
	thing_1.play() # use - module name not required

**Details** - [turtledemo_version_2.py](turtledemo_version_2.py)

* import the needed object by specifying it.
* As we've imported the objects, there's no need to use the module(in fact, it would be an error).
* Importing like this can overshadow existing variables(in the script or between modules) with the same name.

	x = 23
	from A import x # initialized to 65 in A
	print(x) # 65 - collision, main.x overwritten
	
	#-----------------------
	from A import x # x is 1
	from B import x # x is 2
	print(x)  # 2 - collision overwrote x(from A)
	
	#----------------------
	from A import x # x is 1
	import B # has an x set to 2
	print(x)  # 1
	print(B.x) # 2 no collision, x and B.x are separate entities

Note: It's not a good idea to import a whole module and also objects from it simultaneously - to avoid the confusion. **It's not an error though.**

#### **Version 3 - Import with alias**
	# type 1 - import the whole module
	import time as t
	t.sleep() # use
	
	# type 2 - import an object within as alias
	from time import sleep as sp 
	sp() # == sleep()

**Details**

* Original names are not accessible if an alias exists. Python keeps the namespace minimalistic.


#### **Version** 4** - Import whole module, use without reference**
	from module_name import *
	# it's not a good practice, may clash with the existing code
	# bcoz Python lets us overshadow inbuilt functions too - may lead to pesky bugs
	
	print(Car) # all objects added to global namespace

**Details** -  [./turtledemo_version_3.py](turtledemo_version_3.py)

* This imports everything(except things starting with _) from the module.
* Asterisk is allowed only at the module level, i.e globally. It cannot be used in functions, classes
* Use of ``import *`` is discouraged because it can change objects on object collision, and is will not report an error.
* MAID: Remember that ``from`` comes before ``import``. Had this not been the rule, we'd have used ``from`` to import a module instead of ``import``. But ``import`` is the primary keyword. [Secondary=``from``], Primary=``import`` is followed here.



#### Syntax details

* In ``import``, for example ``import pack1.pack2.item``, all the words before ``item`` must be packages. ``item`` can be a module or package.
* In ``from``-``import``, for example ``from pack1.pack2.item1 import item2``, there are two possibilities:
	* If ``item1`` is a package, them ``item2`` *must* be a module. Only ``item2`` is added to namespace.
	* If ``item1`` is a module, then ``item2`` must be a object(cannot be package or module). Only ``item2`` is added to namespace.

Simply remember that ``from``-``import`` needs a single word as the ``import`` argument. 

#### Note

* We have skipped some versions like 'selective import, use with reference' etc. This is because either they don't make sense or are already covered by other versions.
* No need to select the version when coding, write what comes naturally.
* Remember - Either be specific during import or specific each time, but not both.
* Dot notation is followed for both importing(file path or selective) and use of modules.
* [Import conventions](https://realpython.com/absolute-vs-relative-python-imports/#styling-of-import-statements)


