import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import open_form
from anvil import *
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello()
#



def Startup():
  try:
    user = anvil.server.call('check_user')
    print(user)
    open_form('Home')
    
  except anvil.users.AccountIsNotEnabled as e:
    # must be this way round since AccountIsNotEnabled is a subclass of AuthenticationFailes
    print(e)
    open_form('Login')
  except anvil.users.AuthenticationFailed as e:
    print(e)
    open_form('Login')
  
if __name__ == "__main__":
  Startup()
  
