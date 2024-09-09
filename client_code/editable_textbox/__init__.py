from ._anvil_designer import editable_textboxTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class editable_textbox(editable_textboxTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.outlined_button_1.visible=True
    self.outlined_button_2.visible=False

    self.outlined_button_1.text =""
    self.outlined_button_2.text= self.outlined_button_1.text

  def outlined_button_1_click(self, **event_args):
    """This method is called when the label is clicked"""
    self.outlined_button_1.visible = False
    self.outlined_button_2.visible = True
    self.outlined_button_2.focus()
   
  # Event when textbox loses focus (or Enter is pressed)
  def outlined_button_2_lost_focus(self, **event_args):
    """This method is called when the textbox loses focus"""
    self._update_text()

  def outlined_button_2_enter_pressed(self, **event_args):
    """This method is called when the user presses Enter in the textbox"""
    self._update_text()

  def _update_text(self):
    """Update the text and switch back to label mode"""
    self.outlined_button_1.text = self.outlined_button_2.text
    self.outlined_button_1.visible = True
    self.outlined_button_2.visible = False

  