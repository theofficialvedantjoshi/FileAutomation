#importing required modules
import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

#All the paths needed
path = 'C://Users//xxxxx//Downloads'
vid = 'C://Users//xxxxx//Downloads//VIDEOS'
img = 'C://Users//xxxxx//Downloads//IMAGES'
exe = 'C://Users//xxxxx//Downloads//APPS'
doc = 'C://Users//xxxxx//Downloads//DOCS'

#setting up watch dog
patterns = ["*"]
ignore_patterns = None
ignore_directories = False
case_sensitive = True
my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
#moving file on modification
def on_modified(event):
    dir = os.listdir(path)
    for file in dir:
        src_path = os.path.join(path, file)
        if (file.split('.'))[-1] == 'exe':
            dst_path = os.path.join(exe, file)
            shutil.move(src_path, dst_path)
        elif (file.split('.'))[-1] == 'pdf':
            dst_path = os.path.join(doc, file)
            shutil.move(src_path, dst_path)
        elif (file.split('.'))[-1] == 'png' or (file.split('.'))[-1] == 'jpg' or (file.split('.'))[-1] == 'jpeg':
            dst_path = os.path.join(img, file)
            shutil.move(src_path, dst_path)
        elif (file.split('.'))[-1] == 'mp4':
            dst_path = os.path.join(vid, file)
            shutil.move(src_path, dst_path)
#initializing the observer
my_event_handler.on_modified = on_modified
pathc = "C://Users//xxxxx//Downloads"
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, pathc, recursive=go_recursively)
my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
