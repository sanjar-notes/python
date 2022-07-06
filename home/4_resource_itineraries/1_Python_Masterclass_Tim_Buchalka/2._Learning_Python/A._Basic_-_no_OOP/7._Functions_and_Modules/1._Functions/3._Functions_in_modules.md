# 5. Functions in modules
Created Thursday 21 May 2020


* We want to make custom modules involving classes and functions


**Situation:**

1. Running independently/alone/(as a script): Python allows this behavior for previewing purposes. Check tkinter and turtle.

	# testing.py
	print(__name__) # prints __main__
		

2. Imported: The running, i.e main part of the code also runs.

	# testing.py
	import testing # testing.py is printed
	# our code
			
**Problem**: Imported files(at the start) are loaded **into memory** and **executed** as soon as we start execution of the main file. The music player starts automatically, in our case. This behavior prevents us from **choosing **what we want to do, when we import the module.

**Goal(s)**: We want to: 

1. To run the player directly(i.e as a script) if we run the [test_module](test_module.py) alone.
2. To not run the player directed, when it has been imported as a module in a main file, [test_runner.py.](test_runner.py)


**Jargon:**

* **__name__ **- The module's name. It is equal to **'__main__'** if the file is being run independently, i.e as a script. 
* This property is used to give the desired behavior of running directly(as a script) *vs* being **imported but not executed**.  


**Solution: **Add code above the main part of the module, to run only if, no other changes are required.
An example:  [test_module](test_module.py) [test_runner.py.](test_runner.py)

Note: 

1. We can also print a message in a module if it is not meant to be active/script.
2. We need to do this because python does not have a **fixed **main function.


**Lessons:**

1. Write the test before any program, this will ensure easy reuse. Treat it like a main() 🙃️

	# functions and classes
	
	if __name__=='__main__':
		#runner code

