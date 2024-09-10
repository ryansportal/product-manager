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

 # Display project details
    self.project_name_label.text = str(self.project.get('project_name', ''))
    self.project_description_label.text = str(self.project.get('description', ''))
     
# Load tasks for the project into the data grid
    self.load_tasks()

  def load_tasks(self):
    project_id = self.project.get('id')
    if project_id:
        tasks = anvil.server.call('get_tasks_for_project', project_id)
        self.tasks_data_grid.items = tasks
 