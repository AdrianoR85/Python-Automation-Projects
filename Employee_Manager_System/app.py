from customtkinter import CTk
from gui.login_gui import LoginPage

if __name__ == "__main__":
  root = CTk()
  ms = LoginPage(root)
  root.mainloop()
  