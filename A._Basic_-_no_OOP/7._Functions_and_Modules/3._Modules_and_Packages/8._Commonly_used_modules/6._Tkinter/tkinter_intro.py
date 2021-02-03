import tkinter

# make a window object============>
mainWindow = tkinter.Tk()

# set external properties===========>
mainWindow.title('Sample Window Title - Hello World')
# seperated by x, position is specified using first (+, -) from (L, R) and (+, -) from (U, D) all in pixels
# mainWindow.geometry('480x480')
mainWindow.geometry('480x480-0-0') # either set the position(fully) or leave it to the OS

# this sample has no components============>
# nothing!!

# connect it to the event loop=============>
mainWindow.mainloop()
