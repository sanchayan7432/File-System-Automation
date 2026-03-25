# 13_folder_size_analyzer/main.py
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def human_readable_size(size_bytes: int):
    """Convert bytes to human-readable format"""
    units = ["Bytes", "KB", "MB", "GB", "TB"]
    index = 0
    size = float(size_bytes)

    while size >= 1024 and index < len(units) - 1:
        size /= 1024
        index += 1

    if index == 0:
        return f"{int(size)} {units[index]}"
    else:
        return f"{size:.2f} {units[index]}"


def analyze_folder(path: Path):
    total_size = 0
    file_count = 0

    for file in path.rglob("*"):
        if file.is_file():
            total_size += file.stat().st_size
            file_count += 1

    print(f"Folder: {path.name}")
    print(f"Total Files: {file_count}")
    print(f"Total Size: {human_readable_size(total_size)}")


def main():
    default_folder = BASE_DIR / "input"

    while True:
        print()
        user_path = input("Enter full folder path (or 'q' to quit): ").strip()
        print()

        if user_path.lower() == "q":
            print("Exiting Folder Size Analyzer...")
            break

        path = Path(user_path) if user_path else default_folder
        if not path.is_dir():
            print("Invalid folder path or folder does not exist.")
            continue

        try:
            print(f"Analyzing folder: {path}")
            analyze_folder(path)
        except Exception as e:
            print(f"Error during analysis: {e}")


if __name__ == "__main__":
    main()