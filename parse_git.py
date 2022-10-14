# Imports
import shutil
from pathlib import Path
from configparser import ConfigParser

# Setup
settings = ConfigParser()
settings.read('settings.ini')

# Data
LocalDirectory = settings.get('Config', 'local') # Directory of your server
ParseDirectory = settings.get('Config', 'github') # Should be Github in documents by default

# Validate
if not Path(LocalDirectory).is_dir(): raise ValueError("Local directory not found!")
if not Path(ParseDirectory).is_dir(): raise ValueError("Parse directory not found!")

# Handler
Handle = []

# Fill
for directory in Path(ParseDirectory).glob('*'):
    # Validate
    if directory.is_dir():
        Handle.append(directory.name) # Figure out which ones we will need to delete and copy

# Log
Message = "Directories for copying: %d" % len(Handle)

print(Message)

# Actions
for folder in Handle:
    # Directories
    directory = Path(LocalDirectory + "/" + folder)
    remote = Path(ParseDirectory + "/" + folder)

    # Delete
    if directory.exists():
        # Log
        Message = "Deleting directory %s" % directory.name

        print(Message)

        # Remove
        shutil.rmtree(directory)        

    # Copy from remote folder to local
    shutil.copytree(remote, directory)

    # Log
    Message = "Remote %s -> Local" % directory.name

    print(Message)
