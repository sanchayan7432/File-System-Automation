# 11_rename_files_in_bulk/main.py
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def bulk_rename(path):
    """Rename all files inside a folder sequentially (file_1, file_2, ...)"""
    record = 0

    files = sorted([file for file in path.rglob("*") if file.is_file()])

    for file in files:
        record += 1
        old_name = file.name
        new_name = file.with_name(f"file_{record}{file.suffix}")

        if old_name == new_name.name:
            print(f"Skipped (already correct): {old_name}")
            continue

        counter = 1
        while new_name.exists():
            new_name = file.with_name(f"file_{record}_{counter}{file.suffix}")
            counter += 1

        file.rename(new_name)
        print(f"Renamed: {old_name} → {new_name.name}")

    if record == 0:
        print("No files found to rename.")
    else:
        print(f"{record} files processed successfully.")


def main():
    """Entry point for Rename Files in Bulk project"""
    default_folder = BASE_DIR / "input"

    while True:
        print()
        confirm = input("This will rename all files inside the 'input' folder. Continue? (y/n, q to quit): ").strip().lower()
        print()

        if confirm == 'q':
            print("Exiting Rename Files in Bulk project...")
            break

        if confirm == 'n':
            print("Cancelled.")
            break

        if confirm == 'y':
            path = default_folder
            if path.is_dir():
                print(f"Folder exists: {default_folder}")
                try:
                    bulk_rename(path)
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