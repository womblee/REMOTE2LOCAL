# Imports
import shutil
from pathlib import Path
from configparser import ConfigParser

# Setup
settings = ConfigParser()
settings.read('settings.ini')

# Data
LocalDirectory = settings.get('Config', 'local') # Directory which will receive an update
ParseDirectory = settings.get('Config', 'remote') # Directory from which to update

# Validate
if not Path(LocalDirectory).is_dir(): raise ValueError("Local directory not found!")
if not Path(ParseDirectory).is_dir(): raise ValueError("Parse directory not found!")

# Handler
Handle = []

# Fill
for directory in Path(ParseDirectory).glob('*'):
    # Validate
    if directory.is_dir():
        remote = Path(LocalDirectory + "/" + directory.name)

        if remote.exists() and remote.is_dir():
            Handle.append(directory.name) # Figure out which ones we will need to delete and copy

# Log
print("Directories for copying: %d" % len(Handle))

# Actions
for folder in Handle:
    # Directories
    directory = Path(LocalDirectory + "/" + folder)
    remote = Path(ParseDirectory + "/" + folder)
    
    # Message
    print(directory.name)

    # Delete
    if directory.exists():
        # Log
        print("/ Deleting")

        # Remove
        shutil.rmtree(directory)        

    # Copy from remote folder to local
    shutil.copytree(remote, directory)

    # Log
    print("/ Moving")
