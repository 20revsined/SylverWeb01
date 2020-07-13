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
      return private
  
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
    url = str("https://sylverteam.daily.co/" + CallName)
    
    information = "{\"properties\":{\"max_participants\":" + str(MaxPeople) + ",\"autojoin\":false,\"enable_knocking\":true,\"enable_screenshare\":true,\"enable_chat\":" + chat + ",\"start_video_off\":true,\"start_audio_off\":true,\"owner_only_broadcast\":false},\"privacy\:" + public + ",\"name\:" + CallName + "}"
    
    payload = information
    headers = {
    'content-type': "application/json",
    'authorization': "Bearer e144e63a4f56918684b38f42d5e9807eae1fc50f7bd67cb799691fb7f460087b"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    
    webbrowser.open(url)
    
#source: https://docs.daily.co/reference#create-room
