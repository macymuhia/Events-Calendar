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

def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("Select A to Add, U to Update, V to View, D to Delete or X to Exit: ").upper()
    
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print "Calendar empty."
      else:
        print calendar
    
    elif user_choice == "U":
      date = raw_input("What date? ")
      update = raw_input("Enter the update: ")
      calendar[date] = update
      print ("Update successful!")
      print calendar
      
    elif user_choice == "A":
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if (len(date) > 10 or int(date[6:10]) < int(strftime("%Y"))):
        print "invalid date"
        date = raw_input("Enter date (MM/DD/YYYY): ")
        try_again = raw_input("Try again? Y for Yes, N for No: ").upper()
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print ("Event added successfully!")
        print calendar
    elif user_choice == "D":
      if len(calendar.keys()) < 1:
        print ("Calendar is empty!")
      else:
        event = raw_input("What event? ")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print ("Event successfully deleted! ")
            print calendar
            
          else:
            print ("Incorrect event specified! ")
            
    elif user_choice == "X":
      start = False
      
    else:
      print ("Invalid command entered! ")
      start = False
            
start_calendar()