# 6. Tkinter
Created Thursday 21 May 2020

**Intro**

* Tkinter is a GUI framework used to create simple to moderate GUI apps using python.
* It internally uses the TCL language that's embedded into Python.
* It is robust and platform independent.
* It has themed widgets which look different for different platforms/OSs.
* Python 2, T is capital, i.e Tkinter

We can deal with this easily,
	try:
		import tkinter
	except ImportError:
		import Tkinter as tkinter
	
	# app code using tkinter, Python3
	

*****

**Basics:**

1. We have a main window, it has some external properties like titles, size, initial position etc.
2. We have a connected event loop.
3. The mainwindow has components inside.

[tkinter_intro.py](tkinter_intro.py)

