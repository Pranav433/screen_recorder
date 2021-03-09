from pyautogui import screenshot
import cv2 
from os import mkdir,listdir,getcwd
import numpy as np
from threading import Thread
class Video:
    filename = getcwd() + "/tmp/{}.avi"
    fps = 60.0
    def __init__(self,unique_id):
        self.unique_id = unique_id
        self.resolution = (1920, 1080)
        self.codec = cv2.VideoWriter_fourcc(*"XVID") 
        print(self.filename.format(self.unique_id))
        self.vw = cv2.VideoWriter(self.filename.format(self.unique_id), self.codec, self.fps, self.resolution)
    def _record_video(self):
        self.record = True
        while True:
            if not self.record:
                break
            img = screenshot() 
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            for i in range(0,5):
                self.vw.write(frame)
            
        self.vw.release()
    def get_screenshot(self):
        return screenshot()
