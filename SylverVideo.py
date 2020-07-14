from ._anvil_designer import SylverVideoCallTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import webbrowser
import requests

class SylverVideoCall(SylverVideoCallTemplate):
  def __init__(self, **properties):
   
    self.init_components(**properties)
  
  def IsPublic(self):
    response = str(input("Do you want your video call to be public or private?"))
    if response == "public":
      response = "public"
      return response
    
    elif response == "private":
      response = "private"
      return response
  
  def MaxParticipants(self):
    maximum = int(input("Please enter the maximum number of people you would like to have in your video call."))
    
    if maximum > 200:
      maximum = 200
    
    return maximum
  
  def ChatEnabled(self):
    question = str(input("Would you like to enable a chat in your video call?"))
    
    if question == "yes":
      chat = "true"
    
    elif question == "no":
      chat = "false"
     
    return chat
  
  def VideoCallName(self):
    name = str(input("Please name your video call."))
  
    return name
  
  def CreateVideoCall(self):
    
    MaxPeople = self.MaxParticipants()
    IsChatEnabled = self.ChatEnabled()
    CallName = self.VideoCallName()
    public = self.IsPublic()
    url = "https://api.daily.co/v1/rooms/"
    url2 = str("https://sylverteam.daily.co/" + CallName)
    
    information = "{\"properties\":{\"max_participants\":%s,\"autojoin\":false,\"enable_knocking\":true,\"enable_screenshare\":true,\"enable_chat\":%s,\"start_video_off\":true,\"start_audio_off\":true,\"owner_only_broadcast\":false},\"name\":\"%s\",\"privacy\":\"%s\"}" % (str(MaxPeople), IsChatEnabled, CallName, public)
    headers = {
    'content-type': "application/json",
    'authorization': "Bearer e144e63a4f56918684b38f42d5e9807eae1fc50f7bd67cb799691fb7f460087b"
    }

    response = requests.request("POST", url, data=information, headers=headers)
    
    webbrowser.open(url2)
    
#source: https://docs.daily.co/reference#create-room, https://stackoverflow.com/questions/38380462/syntaxerror-unexpected-token-o-in-json-at-position-1/38380728, https://docs.daily.co/reference#set-room-configuration
