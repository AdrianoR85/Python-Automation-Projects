from customtkinter import *
from PIL import Image
from tkinter import messagebox
from config import WINDOW_CONFIG, COLORS, FONTS, ASSETS, TEMP_CREDENTIALS


class LoginGUI(CTk):
  def __init__(self, master):
    self.master = master

    master.geometry('930x478')
    master.resizable(0,0)
    master.title('Login Page')

    # Add a imagem in the login page
    """
    Create a Object image passing the image as parameter. 
    CTKImage is a object that we use to create a image.
    Image.open is used to get the image.
    After created the image, create a label. It will use to add the image.
    So, use the method place for position the image on master
    """
    self.image = CTkImage(Image.open("assets/cover.png"), size=(930,478))
    imageLabel=CTkLabel(master, image=self.image, text="")
    imageLabel.place(x=0, y=0)

    handlingLabel = CTkLabel(master, 
                            text="Employee Management System", 
                            bg_color="#FFFFFF",
                            font=("Goudy Old Style", 20, "bold"),
                            text_color="dark blue" 
                          )
    handlingLabel.place(x=20, y=100)

    self.usernameEntry = CTkEntry(master, width=180, placeholder_text="Enter your username")
    self.usernameEntry.place(x=50, y=150)

    self.passwordEntry = CTkEntry(master, width=180, placeholder_text="Enter your password", show="*")
    self.passwordEntry.place(x=50, y=200)

    self.loginBtn = CTkButton(master, text="Login", cursor="hand2", command=self.login)
    self.loginBtn.place(x=70, y=250)

  def login(self):
    
    if self.usernameEntry.get() == "" or self.passwordEntry.get() == "":
      messagebox.showerror("Error", "All fields are required.")
    elif self.usernameEntry.get() == "adriano" and self.passwordEntry.get() == "1234":
      messagebox.showinfo("Sucess", "Login is successul.")
      self.master.destroy()
    else:
      messagebox.showerror("Error", "Wrong Credentials.")