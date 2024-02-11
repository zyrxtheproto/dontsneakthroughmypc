import requests
import datetime
import time
from colorama import Fore, Style, init
import os

init(autoreset=True)

def send_push_notification(api_key, title, body):
    url = "https://api.pushbullet.com/v2/pushes"
    headers = {
        "Access-Token": api_key,
        "Content-Type": "application/json"
    }

    # Get current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Include the date in the body of the notification
    body = f"{body} - {current_date}"

    data = {
        "type": "note",
        "title": title,
        "body": body
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("1")
    else:
      log_file_name = f"log_{datetime.datetime.now().strftime('%Y-%m-%d')}.txt"
      log_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), log_file_name)
      with open(log_file_path, "a", encoding="utf-8") as log_file: 
          log_file.write(f"Error: {response.text}\n")


message = """
                          ████████                          
                        ██        ██                        
                      ██            ██                      Warning - This program is made to prevent people
                      ██            ██                      who shouldn't be using your computer from using it.
                    ██    ████████    ██                    
                  ██    ████████████    ██                  
                  ██    ████████████    ██                  
                ██      ████████████      ██                
              ██          ████████          ██              
              ██          ████████          ██              If you're right here, it means that you really shouldn't
            ██            ████████            ██            continue using this computer, as everything you do is being
          ██                ████                ██          monitored and will be reported to the owner of the computer.
          ██                ████                ██          
        ██                                        ██        
      ██                    ████                    ██      
      ██                  ████████                  ██      
    ██                  ████████████                  ██    Goodbye, and just shut down the computer...
  ██                    ████████████                    ██  
  ██                      ████████                      ██  
  ██                        ████                        ██  
    ██                                                ██    
      ████████████████████████████████████████████████    
"""
time.sleep(2)
print(Fore.YELLOW + message)


api_key = "InsertYourAPIKeyHere"
send_push_notification(api_key, "Notification", "PC Started!")

# wait until program is closed, if it isn't it will send a notification every 5 minutes
while True:
    time.sleep(300)
    send_push_notification(api_key, "Notification", "PC still Running!")