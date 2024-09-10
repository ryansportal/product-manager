from ._anvil_designer import ProjectDetailFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ProjectDetailForm(ProjectDetailFormTemplate):
  def __init__(self, project=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

        # Store the passed project in the class so we can display it
    self.project = project
        
        # Display the project details in the form
    if project:
      self.project_name_label.text = project['project_name']
      self.project_description_label.text = project['description']
      self.due_date_label.text = str(project['due_date'])

 # def new_task_click(self, **event_args):
  #  task_title = self.task_title_textbox.text
  #  description = self.task_description_textbox.text
  #  due_date = self.due_date_picker.date
  #  assignee = self.assignee_dropdown.selected_value
  #  status = "In Progress"  # Default status for new tasks

  #  if task_title:
  #      anvil.server.call('create_task', self.project['id'], task_title, description, due_date, assignee, status)
  #      alert("Task created successfully!")
  #  else:
   #     alert("Please enter a task title.")

  