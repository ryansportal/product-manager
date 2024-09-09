from ._anvil_designer import TaskCreationFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class TaskCreationForm(TaskCreationFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def task_status_dropdown_change(self, **event_args):
    task_id = self.item['id']
    new_status = self.status_dropdown.selected_value
    anvil.server.call('update_task_status', task_id, new_status)