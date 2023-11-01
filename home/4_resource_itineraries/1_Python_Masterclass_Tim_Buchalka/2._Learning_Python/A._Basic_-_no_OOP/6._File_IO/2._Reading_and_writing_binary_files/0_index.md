# 2. Reading and writing binary files
Created Thursday 14 May 2020


* Binary files are files which have 1's and 0's, they can be images, music, video etc.
* Basic principles of reading and writing is just the same, just specify the modes (typecrud).
* binary files use non-text characters.
* Every character of a binary file is an integer ranging from 0 to 255. This is the least unit. We can think of it as 2 hex numbers. **1 byte = 2 hex numbers.**
* **print() **shouldn't be used for writing here, as bytefiles don't accept contents as string/char. Use write() instead.


