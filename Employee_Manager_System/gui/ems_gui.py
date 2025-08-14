from customtkinter import *
from util.window_utils import center_window, create_background, setup_window
from config.setting import WINDOW_EMS

class ManagementSystemGUI(CTk):
  def __init__(self):
    super().__init__()

    setup_window(self, WINDOW_EMS)
    center_window(self)


