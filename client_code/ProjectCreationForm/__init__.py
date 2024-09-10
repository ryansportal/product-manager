from ._anvil_designer import ProjectCreationFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ProjectCreationForm(ProjectCreationFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def addproject_button_click(self, **event_args):
     project_name = self.projname_box.text
     description = self.projdesc_box.text
     due_date = self.date_picker_1.date
     #assignee = self.assignee_drop_down

     if project_name:
        anvil.server.call('create_project', project_name, description, due_date)
        alert("Project created successfully!")
        open_form('projects')
     else:
        alert("Please enter a project name.")

       

