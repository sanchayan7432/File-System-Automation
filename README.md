# File & Folder Automation

## Description

This repository presents a comprehensive Python-based File System Automation Suite designed to simplify and automate a wide range of everyday tasks involving files, folders, and documents. The project contains 25 standalone utilities, each implemented as an independent Python module, that demonstrate practical techniques for handling file operations such as reading, writing, converting, organizing, analyzing, monitoring, and managing files across a directory structure. The goal of this repository is to provide a hands-on learning resource and a practical toolkit for developers, students, and automation enthusiasts who want to understand how Python can be used to solve real-world file management problems efficiently.

The project covers multiple categories of file system automation. It begins with data format conversion utilities that transform files between formats such as JSON, XML, CSV, PDF, and Word documents. It also includes text processing and analysis tools that help analyze textual content, perform bulk edits, and extract useful information from files. Several utilities focus on file organization and cleanup, enabling users to automatically organize files by type, remove duplicate files, delete empty folders, and manage folder structures in a systematic way. Additionally, the repository includes compression, extraction, and backup tools that help manage storage and maintain safe copies of important files.

Beyond basic file operations, the project introduces more advanced automation utilities such as real-time folder monitoring, permission checking, search and filtering systems, document processing, image-to-text extraction, PDF manipulation, and file size management. These tools demonstrate how Python can interact with different file formats and system-level operations to build efficient automation pipelines. Each utility follows a consistent structure with dedicated input and output directories, making it easy to test, modify, and integrate into larger workflows.

Every project in the repository is designed to be simple, modular, and easy to understand, allowing learners to explore the implementation details without unnecessary complexity. At the same time, the collection demonstrates practical real-world applications of Python file system programming, including automation workflows commonly used in data processing, document handling, and system maintenance tasks. By studying and running these scripts, users can gain valuable experience with Python libraries for file manipulation, directory management, and document processing while also building a versatile toolkit that can be adapted to their own automation needs.



## Projects

01. **[JSON to CSV Converter](01_json_to_csv/)** - A Python script that converts JSON files into CSV format.  
02. **[XML to JSON Converter](02_xml_to_json/)** - A Python script that converts XML files into JSON format.  
03. **[Merge CSV Files](03_merge_csv_files/)** - A Python script that merges multiple CSV files in a folder into a single CSV file.  
04. **[Split Text File by Lines](04_split_file_by_lines/)** - A Python script that splits a .txt file into multiple smaller text files based on a user-defined number of lines per file.  
05. **[Text File Analysis](05_text_file_analysis/)** - A Python script that analyzes a .txt file and provides basic statistics such as word count, line count, and character count.  
06. **[File System Organizer](06_organize_file_system/)** - A Python script that organizes files from a folder into a clean `output/` directory based on file type.  
07. **[Duplicate Files Remover](07_duplicate_files_remover/)** - A Python script that scans a folder for duplicate files based on content and moves duplicates to a separate `output/` folder.  
08. **[Split Folders into Subfolders](08_split_folders_into_subfolders/)** - A Python script that takes all files from a folder (including nested files) and splits them into multiple subfolders in the `output/` folder.  
09. **[Compress Files & Folders](09_compress_files_and_folders/)** - A Python script that compresses a file or an entire folder into a ZIP archive.  
10. **[Zip File Extractor](10_zip_file_extractor/)** - A Python script that extracts a ZIP file into the `output/` folder.  
11. **[Rename Files in Bulk](11_rename_files_in_bulk/)** - A Python script that renames all files inside the `input/` folder automatically.  
12. **[Find and Replace in Text Files](12_find_and_replace_in_text_files/)** - A Python script that allows a user to edit text files using line-based or word-based find and replace operations.  
13. **[Folder Size Analyzer](13_folder_size_analyzer/)** - A Python script that analyzes the total size and number of files in a folder including all nested files and directories.  
14. **[Remove Empty Files & Folders](14_remove_empty_files_and_folders/)** - A Python script that cleans up a folder by removing all empty files and folders including empty subfolders.  
15. **[Folder Monitor](15_monitor_folder_for_changes/)** - A Python script that monitors a folder and displays file changes in real time.  
16. **[Folder Backup](16_folder_backup/)** - A Python script that creates a full backup of a folder into a backup directory.  
17. **[File Permission Checker](17_file_permission_checker/)** - A Python script that checks file permissions inside a folder and reports access details.  
18. **[Search and Filter Files](18_search_and_filter_files/)** - A Python script that allows you to search and filter files in a folder using different conditions such as name, extension, and size.  
19. **[Image to PDF Converter](19_image_to_pdf/)** - A Python script that converts one or multiple image files into a single PDF document.  
20. **[PDF Merger (PDF + Images)](20_pdf_merger/)** - A Python script that merges multiple PDF files and images into a single PDF document.  
21. **[PDF Splitter & Extractor](21_pdf_splitter/)** - A Python script that can split a PDF into multiple PDFs by page ranges or extract pages as images.  
22. **[Image Text Extractor](22_img_text_extractor/)** - A Python script that extracts text from images using Optical Character Recognition (OCR).  
23. **[PDF Watermark Adder](23_pdf_watermark_adder/)** - A Python script that adds a watermark to every page of a PDF document.  
24. **[Document Size Manager](24_document_size_manager/)** - A Python script that can compress or enlarge the size and quality of documents or images while displaying file size before and after processing.  
25. **[PDF ↔ Word Converter](25_pdf_vs_word/)** - A Python script that converts PDF files to DOCX and DOCX files to PDF.  
## How to Use

### 1. Clone the repository using the command:
   ```bash
   git clone https://github.com/<repo name>
   ```

### 2. Open any project folder and read its README.md file for detailed instructions.

### 3. Run the script:
```
python main.py
```


