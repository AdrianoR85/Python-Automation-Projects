from customtkinter import CTkButton
from config.setting import COLORS, FONTS, COMPONENT_CONFIG

class Button(CTkButton):
  def __init__(self, master, text="", command=None, style="primary", **kwargs):
    self.style = style
    self.original_command = command

    style_config = self._get_style_config() 

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
      **style_config,
      **kwargs
    )

  def _get_style_config(self):
    styles = {
      "primary": {
        "fg_color": COLORS['primary'],
        "hover_color":COLORS['primary_hover'],
        "text_color": COLORS['text_light'],
        "border_width": 0
      },
      "secondary": {
        "fg_color": "transparent",
        "hover_color":COLORS['primary'],
        "text_color": COLORS['text_light'],
        "border_width": 2,
        "border_color": COLORS['primary']
      },
      "success": {
        "fg_color": COLORS['success'],
        "hover_color":"#059669",
        "text_color": COLORS['text_light'],
        "border_width": 0
      }
    }
    return styles.get(self.style, styles['primary'])
  
  def _handle_click(self):
    if self.original_command:
      self.original_command()

