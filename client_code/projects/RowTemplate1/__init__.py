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
 

    # Any code you write here will run before the form opens.
  def text_box_project_name_show(self, **event_args):
    self.text_box_project_name.text = str(self.item['project_name'])
    
  def text_box_project_description_show(self, **event_args):
    self.text_box_project_description.text = str(self.item['description'])

  def drop_down_1_show(self, **event_args):
# Ensure 'in_progress' value is one of the dropdown items
    in_progress_value = self.item['in_progress']
    if in_progress_value in self.drop_down_1.items:
        self.drop_down_1.selected_value = in_progress_value
      
# This function is called when the data for this row is set
  def item_load(self):
        # self.item refers to the current project's data (automatically set by the repeating panel)
    self.text_box_1.text = str(self.item['project_name'])
    self.project_description_label.text = str(self.item['description'])
    self.drop_down_1.text = str(self.item['in_progress'])


  def view_project_click(self, **event_args):
        # Get the current row's project (self.item refers to the current row data)
        project = self.item
        
        # Open the ProjectDetailForm and pass the project data to it
        open_form('ProjectDetailForm_copy', project=project)


  def auto_save(self):
        try:
            # Ensure the item has an ID and other required fields
            updated_project = self.item
            if updated_project and 'id' in updated_project:
                anvil.server.call('update_project',
                                  updated_project['id'],
                                  updated_project.get('project_name', ''),
                                  updated_project.get('description', ''),
                                  updated_project.get('in_progress', ''))
        except Exception as e:
            print(f"Error during auto-save: {e}")

  def text_box_project_name_lost_focus(self, **event_args):
        # Update project name when user edits the name field
        if self.item:
            self.item['project_name'] = self.text_box_project_name.text
            self.auto_save()

  def text_box_project_description_lost_focus(self, **event_args):
        # Update project description when user edits the description field
        if self.item:
            self.item['description'] = self.text_box_project_description.text
            self.auto_save()

  def drop_down_1_change(self, **event_args):
 # Update project in_progress when user selects an option in the dropdown
        if self.item:
            self.item['in_progress'] = self.drop_down_1.selected_value
            self.auto_save()


  