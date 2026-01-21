
import argparse
import logging
from db_handler import add_signature, remove_signature
from scanner import scan_folder

def main():
    parser = argparse.ArgumentParser(
        description="Simple Python Antivirus Simulator (educational use only)"
    )
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Scan command
    scan_parser = subparsers.add_parser('scan', help='Scan a folder for malware')
    scan_parser.add_argument('folder', help='Path to the folder to scan')

    # Add signature command
    add_parser = subparsers.add_parser('add', help='Add a hash to the signature database')
    add_parser.add_argument('hash', help='SHA-256 hash to add')

    # Remove signature command
    remove_parser = subparsers.add_parser('remove', help='Remove a hash from the signature database')
    remove_parser.add_argument('hash', help='SHA-256 hash to remove')

    args = parser.parse_args()

    # Basic logging configuration: INFO and above will be shown on the console
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    if args.command == 'scan':
        logging.info(f"Starting scan of folder: {args.folder}")
        scan_folder(args.folder)
    elif args.command == 'add':
        success = add_signature(args.hash)
        if success:
            print(f"Added {args.hash} to signature database.")
        else:
            print(f"Hash {args.hash} is already in the database.")
    elif args.command == 'remove':
        success = remove_signature(args.hash)
        if success:
            print(f"Removed {args.hash} from signature database.")
        else:
            print(f"Hash {args.hash} was not found in the database.")

if __name__ == "__main__":
    main()

