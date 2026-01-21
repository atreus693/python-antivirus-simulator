# db_handler.py
import json
import os

DB_FILE = 'signatures.json'

def load_signatures(db_file=DB_FILE):
    """
    Load the signature database from a JSON file.
    Returns a dictionary with key 'signatures' mapping to a list of hashes.
    If the file does not exist, creates an empty list.
    """
    if not os.path.exists(db_file):
        # If database file doesn't exist, initialize with empty list
        return {'signatures': []}
    with open(db_file, 'r') as f:
        data = json.load(f)  # Parse JSON into Python dict:contentReference[oaicite:15]{index=15}
    return data

def save_signatures(data, db_file=DB_FILE):
    """
    Save the signature dictionary back to the JSON file.
    """
    with open(db_file, 'w') as f:
        json.dump(data, f, indent=4)  # Write dict to JSON file:contentReference[oaicite:16]{index=16}

def add_signature(hash_value, db_file=DB_FILE):
    """
    Add a new hash to the signature database if it is not already present.
    Returns True if added, False if it was already in the database.
    """
    data = load_signatures(db_file)
    if hash_value in data['signatures']:
        return False
    data['signatures'].append(hash_value)
    save_signatures(data, db_file)
    return True

def remove_signature(hash_value, db_file=DB_FILE):
    """
    Remove a hash from the signature database.
    Returns True if removed, False if it was not found.
    """
    data = load_signatures(db_file)
    if hash_value not in data['signatures']:
        return False
    data['signatures'].remove(hash_value)
    save_signatures(data, db_file)
    return True

def is_malware_hash(hash_value, data=None):
    """
    Check if the given hash is in the signature database.
    Returns True if the hash is found (malicious), False otherwise.
    """
    if data is None:
        data = load_signatures()
    return hash_value in data.get('signatures', [])

