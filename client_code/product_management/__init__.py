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

  # Load all projects when the form is initialized
   self.load_projects()

  def load_projects(self):
        # Call the server function to fetch all projects
   projects = anvil.server.call('get_all_projects')
        
        # Set the fetched projects as the items for the repeating panel
   self.repeating_panel_1.items = projects

  def repeating_panel_1_show(self, **event_args):
    """This method is called when the repeating panel is shown on the screen"""
    pass
