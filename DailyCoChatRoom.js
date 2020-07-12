var data = JSON.stringify({
  "properties": {
    "autojoin": false,
    "enable_knocking": true,
    "enable_screenshare": true,
    "enable_chat": true,
    "start_video_off": true,
    "start_audio_off": true,
    "owner_only_broadcast": false,
    "eject_at_room_exp": false,
    "lang": "en"
  },
  "name": "Web Development Chat Room",
  "privacy": "private"
});

var xhr = new XMLHttpRequest();

xhr.addEventListener("readystatechange", function () {
  if (this.readyState === this.DONE) {
    console.log(this.responseText);
  }
});

xhr.open("POST", "https://api.daily.co/v1/rooms");
xhr.setRequestHeader("content-type", "application/json");
xhr.setRequestHeader("authorization", "Bearer e144e63a4f56918684b38f42d5e9807eae1fc50f7bd67cb799691fb7f460087b");

xhr.send(data);
