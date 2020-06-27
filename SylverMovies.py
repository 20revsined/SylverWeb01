from ._anvil_designer import SylverMoviesTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..SylverLogin import SylverLogin

login = SylverLogin()

#if any boolean below is true, then the user can access content via the service
#they log in to

NetflixLoggedIn = False
HuluLoggedIn = False
AmazonVideoLoggedIn = False
DisneyPlusLoggedIn = False

class SylverMovies(SylverMoviesTemplate):
  def __init__(self, **properties):

    self.init_components(**properties)

  #watching via Netflix
  def button_1_click(self, **event_args):
    
    pass

  #watching via Hulu
  def button_2_click(self, **event_args):
    
    pass

  #watching via Amazon Video
  def button_3_click(self, **event_args):
    
    pass

  #watching via Disney+
  def button_4_click(self, **event_args):
    
    pass



#source: https://stackoverflow.com/questions/5216128/log-into-website-specifically-netflix-with-python
