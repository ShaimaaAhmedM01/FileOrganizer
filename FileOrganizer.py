import os 
import shutil

# Ask the user for the folder path
folder_path = input("Please type in the full path of the folder containing your files:    ")
print(f"You entered: {folder_path}")

# Ask the user if they want to simulate
simulate_input = input("Do you want to run in simulate mode? (yes/no): ").strip().lower()
simulate = (simulate_input == "yes")  # True if 'yes', False otherwise

if simulate:
    print("Simulation mode ON — No files will be moved.")
else:
    print("Simulation mode OFF — Files will be moved.")

# Define the categories and their extensions
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".odt", ".txt", ".rtf", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".flv", ".wmv", ".webm"],
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z", ".bz2"],
    "Code": [".py", ".js", ".java", ".c", ".cpp", ".cs", ".rb", ".go", ".php", ".html", ".css", ".ts"],
}

# Dictionary to keep track of file counts per category
counts = {cat: 0 for cat in CATEGORIES}  # start all counts at 0
counts["Others"] = 0  # also track "Others"

# Look at all files in the folder
for file_name in os.listdir(folder_path):
  file_path = os.path.join(folder_path, file_name)
  print(folder_path,file_name)
  print(file_name)

  # Skip if it's not a file 
  if not os.path.isfile(file_path):
    continue

  """ Split the file name into (base_name, extension), [1] is the extension
    check the uppercase of characters for ex. JPG is same as jpg """
  extension = os.path.splitext(file_name)[1].lower() 
  print(extension)

  # Find which category this file belongs to
  found_category = None 
  for cat, exts in CATEGORIES.items():
    if extension in exts: 
      found_category = cat 
      break
  print(found_category)

  # If category not found, put into "Others"
  if found_category is None:
        found_category = "Others"

  # Create category folder if it doesn't exist
  category_folder = os.path.join(folder_path,found_category)
  # Simulate or move
  if simulate:
      print(f"[SIMULATE] Would move '{file_name}' → '{found_category}/'")
  else:
      if not os.path.exists(category_folder):
          os.makedirs(category_folder)
      # Move file to folder based on category
      shutil.move(file_path, os.path.join(category_folder, file_name))
      print(f"Moved '{file_name}' → '{found_category}/'")

  # count the new of files moved based on each category 
  counts[found_category] += 1

print("\nSummary:")
for cat, count in counts.items():
    print(f"{cat}: {count}")




