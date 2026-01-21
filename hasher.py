# hasher.py
import hashlib

def hash_file(filepath):
    """
    Compute and return the SHA-256 hash of the file at 'filepath'.
    Reads the file in chunks to handle large files efficiently.
    """
    sha256 = hashlib.sha256()  # Create a new SHA-256 hash object:contentReference[oaicite:12]{index=12}
    with open(filepath, 'rb') as f:
        # Read the file in 8KB chunks
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            sha256.update(chunk)
    # Return the hexadecimal digest (64 hex characters)
    return sha256.hexdigest()

