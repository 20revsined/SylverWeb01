import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import requests

@anvil.server.callable
def CreateVideoCall(MaxPeople, IsChatEnabled, name, PublicOrPrivate):
  
  #MaxPeople = 2
  #PublicOrPrivate = "private"
  #IsChatEnabled = "true"
  #name = "TestRun"
  
  url = "https://api.daily.co/v1/rooms/"
  url2 = str("https://sylverteam.daily.co/" + str(name))
      
  information = "{\"properties\":{\"max_participants\":%d,\"autojoin\":false,\"enable_knocking\":true,\"enable_screenshare\":true,\"enable_chat\":%s,\"start_video_off\":true,\"start_audio_off\":true,\"owner_only_broadcast\":false},\"name\":\"%s\",\"privacy\":\"%s\"}" % (float(MaxPeople), IsChatEnabled, name, PublicOrPrivate)
  #information = "{\"properties\":{\"max_participants\":2,\"autojoin\":false,\"enable_knocking\":true,\"enable_screenshare\":true,\"enable_chat\":true,\"start_video_off\":true,\"start_audio_off\":true,\"owner_only_broadcast\":false},\"name\":\"test\",\"privacy\":\"private\"}"
  headers = {
    'content-type': "application/json",
    'authorization': "Bearer e144e63a4f56918684b38f42d5e9807eae1fc50f7bd67cb799691fb7f460087b"
  }

  response = requests.request("POST", url, data=information, headers=headers)

  #print(response.text)
  
  print("Here is your video chat room url: " + url2 + "\n")
      
  #webbrowser.open(url2)
  
#sources: https://stackoverflow.com/questions/1841565/valueerror-invalid-literal-for-int-with-base-10, https://python-forum.io/Thread-Python-redirect-users-to-another-url-after-form-post
