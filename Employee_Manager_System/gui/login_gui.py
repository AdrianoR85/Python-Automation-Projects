from customtkinter import *
from tkinter import messagebox
from config.setting import LOGIN_WINDOW_CONFIG, COLORS, FONTS, ASSETS, TEMP_CREDENTIALS
from util.window_utils import create_background, center_window
from gui.components.button import Button
from gui.components.entry import EntryField

class LoginGUI(CTk):
  def __init__(self):
    super().__init__()
    
    self.login_attempts = 0
    self.max_attempts = 3

    # Window Setting
    self._setup_window()
    # Component initialization
    self._create_login_form()


  def _setup_window(self):
    self.geometry(f"{LOGIN_WINDOW_CONFIG['width']}x{LOGIN_WINDOW_CONFIG['height']}")
    self.resizable(LOGIN_WINDOW_CONFIG['resizable'], LOGIN_WINDOW_CONFIG['resizable'])
    self.title(LOGIN_WINDOW_CONFIG['title'])

    center_window(self)
    create_background(self, "cover_image")
  
  
  def _create_login_form(self):
    # Title
    self.title_label = CTkLabel(
      self,
      text=LOGIN_WINDOW_CONFIG['title'],
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

    # Attempts 
    self.attempts_label = CTkLabel(
      self,
      text="",
      bg_color=COLORS['bg_primary'],
      font=FONTS['small'],
      text_color=COLORS['error']
    )
    self.attempts_label.place(x=130, y=330)

    self.bind('<Return>', lambda event:self._handle_login())
  
  def _handle_login(self):
    if self.login_attempts >= 3:
      messagebox.showerror("Blocked", "Many attempts failed. Restart the application.")
      return

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
    self.login_attempts = 0
    self.attempts_label.configure(text="")
    # Here I will call the next screen
    self.destroy()


  def _on_login_failure(self):
    """Actions to perform when login fails"""
    self.login_attempts += 1
    remaining = self.max_attempts - self.login_attempts
    
    if remaining > 0:
        messagebox.showerror("Login Failed", f"Invalid username or password. {remaining} attempt(s) left.")
        self.attempts_label.configure(text=f"Attempts left: {remaining}")
    else:
        messagebox.showerror("Account Locked", "Too many failed login attempts. Please restart the application.")
        self.attempts_label.configure(text="LOCKED - Please restart the application")
        self.attempts_label.place(x=90, y=330)
        self.login_button.configure(state="disabled")
        
    self.username_field.clear()
    self.password_field.clear()
    self.username_field.focus()


