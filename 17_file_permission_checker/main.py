# 17_folder_permission/main.py
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent

def permission_checker(path: Path):
    """Check file permissions recursively for all files in the folder."""
    total_items = 0
    readable_count = 0
    writable_count = 0
    executable_count = 0

    try:
        for file in path.rglob("*"):
            if file.is_file():
                total_items += 1
                readable = os.access(file, os.R_OK)
                writable = os.access(file, os.W_OK)
                executable = os.access(file, os.X_OK)

                print("----")
                print(file.relative_to(path))
                print(f"Readable: {'Yes' if readable else 'No'}")
                print(f"Writable: {'Yes' if writable else 'No'}")
                print(f"Executable: {'Yes' if executable else 'No'}\n")

                readable_count += int(readable)
                writable_count += int(writable)
                executable_count += int(executable)
    except Exception as e:
        print(f"Error: {e}")

    # Summary
    print("===== Summary =====")
    print(f"Total files checked: {total_items}")
    print(f"Readable files: {readable_count}")
    print(f"Writable files: {writable_count}")
    print(f"Executable files: {executable_count}")
    print("===================")


def main():
    default_folder = BASE_DIR / "input"

    while True:
        print()
        user_path = input("Enter full folder path to check permissions (or 'q' to quit): ").strip()
        print()

        if user_path.lower() == 'q':
            print("Exiting Folder Permission Checker...")
            break

        path = Path(user_path) if user_path else default_folder

        if not path.is_dir():
            print(f"Folder not found: {path}. Please enter a valid folder path.")
            continue

        print(f"Folder exists: {path}")
        permission_checker(path)


if __name__ == "__main__":
    main()