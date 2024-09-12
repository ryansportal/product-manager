from ._anvil_designer import ProjectDetailForm_copyTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ProjectDetailForm_copy(ProjectDetailForm_copyTemplate):
  def __init__(self, project=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Save the passed project row to use later
    self.project_row = project  # Use the 'project' parameter passed to the form

    # Load tasks for the project into the data grid
    self.load_tasks()

  def load_tasks(self):
    # Ensure we have a valid project_row
    if self.project_row:
      # Call the server function to get tasks for this project
      tasks = anvil.server.call("get_tasks_for_project", self.project_row)

      # Set the tasks to the data grid or repeating panel
      self.repeating_panel_1.items = tasks
    else:
      alert("No project was provided to load tasks.")
