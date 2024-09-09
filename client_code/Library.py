import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello()
#

#users is a list of tuples: [(email, name), (email, name)...]
user_emails, user_colors = anvil.server.call('get_user_emails_and_colors')

column_types = ['Text', 'Checkbox', 'Priority', 'Users']

priority_items = ['Low', 'Medium', 'High']

priority_colors = {
      'Low': '#2DAF88',
      'Medium': '#F6CA57',
      'High': '#D64045'
    }
