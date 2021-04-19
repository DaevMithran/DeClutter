import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

 
class OnMyWatch:

    # Directory to watch
    FolderToTrack = "D:/TestFolder"

    # Create an Observer, which is going to monitor the directory
    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = myHandler()
        
        # Link handler and observer class using observer.schedule
        self.observer.schedule(event_handler, path = self.FolderToTrack, recursive = True) #recursive = true makes observer to monitor sub directories 
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()   
    
class myHandler(FileSystemEventHandler):
  
    def on_created(self, event):
        print('File was created at %s'% event.src_path)
        shutil.move(event.src_path, 'D:/Destination')

    def on_deleted(self, event):
        print('File was deleted at %s'% event.src_path)

    # def on_modified(self, event):
    #     print('File was modified at %s'% event.src_path)
              
  
if __name__ == '__main__':
    watch = OnMyWatch()
    watch.run()
 

