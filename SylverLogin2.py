from ._anvil_designer import SylverLoginTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class SylverLogin(SylverLoginTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
  
  def getUsername(self, username, **properties):
    return username

  def getPassword(self, password, **properties):
    return password

  def setPassword(self, p, **properties):
    password = p
   
  def setUsername(self, u, **properties):
    username = u
  
  def main(self):
    anvil.users.login_with_form()
    
  def button_1_click(self, **properties):
    alert(SylverLogin.main(self))
    pass
    return True

#source: https://stackoverflow.com/questions/26784252/non-integer-arg-1-for-randrange-in-python-libary

