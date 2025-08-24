from customtkinter import * # type: ignore
from tkinter import messagebox
from config.setting import LOGIN_WINDOW_CONFIG, COLORS, FONTS, COMPONENT_CONFIG
from util.window_utils import get_image, center_window, setup_window
from services.auth_user import AuthUser


class LoginGUI(CTk):
  def __init__(self):
    super().__init__()
    
    self.login_attempts = 0
    self.max_attempts = 3

    # Window Setting
    self._main_window()
    
    # Component initialization
    self._create_login_form()
    self._setup_binding()  

  def _main_window(self):
    setup_window(self, LOGIN_WINDOW_CONFIG)
    center_window(self)
    
    self._create_backgroud()
  

  def _create_backgroud(self):
    if get_image('cover_image'):
      image = get_image('cover_image')
      banner = CTkImage(image, size=(LOGIN_WINDOW_CONFIG['width'], LOGIN_WINDOW_CONFIG['height'])) # type: ignore
      banner_label = CTkLabel(self, image=banner, text="")
      banner_label.grid(row=0, column=0, columnspan=2)
    else:
      self.configure(fg_color=COLORS['secondary'])


  def _create_login_form(self):
    # Title
    self.title_label = CTkLabel(
      self,
      text=LOGIN_WINDOW_CONFIG['title'],
      bg_color=COLORS['secondary'],
      font=FONTS['title'],
      text_color=COLORS['text_primary'] )
    self.title_label.place(x=45, y=100)

    # Username Field
    self.username_entry = CTkEntry(
      self,
      width=COMPONENT_CONFIG['entry_width'],
      height=COMPONENT_CONFIG['entry_height'],
      placeholder_text="Entry your username" )
    self.username_entry.place(x=80, y=160)

    # Password Field
    self.password_entry = CTkEntry(
      self,
      width=COMPONENT_CONFIG['entry_width'],
      height=COMPONENT_CONFIG['entry_height'],
      placeholder_text="Entry your password",
      show="*" )
    self.password_entry.place(x=80, y=220)

    # Button
    self.login_button = CTkButton(
      self,
      width=COMPONENT_CONFIG['btn_login_width'],
      height=COMPONENT_CONFIG['btn_login_height'],
      text="Login",
      font=FONTS['button'],
      command=self._handle_login)
    self.login_button.place(x=80, y=280)

    # Attempts 
    self.attempts_label = CTkLabel(
      self,
      text="",
      bg_color=COLORS['bg_primary'],
      font=FONTS['small'],
      text_color=COLORS['error'])
    self.attempts_label.place(x=160, y=330)

    self.bind('<Return>', lambda event:self._handle_login())
    self.username_entry.focus()
  
  def _handle_login(self):
    if self.login_attempts >= 3:
      messagebox.showerror("Blocked", "Many attempts failed. Restart the application.")
      return

    username = self.username_entry.get().strip()
    password = self.password_entry.get().strip()

    if not self._validate_inputs(username, password):
      return
    
    # Temporary credential check
    if self._authenticate_user(username, password):
      self._on_login_success()
      
      from gui.ems_gui import ManagementSystemGUI
      ems = ManagementSystemGUI()

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
    return AuthUser.login(username, password)
  

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
        
    self.username_entry.delete(0, 'end')
    self.password_entry.delete(0, 'end')
    self.username_entry.focus()


  def _setup_binding(self):
    self.username_entry.bind("<FocusIn>", 
        lambda e: self.username_entry.configure(border_color=COLORS['border_focus']))
    self.username_entry.bind("<FocusOut>", 
        lambda e: self.username_entry.configure(border_color=COLORS['border_light']))
    
    self.password_entry.bind("<FocusIn>", 
        lambda e: self.password_entry.configure(border_color=COLORS['border_focus']))
    self.password_entry.bind("<FocusOut>", 
        lambda e: self.password_entry.configure(border_color=COLORS['border_light']))

