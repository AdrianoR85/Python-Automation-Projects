from PIL import Image
from config.setting import  ASSETS
from customtkinter import *
from config.setting import COLORS
import os

def get_image(image_name):
    try:
      if os.path.exists(ASSETS[image_name]):
        bg_image = Image.open(ASSETS[image_name])
        return bg_image
      else:
        print("Notice: The background image not found.")
        return False
    except Exception as e:
      print("Error to try the image")
      return False

def center_window(self):
    self.update_idletasks()
    width = self.winfo_width()
    height = self.winfo_height()
    x = (self.winfo_screenwidth() // 2) - (width // 2)
    y = (self.winfo_screenheight() // 2) - (height // 2)
    self.geometry(f'{width}x{height}+{x}+{y}')

def setup_window(self, window, bg_color=COLORS['bg_primary']):
    self.geometry(f"{window['width']}x{window['height']}")
    self.resizable(window['resizable'], window['resizable'])
    self.title(window['title'])
    self.configure(fg_color=bg_color)