# 2. Writing to text files
Created Thursday 14 May 2020


1. Using the print function and setting the default argument called file.

	cities = ['Delhi', 'Bombay', 'Akola']
	with open('out.txt', 'w') as f:
		for city in cities:
			print(city, file=f)

If the file does not exist, it will be created.
Modes:
![](pasted_image001%2010.png)

* text or the binary mode is specified by writing it after the mode. e.g **wb** for write binary
* read-write is specified using r+ or w+, both are the same.
* x is useful for creating new files.

Note:

1. There should be** no spaces **on the '=' signs in default arguments, because they are not actually a regular assignment.
2. We can use the optional print arg called **flush**(flush refers to the buffer for the i/o devices), it is set to **False **by default. Think of it like overwriting the buffer as soon as the process is over. This is helpful for real time prints. We may **miss** some lines this way.
3. **strip(**subs**)** removes the letters contained in subs from the beginning and/or end of the string. e.g "muh*ammad sanjar af)aq".strip('abcdefghijklmnopqrstuvwxyz')
4. CR-LF is automatically handled by python in text read mode. e.g for Windows


