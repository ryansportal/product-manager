from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

# This function is called when the data for this row is set
    def item_load(self):
        # self.item refers to the current project's data (automatically set by the repeating panel)
       self.project_name_label.text = str(self.item['project_name'])
       self.project_description_label.text = str(self.item['description'])
       self.due_date_label.text = str(self.item['due_date'])
       self.drop_down_1.text = str(self.item['assignee'])

  def view_project_click(self, **event_args):
        # Get the current row's project (self.item refers to the current row data)
        project = self.item
        
        # Open the ProjectDetailForm and pass the project data to it
        open_form('ProjectDetailForm', project=project)
