from customtkinter import CTkButton
from config.setting import COLORS, FONTS, COMPONENT_CONFIG

class Button(CTkButton):
  def __init__(self, master, text="", command=None, **kwargs):
    self.original_command = command

    super().__init__(
      master,
      text=text,
      bg_color="#FFFFFF",
      command=self._handle_click,
      width=COMPONENT_CONFIG['button_width'],
      height=COMPONENT_CONFIG['button_height'],
      font=FONTS['button'],
      corner_radius=COMPONENT_CONFIG['border_radius'],
      cursor="hand2",
      fg_color=COLORS['primary'],
      hover_color=COLORS['primary_hover'],
      text_color=COLORS['text_light'],
      border_width=0,
      **kwargs
    )

  def _handle_click(self):
    if self.original_command:
      self.original_command()

