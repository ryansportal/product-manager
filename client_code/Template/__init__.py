from ._anvil_designer import TemplateTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Template(TemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.



  def home_button_click(self, **event_args):
    open_form('Home')

  def product_management_button_click(self, **event_args):
    open_form('product_management')

  def button_logout_click(self, **event_args):
    anvil.users.logout()
    open_form('Login')
