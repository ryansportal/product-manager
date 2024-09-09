from ._anvil_designer import product_managementTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class product_management(product_managementTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
#Front end logic to interact with the backend functions in server

  #add new project
  def new_project_click(self, **event_args):
   open_form('ProjectCreationForm')

