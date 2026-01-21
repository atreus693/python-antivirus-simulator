# quarantine.py
import os
import shutil

QUARANTINE_DIR = 'quarantine'

def move_to_quarantine(filepath, quarantine_dir=QUARANTINE_DIR):
    """
    Move the given file to the quarantine directory.
    Creates the directory if it does not exist.
    """
    os.makedirs(quarantine_dir, exist_ok=True)  # Ensure quarantine folder exists
    filename = os.path.basename(filepath)
    destination = os.path.join(quarantine_dir, filename)
    shutil.move(filepath, destination)  # Move the file into quarantine

