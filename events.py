"""
A calendar that a user can view, add event, update event or delete event
"""
from time import sleep, strftime, gmtime

calendar = {}

def welcome():
  USER_FIRST_NAME = raw_input("What's your name? ")
  print "Welcome %s" % USER_FIRST_NAME
  print "calendar opening . . ."
  sleep(3)
  print strftime("%A, %B %d %Y")
  print strftime("%H:%M:%S")
  sleep(1)
  print "What would you like to do?"

