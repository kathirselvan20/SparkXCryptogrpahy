import GfG_code_modifications
import tkinter
from PIL import Image, ImageTk
from functools import partial


mainWindow = tkinter.Tk()
mainWindow.geometry("700x700")
mainWindow.title("Steganography")

labelResult = tkinter.Label(mainWindow)
labelResult.grid(row=7, column=2)

name = Image.open("test.png")
img = ImageTk.PhotoImage(name)
photo_Label = tkinter.Label(mainWindow, image=img).grid(row=1, column=0)

img = tkinter.StringVar()
data = tkinter.StringVar()
new_img = tkinter.StringVar()
new_img_2 = tkinter.StringVar()

img_Entry = tkinter.Entry(mainWindow, textvariable=img).grid(row=0, column=1)
data_Entry = tkinter.Entry(mainWindow, textvariable=data).grid(row=1, column=1)
new_img_Entry = tkinter.Entry(mainWindow, textvariable=new_img).grid(row=2, column=1)
new_img_2_Entry = tkinter.Entry(mainWindow, textvariable=new_img_2).grid(row=4, column=1)

img_Label = tkinter.Label(mainWindow, text="Enter name with extension: ").grid(row=0, column=0, sticky="e")
data_Label = tkinter.Label(mainWindow, text="Enter data to be encoded: ").grid(row=1, column=0, sticky="e")
new_img_Label = tkinter.Label(mainWindow, text="Enter name of new image with extension: ").grid(row=2, column=0,
                                                                                                sticky="e")
new_img_2_Label = tkinter.Label(mainWindow, text="Enter name with extension: ").grid(row=4, column=0, sticky="e")


GfG_code_modifications.decrypt = partial(GfG_code_modifications.decrypt, labelResult, new_img_2.get())

encrypt_Button = tkinter.Button(mainWindow, text="Encrypt", command=encrypt)
encrypt_Button.grid(row=6, column=4)

mainWindow.mainloop()
