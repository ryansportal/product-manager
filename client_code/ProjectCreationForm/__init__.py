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

    # Call the server function to get the list of user names
    users = anvil.server.call('get_user_names')
    # Create a list of tuples for dropdown items (display_name)
    user_items = [(user['name'], user['name']) for user in users]
    
    # Populate the dropdown with user names
    self.assignee_drop_down.items = user_items

  def addproject_button_click(self, **event_args):
     new_project_name = self.projname_box.text
     new_description = self.projdesc_box.text
     new_due_date = self.date_picker_1.date
     new_assignee = self.assignee_drop_down.selected_value


       
     if new_project_name:
            try:
                # Call the server function to create a new project
                project_id = anvil.server.call('create_project', new_project_name, new_description, new_assignee, new_due_date)
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