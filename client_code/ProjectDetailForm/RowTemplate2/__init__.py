from ._anvil_designer import RowTemplate2Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowTemplate2(RowTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

     # Manually trigger item_load to ensure it loads when the form opens
    self.item_load()
    
    # Any code you write here will run before the form opens.
  def project_task_name_show(self, **event_args):
      self.project_task_name.text = self.item['project_name_link']['project_name']

    
# This function is called when the data for this row is set
  def item_load(self):
    if self.item:
        # Access the project_name directly using the column name without extra quotes or lists
        self.project_task_name.text = self.item['project_name_link']['project_name']
    else:
        print("No item data found")


