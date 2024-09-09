import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.


#Users
@anvil.server.callable
def check_user():
  user = anvil.users.get_user()
  if user is None:
    raise anvil.users.AuthenticationFailed('user not logged in')

#data tables
@anvil.server.callable
def add_column_to_db(column_name, project, type):
    #project is a row from the Projects Data Table
    #add a new row to the Columns Data Table  
  column_row = app_tables.columns.add_row(title=column_name, type=type)
   #link the new column to Projects
  project['columns'] += [column_row]
  return column_row