from ._anvil_designer import ProjectDetailFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ProjectDetailForm(ProjectDetailFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  # Store the project information in a class attribute for further use
    self.project = project
        
        # Display the project details
    if project:
       self.project_name_label.text = project['name']
       self.project_description_label.text = project['description']
       self.due_date_label.text = str(project['due_date'])

  def new_task_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def delete_task_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

