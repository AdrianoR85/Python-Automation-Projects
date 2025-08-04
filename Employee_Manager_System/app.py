from customtkinter import *
from PIL import Image

root = CTk()
root.geometry('930x478')
root.resizable(0,0)
root.title('Login Page')
image = CTkImage(Image.open("assets/cover.png"), size=(930,478))
imageLabel=CTkLabel(root, image=image, text="")
imageLabel.place(x=0, y=0)
root.mainloop()