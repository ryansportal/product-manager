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
     new_project_name = self.projname_box.text
     new_description = self.projdesc_box.text
     new_due_date = self.date_picker_1.date
     #assignee = self.assignee_drop_down


       
     if new_project_name:
            try:
                # Call the server function to create a new project
                project_id = anvil.server.call('create_project', new_project_name, new_description, new_due_date)
                # Check if the project ID was returned successfully
                if project_id:
                    alert(f"Project created successfully with ID: {project_id}")
                    open_form('projects')
                else:
                    alert("Failed to create project.")
            except Exception as e:
                alert(f"An error occurred: {e}")
     else:
            alert("Please enter a project name.")