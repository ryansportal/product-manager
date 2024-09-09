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


#PM - Create a new task
@anvil.server.callable
def create_task(project_id, title, description, due_date, assignee_email):
    project = app_tables.projects.get_by_id(project_id)
    assignee = app_tables.users.get(email=assignee_email)
    
    new_task = app_tables.tasks.add_row(
        title=title,
        description=description,
        due_date=due_date,
        project=project,
        assignee=assignee,
        status=status
      
 

#PM - Update task status

##@anvil.server.callable
def update_task_status(task_id, status):
    task = app_tables.tasks.get_by_id(task_id)
    task.update(status=status)

#PM - Assign users
##@anvil.server.callable
def assign_task_to_user(task_id, user_email):
    user = app_tables.users.get(email=user_email)
    task = app_tables.tasks.get_by_id(task_id)
    task.update(assignee=user)

### Add a comment
@anvil.server.callable
def add_comment(task_id, comment_text):
    task = app_tables.tasks.get_by_id(task_id)
    app_tables.comments.add_row(task=task, comment_text=comment_text)


#add project
@anvil.server.callable
def create_project(name, description, due_date):
    app_tables.projects.add_row(name=name, description=description, due_date=due_date)
