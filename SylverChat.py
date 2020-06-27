from ._anvil_designer import SylverChatTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..SylverLogin import SylverLogin
from ..SylverMovies import SylverMovies

login = SylverLogin()
movies = SylverMovies()
TicketList = {}

class SylverChat(SylverChatTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    
    SylverLogin.button_1_click(login, **properties)
  
  def GetKey(self, x):
    for key, value in TicketList.items():
      if x == value:
        return key
    return "Key not found." 
  

  def text_box_1_pressed_enter(self, **event_args):
    user = str(anvil.users.get_user(allow_remembered = True)['email'])
    print(user + ": ")
    message = str(input(self.text_box_1.text))
    print("\n")
    pass
    return message

  #create a chat
  def button_1_click(self, **event_args):
    password = str(input("Please enter a password, so other users can join your chat.\n"))
    number = int(input("Please enter the number of users you want to invite.\n"))
    x = 0
    
    while x < number:
      user = str(input("Please enter the email of each user you want to invite.\n"))
      if anvil.users.get_user()['email'] == user:
        TicketList.update({user: password})
        print("User successfully added!\n")
        x = x + 1
      
      else:
        print("This user does not exist. Please enter an email associated with an existing user.\n")
    pass

  #join a chat
  def button_2_click(self, **event_args):
    user = str(input("Please enter the user's email who is hosting the chat.\n"))
    password = str(input("Please enter a password, so you can join a chat.\n"))
    
    if user == SylverChat.GetKey(self, TicketList[user]) and password == TicketList[user]:
      print("User's email and password have been accepted! Welcome to " + user + "'s chat!\n")
      pass
    
    else:
      print("User's email and/or password are not correct. Please try again.\n")

  #enables a user to view their pending invites
  def button_3_click(self, **event_args):
    print(TicketList)
    pass



#sources: https://anvil.works/forum/t/is-there-a-way-i-can-move-copy-entire-forms-and-modules-from-project-to-project/196,
#https://anvil.works/forum/t/efficiently-passing-information-from-one-form-to-another/3537, https://anvil.works/docs/users/quickstart-login,
#https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/

