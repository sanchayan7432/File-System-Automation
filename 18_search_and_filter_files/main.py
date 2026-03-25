# 18_search_filter/main.py
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def option_fileext(path: Path):
    """Filter files by extension"""
    while True:
        ext = input("Enter extension (example: .py) (or 'q' to go back): ").strip()
        if ext.lower() == "q":
            print("Going back...\n")
            break
        if not ext:
            print("Default '.py' extension used")
            ext = ".py"

        matched = {f.relative_to(path): f.stat().st_size for f in path.rglob("*") if f.is_file() and f.suffix == ext}
        print(f"Total matched files: {len(matched)}")
        for f, size in matched.items():
            print(f"File: {f} - Size: {size} bytes")
        print()

def option_filename(path: Path):
    """Search files by name"""
    while True:
        name = input("Enter file name (example: main.py) (or 'q' to go back): ").strip()
        if name.lower() == "q":
            print("Going back...\n")
            break
        if not name:
            print("Default 'main.py' used")
            name = "main.py"

        matched = {f.relative_to(path): f.stat().st_size for f in path.rglob("*") if f.is_file() and f.name == name}
        print(f"Total matched files: {len(matched)}")
        for f, size in matched.items():
            print(f"File: {f} - Size: {size} bytes")
        print()

def option_filesize(path: Path):
    """Filter files by max size in KB"""
    while True:
        size_input = input("Enter max file size in KB (example: 150) (or 'q' to go back): ").strip()
        if size_input.lower() == "q":
            print("Going back...\n")
            break
        max_size = int(size_input) * 1024 if size_input else 300 * 1024
        if not size_input:
            print("Default 300 KB used")

        matched = {f.relative_to(path): f.stat().st_size for f in path.rglob("*") if f.is_file() and f.stat().st_size <= max_size}
        print(f"Total matched files: {len(matched)}")
        for f, size in matched.items():
            print(f"File: {f} - Size: {size} bytes")
        print()

def option_filecontent(path: Path):
    """Search text inside files"""
    while True:
        text = input("Enter text to search inside files (or 'q' to go back): ").strip()
        if text.lower() == "q":
            print("Going back...\n")
            break
        if not text:
            print("Default text used: 'Welcome to the system'")
            text = "Welcome to the system"

        matched = {}
        for f in path.rglob("*"):
            if f.is_file():
                try:
                    with f.open("r", encoding="utf-8") as file:
                        if text in file.read():
                            matched[f.relative_to(path)] = f.stat().st_size
                except:
                    continue

        print(f"Total matched files: {len(matched)}")
        for f, size in matched.items():
            print(f"File: {f} - Size: {size} bytes")
        print()

def search_and_filter(path: Path):
    """Main menu for search/filter operations"""
    while True:
        choice = input(
            "Choose filter type:\n"
            "1 - Filter by extension\n"
            "2 - Search by file name\n"
            "3 - Filter by max size (KB)\n"
            "4 - Search inside file content\n"
            ": (or 'q' to go back): "
        ).strip()
        if choice.lower() == "q":
            print("Going back...\n")
            break

        try:
            choice = int(choice)
            if choice == 1:
                option_fileext(path)
            elif choice == 2:
                option_filename(path)
            elif choice == 3:
                option_filesize(path)
            elif choice == 4:
                option_filecontent(path)
            else:
                print("Invalid choice\n")
        except Exception as e:
            print(f"Error: {e}\n")

def main():
    default_folder = BASE_DIR / "input"
    while True:
        user_path = input("Enter full folder path (or 'q' to quit): ").strip()
        if user_path.lower() == "q":
            print("Exiting Folder Search & Filter...")
            break

        path = Path(user_path) if user_path else default_folder
        if not path.is_dir():
            print(f"Folder not found: {path}")
            continue

        print(f"Folder exists: {path}")
        search_and_filter(path)

if __name__ == "__main__":
    main()