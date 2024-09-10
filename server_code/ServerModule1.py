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


#Create project
@anvil.server.callable
def create_project(name, description, due_date):
     # Add a new row to the projects table
    project_row = app_tables.projects.add_row(
        project_name=name, 
        description=description, 
        due_date=due_date
    )
    # Get the unique ID assigned by Anvil
    project_id = project_row.get_id()
    return project_id


#Display all projects
@anvil.server.callable
def get_all_projects():
    return app_tables.projects.search()
#Update Projects
@anvil.server.callable
def update_project(project_id, name, description):
    # Fetch the project from the database using its ID
    project = app_tables.projects.get(id=project_id)
    
    # If the project exists, update its fields
    if project:
        project['project_name'] = name
        project['description'] = description
        return True
    return False

#Get Tasks for specific project
@anvil.server.callable
def get_tasks_for_project(project_id):
    return app_tables.tasks.search(project_id=project_id)