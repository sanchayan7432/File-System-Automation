# 09_compress_files_and_folders/main.py
from pathlib import Path
import shutil

BASE_DIR = Path(__file__).resolve().parent

def compress(path):
    """Compress a file or folder into a ZIP archive inside output/"""
    output_dir = BASE_DIR / "output"

    if output_dir.exists():
        confirm = input("Output folder exists. Delete and continue? (y/n): ").strip().lower()
        if confirm != "y":
            print("Cancelled.")
            return
        shutil.rmtree(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        archive_path = output_dir / path.stem

        if path.is_dir():
            shutil.make_archive(str(archive_path), "zip", path)
        else:
            shutil.make_archive(
                str(archive_path),
                "zip",
                root_dir=path.parent,
                base_dir=path.name
            )

        print(f"Compressed successfully → {archive_path.with_suffix('.zip')}")

    except Exception as e:
        print(f"Error while compressing: {e}")


def main():
    """Entry point for Compress Files & Folders project"""
    default_folder = BASE_DIR / "input"

    while True:
        print()
        user_path = input("Enter full path of file or folder to compress (Enter for default, 'q' to quit): ").strip()
        print()

        if user_path.lower() == 'q':
            print("Exiting Compress Files & Folders project...")
            break

        if not user_path:
            path = default_folder
            if path.is_dir():
                print(f"No path provided — using default folder: {default_folder}")
            else:
                print("Default folder is missing.")
                continue
        else:
            path = Path(user_path)

        if path.is_dir() or path.is_file():
            try:
                print(f"Path exists: {path}")
                compress(path)
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("404 - Please enter a valid folder or file path.")


if __name__ == "__main__":
    main()