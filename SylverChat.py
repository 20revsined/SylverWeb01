from ._anvil_designer import SylverChatTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..SylverLogin import SylverLogin
from ..SylverMovies import SylverMovies
from ..SylverVideoCall import SylverVideoCall
#import anvil.http
#import webbrowser

login = SylverLogin()
movies = SylverMovies()
VideoCall = SylverVideoCall()

class SylverChat(SylverChatTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    
    
    SylverLogin.button_1_click(login, **properties)
    
    
  
  def GetKey(self, x):
    for key, value in TicketList.items():
      if x == value:
        return key
    return "Key not found."
  
  def IsValidUser(self, x):
    for y in app_tables.users.search(tables.order_by("email")):
      if x == y:
        return y

    return "User doesn't exist."

  def ReceiveMessage(self, talker):
    app_tables.chat.add_row(RowNumber = len(app_tables.chat.search()) + 1, User = talker, ChatMessage = self.text_box_1.text)
    print(app_tables.chat.get(RowNumber = len(app_tables.chat.search()))['User'] + ": " + app_tables.chat.get(RowNumber = len(app_tables.chat.search()))['ChatMessage'] + "\n")

    

  def text_box_1_pressed_enter(self, **event_args):
    user = str(anvil.users.get_user()['email'])
    message = self.text_box_1.text
    pass
  
    for y in app_tables.chat.search():
      if y['User'] is not anvil.users.get_user()['email']:
        self.ReceiveMessage(y['User'])
        break
    
    app_tables.chat.add_row(RowNumber = len(app_tables.chat.search()) + 1, User = user, ChatMessage = self.text_box_1.text)
    
    print(anvil.users.get_user()['email'] + ": " + app_tables.chat.get(RowNumber = len(app_tables.chat.search()))['ChatMessage'] + "\n")
    #print(app_tables.chat.get(len(app_tables.chat.search()))['User'] + ": " + app_tables.chat.get(len(app_tables.chat.search()))['ChatMessage'] + "\n")
    
    self.text_box_1.text = ""
    #self.ReceiveMessage(user)    


    
    return message
 
  #create a chat
  def button_1_click(self, **event_args):
    ChatPassword = str(input("Please enter a password, so other users can join your chat.\n"))
    number = int(input("Please enter the number of users you want to invite.\n"))
    x = 0
    
    LoggedInUser = anvil.users.get_user()
    
    
    while x < number:
      user = str(input("Please enter the email of each user you want to invite.\n"))
      check = app_tables.users.get(email = user)['email']
      
      if user == LoggedInUser['email']:
        print("You cannot invite yourself to your own chat room.")
        
      elif not user == LoggedInUser['email'] and user == check:
        app_tables.invites.add_row(ChatKey = ChatPassword, host = LoggedInUser['email'], invitees = user)
        print("User successfully added!\n")
        x = x + 1
        
      elif not user == LoggedInUser['email'] and check == "User doesn't exist.":
        print("This user does not exist. Please enter an email associated with an existing user.\n")
    pass

  #join a chat
  def button_2_click(self, **event_args):
    user = str(input("Please enter the user's email who is hosting the chat.\n"))
    password = str(input("Please enter a password, so you can join a chat.\n"))
    
    if app_tables.invites.get(host = user) and app_tables.invites.get(ChatKey = password):
      print("User's email and password have been accepted! Welcome to " + user + "'s chat!\n")
      LoggedInUser = anvil.users.get_user()
      print(LoggedInUser['email'] + " has entered the chat. Welcome, " + LoggedInUser['email'] + "!\n")
        
      
    else:
      print("User's email and/or password are not correct. Please try again.\n")   
      pass
    

  #enables a user to view their pending invites
  def button_3_click(self, **event_args):
    for x in app_tables.invites.search():
      print("host(s): " + x['host'] + "\n")
      print("invitee(s): " + x['invitees'] + "\n")
      print("password(s): " + x['ChatKey'] + "\n")
    pass
  
  #video chat
  def button_4_click(self, **event_args):
    #SylverVideoCall.CreateVideoCall()
    SylverVideoCall.MakeVideoCall(VideoCall)
    pass




#sources: https://anvil.works/forum/t/is-there-a-way-i-can-move-copy-entire-forms-and-modules-from-project-to-project/196,
#https://anvil.works/forum/t/efficiently-passing-information-from-one-form-to-another/3537, https://anvil.works/docs/users/quickstart-login,
#https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/, https://anvil.works/docs/data-tables,
#https://levelup.gitconnected.com/learn-python-by-building-a-multi-user-group-chat-gui-application-af3fa1017689, https://www.youtube.com/watch?v=oiPGkgHAO5Y,
#https://anvil.works/forum/t/commenting-system-in-anvil/1900/3, https://anvil.works/learn/tutorials/multi-user-apps/chapter-3, https://anvil.works/forum/t/facebook-like-chat/2729,
#https://www.geeksforgeeks.org/python-string-replace/, https://anvil.works/docs/server

