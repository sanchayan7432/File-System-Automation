# 14_remove_empty_files_and_folders/main.py
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def remove_empty(path: Path):
    """Remove empty files and empty folders recursively"""
    empty_files = 0
    empty_folders = 0

    # 1️⃣ Remove empty files
    files = [f for f in path.rglob("*") if f.is_file()]
    for file in sorted(files, key=lambda f: f.name.lower()):
        if file.stat().st_size == 0:
            file.unlink()
            print(f"Removed empty file: {file.relative_to(BASE_DIR)}")
            empty_files += 1

    # 2️⃣ Remove empty folders (bottom-up)
    folders = [f for f in path.rglob("*") if f.is_dir()]
    for folder in sorted(folders, key=lambda f: len(f.parts), reverse=True):
        if not any(folder.iterdir()):
            folder.rmdir()
            print(f"Removed empty folder: {folder.relative_to(BASE_DIR)}")
            empty_folders += 1

    print(f"\nTotal files checked: {len(files)}")
    print(f"Empty files removed: {empty_files}")
    print(f"Empty folders removed: {empty_folders}")


def main():
    default_folder = BASE_DIR / "input"

    while True:
        print()
        confirm = input(
            "This will remove empty files & folders inside the 'input' folder. Continue? (y/n or 'q' to quit): "
        ).lower()
        print()

        if confirm == 'q':
            print("Exiting Remove Empty Files & Folders...")
            break
        elif confirm == 'n':
            print("Operation cancelled.")
            break
        elif confirm == 'y':
            if default_folder.is_dir():
                print(f"Folder exists: {default_folder}")
                try:
                    remove_empty(default_folder)
                except Exception as e:
                    print(f"Error: {e}")
                    continue
            else:
                print("Input folder is missing.")
                break
        else:
            print("Please choose a valid option (y/n/q).")


if __name__ == "__main__":
    main()