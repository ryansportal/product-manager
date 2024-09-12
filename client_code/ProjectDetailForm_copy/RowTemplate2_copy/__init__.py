from ._anvil_designer import RowTemplate2_copyTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowTemplate2_copy(RowTemplate2_copyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Manually trigger item_load to ensure it loads when the form opens
    self.item_load()

  # Show editable fields
  def project_task_name_show(self, **event_args):
    self.project_task_name.text = self.item["project_name_link"]["project_name"]

  def task_box_show(self, **event_args):
    self.task_box.text = self.item["task_name"]

  def desc_box_show(self, **event_args):
    self.desc_box.text = self.item["description"]

  def territory_dd_show(self, **event_args):
    # Ensure 'in_progress' value is one of the dropdown items
    territory_value = self.item["territory"]
    if territory_value in self.territory_dd.items:
      self.territory_dd.selected_value = territory_value

  def type_dd_show(self, **event_args):
    type_value = self.item["type"]
    if type_value in self.type_dd.items:
      self.type_dd.selected_value = type_value

  # This function is called when the data for this row is set
  def item_load(self):
    if self.item:
      # Access the project_name directly using the column name without extra quotes or lists
      self.project_task_name.text = self.item["project_name_link"]["project_name"]
    else:
      print("No item data found")

  # Auto Save
  def auto_save(self):
    try:
      # Ensure the item has an ID and other required fields
      updated_item = self.item
      if updated_item and "id" in updated_item:
        anvil.server.call(
          "update_project_task",
          updated_item["id"],
          updated_item.get("project_name_link", {}).get("project_name", ""),
          updated_item.get("task_name", ""),
          updated_item.get("description", ""),
          updated_item.get("territory", ""),
          updated_item.get("type", ""),
        )

    except Exception as e:
      print(f"Error during auto-save: {e}")

  # Lost Focus Update Fields:
  def task_box_lost_focus(self, **event_args):
    # Update project description when user edits the description field
    if self.item:
      self.item["task_name"] = self.task_box.text
      self.auto_save()

  def desc_box_lost_focus(self, **event_args):
    if self.item:
      self.item["description"] = self.desc_box.text
      self.auto_save()

  def territory_dd_change(self, **event_args):
    # Update territory when user selects an option in the dropdown
    if self.item:
      self.item["territory"] = self.territory_dd.selected_value
      self.auto_save()

  def type_dd_change(self, **event_args):
    if self.item:
      self.item["type"] = self.type_dd.selected_value
      self.auto_save()
