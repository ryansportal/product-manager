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
#Front end logic to interact with the backend functions in server

def save_task_click(self, **event_args):
    title = self.title_textbox.text
    description = self.description_textbox.text
    due_date = self.due_date_picker.date
    assignee = self.assignee_dropdown.selected_value

    if title and assignee:
        anvil.server.call('create_task', self.project_id, title, description, due_date, assignee)
        alert("Task Created")
    else:
        alert("Please fill in all required fields.")