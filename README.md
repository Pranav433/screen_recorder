# screen_recoder

[![PyPI version](https://badge.fury.io/py/screen_recorder.svg)](https://badge.fury.io/py/screen_recorder)


This is a simple python package for recording your screen on WINDOWS

``NOTE :- don't install it in other OS``

## Key features
* simple
* Fast
* efficient

## Installing

```
pip install screen_recorder
```

**OR**

```
git clone space
cd screen_recorder
pip install .
```
## Dependencies
* cffi==1.14.5
* ffmpeg-python==0.2.0
* future==0.18.2
* MouseInfo==0.1.3
* numpy==1.20.1
* opencv-python==4.5.1.48
* Pillow==8.1.2
* PyAutoGUI==0.9.52
* pycparser==2.20
* PyGetWindow==0.0.9
* PyMsgBox==1.0.9
* pyperclip==1.8.2
* PyRect==0.1.4
* PyScreeze==0.1.26
* PyTweening==1.0.3
* sounddevice==0.4.1
* SoundFile==0.10.3.post1

## Example
you have to use [threading](https://realpython.com/intro-to-python-threading/) for this module to work
```python
from threading import Thread
from screen_recorder import Recorder
import time
rec = Recorder() 
def record():
    rec.record_screen()  # This will start the recording
    print(rec.get_screenshot())

def stop(): # This will stop the recording after 30 seconds considering it takes 0 seconds inside the loop
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
```
## Links
* [github](https://github.com/Pranav433/screen_recorder)
* [package]()
