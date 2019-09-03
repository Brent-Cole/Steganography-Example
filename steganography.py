from stegano import lsb
from tkinter import *
from tkinter import ttk
import os
window = Tk()
window.title("Steganography Example")
window.geometry("275x200")

#insert a warning label about valid file formats
Label(window, text= "Valid file format extensions: png and bmp").pack()
#The file name to act on
Label(window, text="Please enter your file name: ").pack()
entry = ttk.Entry(window, width = 30)
entry.pack()

#Enter a check box to see if we are hiding or recovering a message
var1 = IntVar()
check = ttk.Checkbutton(window, text = "Reveal?",variable = var1)
check.pack()

#The text to be hidden in the picture
Label(window, text="Whats your secret? ").pack()
entry2 = ttk.Entry(window, width = 30)
entry2.pack()


#button
button = ttk.Button(window, text="Finish")
button.pack()

def pressed():
    #print("Button has been clicked")
    file_name = entry.get()
    secret = entry2.get()
    #print("Var1: ", var1.get())
    if var1.get()==1:
        if os.path.isfile(file_name) == True:       #verify we have a valid file name before we open it
            clear_message = lsb.reveal(file_name)
            entry2.insert(0,clear_message)

    else:
        if os.path.isfile(file_name) == True:       #verify we have a valid file name before we open it
            act = lsb.hide(file_name,secret)
            act.save("Secret_Picture.png")
        else:
            print("Not a valid file name!!")

button.config(command = pressed)


window.mainloop()


