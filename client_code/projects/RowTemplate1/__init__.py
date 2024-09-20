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

    
  def text_box_project_name_show(self, **event_args):
    self.text_box_project_name.text = str(self.item['project_name'])
  def text_box_project_description_show(self, **event_args):
    self.text_box_project_description.text = str(self.item['description'])     
  def assignee_drop_down_show(self, **event_args):
        users_list = anvil.server.call('get_user_names')
        self.assignee_drop_down.items = [(user['name'], user['name']) for user in users_list]
      
        # Check if self.item['assignee'] is a list
        if isinstance(self.item['assignee'], list) and len(self.item['assignee']) > 0:
            # If it's a list, access the first item (assuming it holds a user row)
            assignee_row = self.item['assignee'][0]
            self.assignee_drop_down.selected_value = assignee_row['name']
        elif isinstance(self.item['assignee'], tables.Row):
            # If it's a single row, directly access the 'name' field
            self.assignee_drop_down.selected_value = self.item['assignee']['name']

# This function is called when the data for this row is set
  def item_load(self):
        # self.item refers to the current project's data (automatically set by the repeating panel)
    self.text_box_1.text = str(self.item['project_name'])
    self.project_description_label.text = str(self.item['description'])
   
  def view_project_click(self, **event_args):
        # Get the current row's project (self.item refers to the current row data)
        project = self.item
        
        # Open the ProjectDetailForm and pass the project data to it
        open_form('ProjectDetailForm', project=project)

  def auto_save(self):
        try:
            # Ensure the item has an ID and other required fields
            updated_project = self.item
            if updated_project and 'id' in updated_project:
                anvil.server.call('update_project',
                                  updated_project['id'],
                                  updated_project.get('project_name', ''),
                                  updated_project.get('description', ''),  
                                  updated_project.get('assignee', ''))
        except Exception as e:
            print(f"Error during auto-save: {e}")

  def text_box_project_name_lost_focus(self, **event_args):
        # Update project name when user edits the name field
        if self.item:
            self.item['project_name'] = self.text_box_project_name.text
            self.auto_save()
  def text_box_project_name_pressed_enter(self, **event_args):
        # Update project name when user edits the name field
        if self.item:
            self.item['project_name'] = self.text_box_project_name.text
            self.auto_save()

  def text_box_project_description_lost_focus(self, **event_args):
        # Update project description when user edits the description field
        if self.item:
            self.item['description'] = self.text_box_project_description.text
            self.auto_save()
  def text_box_project_description_pressed_enter(self, **event_args):
          # Update project desc when user edits the name field
        if self.item:
            self.item['description'] = self.text_box_project_description.text
            self.auto_save()

  def assignee_drop_down_change(self, **event_args):
# Get the new selected assignee name
    new_assignee_name = self.assignee_drop_down.selected_value
# Call the server function to get the user row by name
    new_assignee_row = anvil.server.call('get_user_by_name', new_assignee_name)
    if new_assignee_row:
# Update the current item's assignee with the new user row
        self.item['assignee'] = [new_assignee_row]
# Save the change to the server
        self.auto_save()










  