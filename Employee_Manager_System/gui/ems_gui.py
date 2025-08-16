from customtkinter import *
from util.window_utils import center_window, get_image, setup_window
from config.setting import WINDOW_EMS, COLORS, COMPONENT_CONFIG, FONTS
from data.role import role_options, gender_options

class ManagementSystemGUI(CTk):
  def __init__(self):
    super().__init__()

    self._main_window()

    self._widgets()
  
  def _main_window(self):
    setup_window(self, WINDOW_EMS, COLORS['bg_secondary'])
    center_window(self)
    self._create_banner()

  def _create_banner(self):
    if get_image('banner'):
      image = get_image('banner')
      banner = CTkImage(image, size=(WINDOW_EMS['width'], WINDOW_EMS['banner_height']))
      banner_label = CTkLabel(self, image=banner, text="")
      banner_label.grid(row=0, column=0, columnspan=2)
    else:
      self.configure(fg_color=COLORS['secondary'])
  
  
  def _widgets(self):
    self._left_frame()
    self._right_frame()


  def _left_frame(self):
    self.left_frame = CTkFrame(self, fg_color=COLORS['bg_secondary'])
    self.left_frame.grid(row=1, column=0)

    # ID
    self.id_label = CTkLabel(
      self.left_frame, text='id', 
      font=FONTS['label'], 
      text_color=COLORS['text_light']
    )
    self.id_label.grid(row=0, column=0, padx=20, pady=15, stick='w')

    self.id_entry = CTkEntry(
      self.left_frame, 
      width=COMPONENT_CONFIG['small_entry_width'], 
      height=COMPONENT_CONFIG['small_entry_height'],
      font=FONTS['entry']
    )
    self.id_entry.grid(row=0, column=1)

    # Name
    self.name_label = CTkLabel(
      self.left_frame, 
      text='name', 
      font=FONTS['label'],
      text_color=COLORS['text_light']
    )
    self.name_label.grid(row=1, column=0, padx=20, pady=15, stick='w')

    self.name_entry = CTkEntry(
      self.left_frame, 
      width=COMPONENT_CONFIG['small_entry_width'], 
      height=COMPONENT_CONFIG['small_entry_height'],
      font=FONTS['entry']
    )
    self.name_entry.grid(row=1, column=1)

    # Phone
    self.phone_label = CTkLabel(
      self.left_frame, 
      text='Phone', 
      font=FONTS['label'],
      text_color=COLORS['text_light']
    )
    self.phone_label.grid(row=2, column=0, padx=20, pady=15, stick='w')

    self.phone_entry = CTkEntry(
      self.left_frame, 
      width=COMPONENT_CONFIG['small_entry_width'], 
      height=COMPONENT_CONFIG['small_entry_height'],
      font=FONTS['entry']
    )
    self.phone_entry.grid(row=2, column=1)

    # Role
    self.role_label = CTkLabel(
      self.left_frame, 
      text='Role', 
      font=FONTS['label'],
      text_color=COLORS['text_light']
    )
    self.role_label.grid(row=3, column=0, padx=20, pady=15, stick='w')

    self.role_box = CTkComboBox(
      self.left_frame, 
      width=COMPONENT_CONFIG["small_entry_width"], 
      height=COMPONENT_CONFIG["small_entry_height"],
      values=role_options,
      state="readonly",
      font=FONTS['entry']
    )
    self.role_box.grid(row=3, column=1)
    self.role_box.set(role_options[0])

    # Gender
    self.gender_label = CTkLabel(
      self.left_frame, 
      text='Gender', 
      font=FONTS['label'],
      text_color=COLORS['text_light']
    )
    self.gender_label.grid(row=4, column=0, padx=20, pady=15, stick='w')

    self.gender_box = CTkComboBox(
      self.left_frame, 
      width=COMPONENT_CONFIG["small_entry_width"], 
      height=COMPONENT_CONFIG["small_entry_height"],
      values=gender_options,
      state="readonly",
      font=FONTS['entry']
    )
    self.gender_box.grid(row=4, column=1)
    self.gender_box.set(gender_options[0])

    # Salary
    self.salary_label = CTkLabel(
      self.left_frame, 
      text='Salary', 
      font=FONTS['label'],
      text_color=COLORS['text_light']
    )
    self.salary_label.grid(row=5, column=0, padx=20, pady=15, stick='w')

    self.salary_entry = CTkEntry(
      self.left_frame, 
      width=COMPONENT_CONFIG["small_entry_width"], 
      height=COMPONENT_CONFIG["small_entry_height"],
      font=FONTS['entry']
    )
    self.salary_entry.grid(row=5, column=1)


  def _right_frame(self):
    self.right_frame = CTkFrame(self)
    self.right_frame.grid(row=1, column=1)
    