from ._anvil_designer import SylverVideoCallTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import requests

class SylverVideoCall(SylverVideoCallTemplate):
  def __init__(self, **properties):
   
    self.init_components(**properties)
  
  def VideoCall(self):
    url = "https://api.daily.co/v1/rooms"

    payload = "{\"properties\":{\"autojoin\":false,\"enable_knocking\":true,\"enable_screenshare\":true,\"enable_chat\":true,\"start_video_off\":true,\"start_audio_off\":true,\"owner_only_broadcast\":false,\"eject_at_room_exp\":false,\"lang\":\"en\"},\"name\":\"hello\",\"privacy\":\"private\"}"
    headers = {
    'content-type': "application/json",
    'authorization': "Bearer e144e63a4f56918684b38f42d5e9807eae1fc50f7bd67cb799691fb7f460087b"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

#source: https://docs.daily.co/reference#create-room
