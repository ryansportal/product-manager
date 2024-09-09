from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Login(LoginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  # if user is not None:
     # open_form('Home')  # Replace 'new_form_name' with the actual form you want to open

  def button_login_click(self, **event_args):
    user = anvil.users.login_with_form(allow_cancel=True)
    if user is not None:
      from ..Startup import Startup
      Startup()
