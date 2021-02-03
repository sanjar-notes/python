import tkinter

mainWindow = tkinter.Tk()

mainWindow.title('Hello World')
mainWindow.geometry('640x40')

# text inside using Label widget
label = tkinter.Label(mainWindow, text='Inside the window')
label.pack(side='top')

# create canvas widget inside
canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=5)
canvas.pack(side='top', expand=False)

mainWindow.mainloop()
