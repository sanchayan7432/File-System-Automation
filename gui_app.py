from pathlib import Path
import subprocess
import sys

# Base directory
BASE_DIR = Path(r"D:\AutomationScripting\file-system-automation")

# Utility mapping
utilities = {
    1: ("JSON to CSV Converter", BASE_DIR / "01_json_to_csv" / "main.py"),
    2: ("XML to JSON Converter", BASE_DIR / "02_xml_to_json" / "main.py"),
    3: ("Merge CSV Files", BASE_DIR / "03_merge_csv_files" / "main.py"),
    4: ("Split Text File by Lines", BASE_DIR / "04_split_file_by_lines" / "main.py"),
    5: ("Text File Analysis", BASE_DIR / "05_text_file_analysis" / "main.py"),
    6: ("File System Organizer", BASE_DIR / "06_organize_file_system" / "main.py"),
    7: ("Duplicate Files Remover", BASE_DIR / "07_duplicate_files_remover" / "main.py"),
    8: ("Split Folders into Subfolders", BASE_DIR / "08_split_folders_into_subfolders" / "main.py"),
    9: ("Compress Files & Folders", BASE_DIR / "09_compress_files_and_folders" / "main.py"),
    10: ("Zip File Extractor", BASE_DIR / "10_zip_file_extractor" / "main.py"),
    11: ("Rename Files in Bulk", BASE_DIR / "11_rename_files_in_bulk" / "main.py"),
    12: ("Find and Replace in Text Files", BASE_DIR / "12_find_and_replace_in_text_files" / "main.py"),
    13: ("Folder Size Analyzer", BASE_DIR / "13_folder_size_analyzer" / "main.py"),
    14: ("Remove Empty Files & Folders", BASE_DIR / "14_remove_empty_files_and_folders" / "main.py"),
    15: ("Folder Monitor", BASE_DIR / "15_monitor_folder_for_changes" / "main.py"),
    16: ("Folder Backup", BASE_DIR / "16_folder_backup" / "main.py"),
    17: ("File Permission Checker", BASE_DIR / "17_file_permission_checker" / "main.py"),
    18: ("Search and Filter Files", BASE_DIR / "18_search_and_filter_files" / "main.py"),
    19: ("Image to PDF Converter", BASE_DIR / "19_img_to_pdf_converter" / "main.py"),
    20: ("PDF Merger", BASE_DIR / "20_pdf_merger" / "main.py"),
    21: ("PDF Splitter", BASE_DIR / "21_pdf_splitter" / "main.py"),
    22: ("OCR Extractor", BASE_DIR / "22_img_text_extractor" / "main.py"),
    23: ("PDF Watermark", BASE_DIR / "23_pdf_watermark_adder" / "main.py"),
    24: ("Document Size Manager", BASE_DIR / "24_document_size_manager" / "main.py"),
    25: ("PDF ↔ Word Converter", BASE_DIR / "25_pdf_vs_word" / "main.py"),
}


# ================= RUN FUNCTION =================
def run_utility(choice: int):
    """Run selected utility safely"""
    if choice not in utilities:
        print("❌ Invalid utility number")
        return

    desc, script_path = utilities[choice]

    if not script_path.exists():
        print(f"❌ Script not found: {script_path}")
        return

    print(f"\n🚀 Running: {desc}\n")

    try:
        subprocess.run(
            [sys.executable, str(script_path)],
            cwd=script_path.parent,   # 🔥 VERY IMPORTANT FIX
        )
    except Exception as e:
        print(f"❌ Error running utility: {e}")


# ================= CLI MENU =================
def interactive_menu():
    while True:
        print("\n=== Universal File System Automation Suite ===\n")

        for key, (desc, _) in utilities.items():
            print(f"{key}. {desc}")

        print("q. Quit")

        choice = input("\nSelect utility number: ").strip()

        if choice.lower() == "q":
            print("👋 Exiting...")
            break

        try:
            run_utility(int(choice))
        except ValueError:
            print("❌ Enter a valid number")


# ================= ENTRY POINT =================
if __name__ == "__main__":
    # 🔥 GUI MODE (argument passed)
    if len(sys.argv) > 1:
        try:
            run_utility(int(sys.argv[1]))
        except ValueError:
            print("❌ Invalid argument. Use a number.")
    else:
        # CLI fallback
        interactive_menu()