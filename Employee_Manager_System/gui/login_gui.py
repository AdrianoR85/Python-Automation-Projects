import os
from customtkinter import *
from tkinter import messagebox
from PIL import Image
from config.setting import WINDOW_CONFIG, COLORS, FONTS, ASSETS, TEMP_CREDENTIALS
from gui.components.button import Button
from gui.components.entry import EntryField


class LoginGUI(CTk):
  def __init__(self):
    super().__init__()

    # Window Setting
    self._setup_window()

    # Component initialization
    self._create_widgets()


  def _setup_window(self):
    self.geometry(f"{WINDOW_CONFIG['width']}x{WINDOW_CONFIG['height']}")
    self.resizable(WINDOW_CONFIG['resizable'], WINDOW_CONFIG['resizable'])
    self.title(WINDOW_CONFIG['title'])

    self._center_window()
  

  def _center_window(self):
    self.update_idletasks()
    width = self.winfo_width()
    height = self.winfo_height()
    x = (self.winfo_screenwidth() // 2) - (width // 2)
    y = (self.winfo_screenheight() // 2) - (height // 2)
    self.geometry(f'{width}x{height}+{x}+{y}')


  def _create_widgets(self):
    self._create_background()
    self._create_login_form()
  

  def _create_background(self):
    try:
      if os.path.exists(ASSETS['cover_image']):
        self.bg_image = CTkImage(
          Image.open(ASSETS['cover_image']),
          size=(WINDOW_CONFIG['width'], WINDOW_CONFIG['height'])
        )
        self.bg_label = CTkLabel(self, image=self.bg_image, text="")
        self.bg_label.place(x=0, y=0)
      else:
        self.configure(fg_color=COLORS['secondary'])
        print("Notice: The background image not found.")
    except Exception as e:
      print("Error to try the image")
      self.configure(fg_color=COLORS['secondary'])
  

  def _create_login_form(self):
    # Title
    self.title_label = CTkLabel(
      self,
      text=WINDOW_CONFIG['title'],
      bg_color=COLORS['secondary'],
      font=FONTS['title'],
      text_color=COLORS['text_primary']
    )
    self.title_label.place(x=40, y=100)

    # Username Field
    self.username_field = EntryField(
      self,
      placeholder_text="Entry your username",
    )
    self.username_field.place(x=60, y=160)

    # Password Field
    self.password_field = EntryField(
      self,
      placeholder_text="Entry your password",
      show="*"
    )
    self.password_field.place(x=60, y=220)

    # Button
    self.login_button = Button(
      self,
      text="Login",
      command=self._handle_login
    )
    self.login_button.place(x=60, y=280)


    self.bind('<Return>', lambda event:self._handle_login())

    self.username_field.focus()
  

  def _handle_login(self):
    username = self.username_field.get().strip()
    password = self.password_field.get().strip()

    if not self._validate_inputs(username, password):
      return
    
    # Temporary credential check
    if self._authenticate_user(username, password):
      self._on_login_success()
    else:
      self._on_login_failure()


  def _validate_inputs(self, username, password):
    """Input field validation"""
    if not username or not password:
      messagebox.showerror("Error", "All fields are required.")
      return False
    return True
  

  def _authenticate_user(self, username, password):
    """User authentication (temporary implementation)"""
    return (username == TEMP_CREDENTIALS['username'] and
            password == TEMP_CREDENTIALS['password'])
  
  
  def _on_login_success(self):
    messagebox.showinfo("Success", "Login is successful.")
    # Here I will call the next screen
    self.destroy()


  def _on_login_failure(self):
    messagebox.showerror("Error", "Invalid credentials.")
    self.password_field.clear() # Clean the password
    self.username_field.clear() # clean the username
    self.username_field.focus() # Focus on username field