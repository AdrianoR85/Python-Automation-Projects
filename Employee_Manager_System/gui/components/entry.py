from customtkinter import CTkEntry, CTkLabel, CTkFrame
from config.setting import COLORS, FONTS, COMPONENT_CONFIG


class EntryField(CTkFrame):
  def __init__(self, master, placeholder_text="", show="", label_text="", **kwargs):
    super().__init__(master, fg_color="#ffffff", **kwargs)

    self.placeholder_text = placeholder_text
    self.show = show
    self.label_text = label_text

    self._create_widgets()
    self._setup_binding()
  

  def _create_widgets(self):
    if self.label_text:
      self.label = CTkLabel(
        self, 
        text=self.label_text,
        font=FONTS['label'],
        text_color=COLORS['text_secondary'],
        bg_color=COLORS['bg_primary']
      )
      self.label.pack(anchor='w', pady=(0,8))
    
    self.entry = CTkEntry(
      self,
      width=COMPONENT_CONFIG['entry_width'],
      height=COMPONENT_CONFIG['entry_height'],
      placeholder_text=self.placeholder_text,
      font=FONTS['entry'],
      show=self.show,
      border_width=2,
      border_color=COLORS['border_light'],
      fg_color=COLORS['bg_primary'],
      text_color=COLORS['text_primary'],
      placeholder_text_color=COLORS['text_secondary'],
      corner_radius=COMPONENT_CONFIG['border_radius']
    )
    self.entry.pack()

  def _setup_binding(self):
    self.entry.bind("<FocusIn>", self._on_focus_in)
    self.entry.bind("<FocusOut>", self._on_focus_out)
  
  
  def _on_focus_in(self, event):
    self.entry.configure(border_color=COLORS['border_focus'])
  

  def _on_focus_out(self, event):
    self.entry.configure(border_color=COLORS['border_light'])

  
  def get(self):
    return self.entry.get()
  
  
  def clear(self):
    self.entry.delete(0, "end")


  def focus(self):
    self.entry.focus()