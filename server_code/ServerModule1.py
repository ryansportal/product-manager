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
    app_tables.projects.add_row(name=name, description=description, due_date=due_date)

#Create task 

@anvil.server.callable
def create_task(project_id, title, description, due_date, assignee_email, status):
    project = app_tables.projects.get_by_id(project_id)
    assignee = app_tables.users.get(email=assignee_email)
    
    app_tables.tasks.add_row(
        title=title, 
        description=description, 
        due_date=due_date,
        project=project, 
        assignee=assignee, 
        status=status
    )

