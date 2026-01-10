# https://www.fesliyanstudios.com/soundeffects-download.php?id=7431
from playsound import playsound
import time
import  os
from playsound import playsound


CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0
    
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        
        time_left =seconds - time_elapsed 
        minutes_left = time_left //60 # 125 //60   2
        seconds_left = time_left % 60
        
        print(f"{CLEAR_AND_RETURN}Alarm will sound in : "
              f"{minutes_left:02d}:{seconds_left:02d}"
              )    #02d mean 2 digit outcomes
    sound_path = os.path.join(os.path.dirname(__file__), "alarm.mp3")



    playsound(sound_path)

minutes = int(input("How many minutes to wait: ")) 
seconds = int(input("How many seconds to wait: "))  
total_seconds = minutes * 60 + seconds 
alarm(total_seconds)        

