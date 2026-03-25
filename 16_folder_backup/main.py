# 16_folder_backup/main.py
from pathlib import Path
import shutil, time
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent

def backup(path: Path):
    """Back up all contents of the folder to backup/ in BASE_DIR."""
    output_dir = BASE_DIR / "backup"

    if output_dir.exists():
        confirm = input("Backup folder exists. Delete and continue? (y/n): ").lower()
        if confirm != "y":
            print("Cancelled.")
            return
        shutil.rmtree(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    total_items = 0
    copied_items = 0

    start_time = time.time()

    for item in path.rglob("*"):
        total_items += 1
        relative_path = item.relative_to(path)
        target = output_dir / relative_path

        try:
            if item.is_dir():
                target.mkdir(parents=True, exist_ok=True)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, target)
            copied_items += 1
        except Exception as e:
            print(f"Error copying {item}: {e}")

    elapsed = time.time() - start_time

    print(f"\nTotal items found: {total_items}")
    print(f"Items copied: {copied_items}")
    print(f"Backup completed in {elapsed:.2f} seconds")
    print(f"Backup date: {datetime.today().date()}")


def main():
    default_folder = BASE_DIR / "input"

    while True:
        print()
        user_path = input("Enter full folder path to back up (or 'q' to quit): ").strip()
        print()

        if user_path.lower() == 'q':
            print("Exiting Folder Backup...")
            break

        path = Path(user_path) if user_path else default_folder

        if not path.is_dir():
            print(f"Folder not found: {path}. Please enter a valid folder path.")
            continue

        print(f"Folder exists: {path}")
        backup(path)


if __name__ == "__main__":
    main()