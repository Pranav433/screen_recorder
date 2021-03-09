from threading import Thread
from screen_recorder import Recorder
import time
rec = Recorder() 
def record():
    rec.record_screen()  # this will start the recording
    print(rec.get_screenshot())

def stop(): # This is stop the recording after 30 seconds considering it takes 0 seconds inside the loop
    i=0
    while True:
        time.sleep(1)
        if i == 30:
            rec.stop()
            rec.save("recording.mp4")
            break
        i+=1
record_thread = Thread(target=record)
stop_thread = Thread(target=stop)
record_thread.start()
stop_thread.start()