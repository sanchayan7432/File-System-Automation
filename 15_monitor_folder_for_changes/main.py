# 15_folder_monitor/main.py
from pathlib import Path
import time
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

BASE_DIR = Path(__file__).resolve().parent

class FolderEventHandler(FileSystemEventHandler):
    """Handles file system events and prints them to console."""

    def on_created(self, event):
        print(f"[CREATED] {event.src_path}")

    def on_deleted(self, event):
        print(f"[DELETED] {event.src_path}")

    def on_modified(self, event):
        # Avoid repeated messages for directory metadata changes
        if not event.is_directory:
            print(f"[MODIFIED] {event.src_path}")

    def on_moved(self, event):
        print(f"[MOVED] from {event.src_path} → {event.dest_path}")

def monitor_folder(path_to_watch: Path):
    """Start monitoring the given folder for changes."""
    try:
        event_handler = FolderEventHandler()
        observer = Observer()
        observer.schedule(event_handler, path=str(path_to_watch), recursive=True)
        observer.start()
        print(f"\nMonitoring started on: {path_to_watch}")
        print("Press Ctrl+C to stop.\n")

        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopping monitoring...")
        observer.stop()
    except FileNotFoundError:
        print(f"Error: The folder '{path_to_watch}' does not exist.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

    observer.join()

def main():
    default_folder = BASE_DIR / "input"

    while True:
        print()
        user_path = input("Enter full folder path to monitor (or 'q' to quit): ").strip()
        print()

        if user_path.lower() == 'q':
            print("Exiting Folder Monitor...")
            break

        path = Path(user_path) if user_path else default_folder

        if not path.is_dir():
            print(f"Folder not found: {path}. Please enter a valid folder path.")
            continue

        print(f"Folder exists: {path}")
        monitor_folder(path)

if __name__ == "__main__":
    main()