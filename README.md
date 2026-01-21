# Python CLI Antivirus Simulator (Educational)

This Python project simulates a simple signature-based antivirus engine. It is intended for **educational use only**, to help beginners learn how antivirus scanning and signature databases work. **Do not use this for real malware protection**. It is not a substitute for real security software.

## Features

- **Folder Scanning:** Recursively scans a specified directory for files.  
- **Hashing:** Computes SHA-256 hash of each file using Python’s `hashlib`:contentReference[oaicite:27]{index=27}.  
- **Signature Database:** Compares file hashes against a JSON database of known malware signatures. The database is easy to update (add/remove hashes).  
- **Quarantine:** Malicious files (hash matches) are flagged and moved to a `quarantine/` folder.  
- **CLI Interface:** Run from the command line to `scan` directories and `add`/`remove` signatures. Uses `argparse` for user-friendly commands.  
- **Logging:** Basic logging is implemented (e.g. INFO logs for scanned files, WARNING for detections).



