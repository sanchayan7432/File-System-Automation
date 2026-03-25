# 12_find_and_replace_in_text_files/main.py
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def line_based_edit(data, path):
    """Allow editing specific lines in a text file"""
    for i, line in enumerate(data, start=1):
        print(f"{i}: {line.strip()}")

    while True:
        choice = input("Enter line number to edit (or 'q' to go back): ").strip()
        if choice.lower() == "q":
            print("Going back to main menu...")
            break
        if not choice.isdigit():
            print("Invalid input.")
            continue

        index = int(choice) - 1
        if index < 0 or index >= len(data):
            print("Invalid line number.")
            continue

        print(f"Current text: {data[index].strip()}")
        new_text = input("Enter new text: ")
        data[index] = new_text + "\n"

        with open(path, "w", encoding="utf-8") as f:
            f.writelines(data)

        print(f"Line {index+1} updated successfully.")


def word_based_edit(data, path):
    """Allow replacing all occurrences of a word"""
    for line in data:
        print(line.strip())

    while True:
        word = input("Enter word to find (or 'q' to go back): ").strip()
        if word.lower() == "q":
            print("Going back to main menu...")
            break

        count = sum(line.count(word) for line in data)
        if count == 0:
            print("Word not found in file.")
            continue

        print(f"{count} occurrence(s) found.")
        new_word = input("Enter new word to replace with: ")

        new_data = [line.replace(word, new_word) for line in data]

        with open(path, "w", encoding="utf-8") as f:
            f.writelines(new_data)

        print("All occurrences replaced successfully.")
        break


def replace_text(file, path):
    data = file.readlines()

    while True:
        choice = input("Enter 1 for Line-based editing, 2 for Word-based editing: ").strip()
        if choice in ["1", "2"]:
            break
        print("Invalid choice. Enter 1 or 2.")

    if choice == "1":
        line_based_edit(data, path)
    else:
        word_based_edit(data, path)


def main():
    default_file = BASE_DIR / "input" / "data.txt"

    while True:
        print()
        user_path = input("Enter full file path (or 'q' to quit): ").strip()
        print()

        if user_path.lower() == "q":
            print("Exiting Find and Replace project...")
            break

        path = Path(user_path) if user_path else default_file
        if not path.is_file():
            print("Invalid file or file not found.")
            continue
        if path.suffix != ".txt":
            print("Only .txt files are allowed.")
            continue

        try:
            with path.open("r", encoding="utf-8") as file:
                print(f"File loaded successfully: {path.name}")
                replace_text(file, path)
        except Exception as e:
            print(f"Failed to open file: {e}")


if __name__ == "__main__":
    main()