import os
import time
import shutil

from pathlib import Path
from watchdog.events import FileSystemEventHandler
from extensions import extension_paths

def rename_file(source: Path, dest_path: Path):
    
    if Path(dest_path / source.name).exists():
        i = 0

        while True:
            i+=1
            new_name = dest_path / f'{source.stem}_{i}{source.suffix}'

            if not new_name.exists():
                return new_name
    
    else :
        return dest_path/source.name  
    
class myHandler(FileSystemEventHandler):

    def __init__(self, sourcePath, destPath):
        self.sourcePath = Path(sourcePath).resolve()
        self.destPath = Path(destPath).resolve()


    def on_modified(self, event):
        for newFile in self.sourcePath.iterdir():
            if newFile.is_file():
                destination = self.destPath / extension_paths[newFile.suffix.lower()]
                destination = rename_file(source = newFile, dest_path = destination)
                shutil.move(src = newFile, dst =destination)
                print('File was modified at %s'% event.src_path)
              
  

 

