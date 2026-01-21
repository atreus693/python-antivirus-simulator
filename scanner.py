# scanner.py
import os
import logging
from hasher import hash_file
from db_handler import is_malware_hash
from quarantine import move_to_quarantine

def scan_folder(folder):
    """
    Recursively scan the given folder for malicious files.
    For each file, compute its hash and compare to the signature DB.
    If matched, log a warning and quarantine the file.
    """
    for root, dirs, files in os.walk(folder):  # Recursively traverse directories:contentReference[oaicite:19]{index=19}
        for name in files:
            filepath = os.path.join(root, name)
            try:
                file_hash = hash_file(filepath)
                logging.info(f"Scanned {filepath}  [SHA-256: {file_hash}]")
                if is_malware_hash(file_hash):
                    logging.warning(f"Malicious file detected: {filepath}")
                    move_to_quarantine(filepath)
            except Exception as e:
                logging.error(f"Error scanning {filepath}: {e}")

