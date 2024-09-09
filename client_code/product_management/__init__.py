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

def add_project_links(self):
    #clear out the container that the links are in
    self.link_panel.clear()
    #get a list of the projects from the database
    for row in anvil.server.call('get_projects'):
      #create a link
      link = Link(text=row["project_name"], tag=row)
      #set up a event handler that opens the project when the link is clicked
      link.set_event_handler("click", self.open_project)
      #add the link to the container
      self.link_panel.add_component(link)