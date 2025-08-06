from customtkinter import *
from PIL import Image

root = CTk()
root.geometry('930x478')
root.resizable(0,0)
root.title('Login Page')

# Add a imagem in the login page
"""
Create a Object image passing the image as parameter. 
CTKImage is a object that we use to create a image.
Image.open is used to get the image.
After created the image, create a label. It will use to add the image.
So, use the method place for position the image on root
"""
image = CTkImage(Image.open("assets/cover.png"), size=(930,478))
imageLabel=CTkLabel(root, image=image, text="")
imageLabel.place(x=0, y=0)

handlingLabel = CTkLabel(root, 
                        text="Employee Management System", 
                        bg_color="#FFFFFF",
                        font=("Goudy Old Style", 20, "bold"),
                        text_color="dark blue" 
                      )
handlingLabel.place(x=20, y=100)

usernameEntry = CTkEntry(root, width=180, placeholder_text="Enter your username")
usernameEntry.place(x=50, y=150)

passwordEntry = CTkEntry(root, width=180, placeholder_text="Enter your password", show="*")
passwordEntry.place(x=50, y=200)

loginBtn = CTkButton(root, text="Login", cursor="hand2")
loginBtn.place(x=70, y=250)

root.mainloop()