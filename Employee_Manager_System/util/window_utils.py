from PIL import Image
from config.setting import LOGIN_WINDOW_CONFIG, COLORS, FONTS, ASSETS, TEMP_CREDENTIALS
from customtkinter import *
import os

def create_background(self, image_name):
    try:
      if os.path.exists(ASSETS[image_name]):
        self.bg_image = CTkImage(
          Image.open(ASSETS[image_name]),
          size=(LOGIN_WINDOW_CONFIG['width'], LOGIN_WINDOW_CONFIG['height'])
        )
        self.bg_label = CTkLabel(self, image=self.bg_image, text="")
        self.bg_label.place(x=0, y=0)
      else:
        self.configure(fg_color=COLORS['secondary'])
        print("Notice: The background image not found.")
    except Exception as e:
      print("Error to try the image")
      self.configure(fg_color=COLORS['secondary'])

def center_window(self):
    self.update_idletasks()
    width = self.winfo_width()
    height = self.winfo_height()
    x = (self.winfo_screenwidth() // 2) - (width // 2)
    y = (self.winfo_screenheight() // 2) - (height // 2)
    self.geometry(f'{width}x{height}+{x}+{y}')