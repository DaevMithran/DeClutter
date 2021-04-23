import time
from eventHandler import myHandler
from watchdog.observers import Observer

class OnMyWatch:
    # Create an Observer, which is going to monitor the directory
    def __init__(self):
        self.observer = Observer()

    def run(self, source, dest):
        event_handler = myHandler(sourcePath = source, destPath = dest)
        
        # Link handler and observer class using observer.schedule
        self.observer.schedule(event_handler, path = event_handler.sourcePath, recursive = True) #recursive = true makes observer to monitor sub directories 
        self.observer.start()
        print('Observer activated')
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")
        
        self.observer.join() 

if __name__ == '__main__':
    source = "D:/TestFolder"
    dest = "D:/TestFolder/Destination"
    watch = OnMyWatch()
    watch.run(source, dest)