import os
import shutil

FOLDER_PATH = os.getcwd()  # use the current working directory as the folder path

# Define the file types and their corresponding extensions
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp",".ico"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx",".exe"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Archives": [".zip", ".rar", ".tar", ".gz",".winmd"],
    "Scripts": [".js", ".html", ".css"],
    "Others": [],
}

# Create folders for each file type if they don't exist
for folder in FILE_TYPES.keys():
    folder_path = os.path.join(FOLDER_PATH, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# organize files in the folder based on their extensions
for filename in os.listdir(FOLDER_PATH):
    file_path = os.path.join(FOLDER_PATH, filename)

    # skip folder
    if os.path.isdir(file_path):
        continue

    # get the file extension
    file_extension = os.path.splitext(filename)[1].lower()

    for folder, extensions in FILE_TYPES.items():
        if file_extension in extensions:
            shutil.move(file_path, os.path.join(FOLDER_PATH, folder, filename))
            break

print("Files oraganized successfully!")