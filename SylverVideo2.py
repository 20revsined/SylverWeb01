import requests
import webbrowser

def IsPublic():
    response = str(input("Do you want your video call to be public or private?"))
    if response == "public":
      response = "public"
      return response
      
    elif response == "private":
      response = "private"
    return response
    
def MaxParticipants():
  maximum = int(input("Please enter the maximum number of people you would like to have in your video call."))
      
  if maximum > 200:
    maximum = 200
      
  return maximum
    
def ChatEnabled():
  question = str(input("Would you like to enable a chat in your video call?"))
    
  if question == "yes":
    chat = "true"
      
  elif question == "no":
    chat = "false"
       
  return chat
    
def VideoCallName():
  name = str(input("Please name your video call."))
    
  return name
    
def CreateVideoCall():
      
  MaxPeople = MaxParticipants()
  IsChatEnabled = ChatEnabled()
  CallName = VideoCallName()
  public = IsPublic()
  url = "https://api.daily.co/v1/rooms/"
  url2 = str("https://sylverteam.daily.co/" + CallName)
      
  information = "{\"properties\":{\"max_participants\":%s,\"autojoin\":false,\"enable_knocking\":true,\"enable_screenshare\":true,\"enable_chat\":%s,\"start_video_off\":true,\"start_audio_off\":true,\"owner_only_broadcast\":false},\"name\":\"%s\",\"privacy\":\"%s\"}" % (str(MaxPeople), IsChatEnabled, CallName, public)
  #information = "{\"properties\":{\"max_participants\":2,\"autojoin\":false,\"enable_knocking\":true,\"enable_screenshare\":true,\"enable_chat\":true,\"start_video_off\":true,\"start_audio_off\":true,\"owner_only_broadcast\":false},\"name\":\"test\",\"privacy\":\"private\"}"
  headers = {
    'content-type': "application/json",
    'authorization': "Bearer e144e63a4f56918684b38f42d5e9807eae1fc50f7bd67cb799691fb7f460087b"
  }

  response = requests.request("POST", url, data=information, headers=headers)

  print(response.text)
      
  webbrowser.open(url2)

CreateVideoCall()

#sources: https://stackoverflow.com/questions/38380462/syntaxerror-unexpected-token-o-in-json-at-position-1/38380728, https://docs.daily.co/reference#set-room-configuration, https://docs.daily.co/reference#create-room
