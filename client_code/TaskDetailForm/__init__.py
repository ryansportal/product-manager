from ._anvil_designer import TaskDetailFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class TaskDetailForm(TaskDetailFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def new_task_click(self, **event_args):
    task_title = self.task_title_textbox.text
    description = self.task_description_textbox.text
    due_date = self.due_date_picker.date
    assignee = self.assignee_dropdown.selected_value
    status = "In Progress"  # Default status for new tasks

    if task_title:
        anvil.server.call('create_task', self.project['id'], task_title, description, due_date, assignee, status)
        alert("Task created successfully!")
    else:
        alert("Please enter a task title.")

  