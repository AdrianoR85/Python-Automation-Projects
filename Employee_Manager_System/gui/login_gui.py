from customtkinter import *
from PIL import Image
from tkinter import messagebox
from config.setting import WINDOW_CONFIG, COLORS, FONTS, ASSETS, TEMP_CREDENTIALS


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
    ...
