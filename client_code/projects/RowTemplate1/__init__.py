from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import anvil.tables as tables
from anvil.tables import app_tables

class RowTemplate1(RowTemplate1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Call the server function to get the list of user rows (not just names)
        users = anvil.server.call('get_user_names')
        
        # Populate the dropdown with (display_name, user_row) pairs
        self.assignee_drop_down.items = [(user['name'], user) for user in users]

    def text_box_project_name_show(self, **event_args):
        self.text_box_project_name.text = str(self.item['project_name'])

    def text_box_project_description_show(self, **event_args):
        self.text_box_project_description.text = str(self.item['description'])

    def assignee_drop_down_show(self, **event_args):
        # Set the dropdown's selected value to the current assignee (which is a list of rows)
        if self.item['assignee']:
            # Assuming single assignee, set selected_value to the first assignee row
            assignee_row = self.text['assignee']
            self.assignee_drop_down.selected_value = assignee_row

    def item_load(self):
        # This function is called when the data for this row is set
        self.text_box_1.text = str(self.item['project_name'])
        self.project_description_label.text = str(self.item['description'])

        # Set the dropdown value based on the current assignee
        if self.item['assignee']:
            assignee_row = self.text['assignee']
            self.assignee_drop_down.selected_value = assignee_row

    def assignee_drop_down_change(self, **event_args):
        # Update the assignee field with the selected user row from the dropdown
        self.text = self.assignee_drop_down.selected_value
     #   if self.item:
      #      selected_user_row = self.assignee_drop_down.selected_value  # This will be the user row
      #      self.item['assignee'] = [selected_user_row]  # Assign the selected row as a list
        self.auto_save()

    def auto_save(self):
        try:
            # Ensure the item has an ID and other required fields
            updated_project = self.item
            if updated_project and 'id' in updated_project:
                anvil.server.call('update_project',
                                  updated_project['id'],
                                  updated_project.get('project_name', ''),
                                  updated_project.get('description', ''),
                                  updated_project.get('assignee', []))  # Assignee should be a list of rows
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

  #  def view_project_click(self, **event_args):
        