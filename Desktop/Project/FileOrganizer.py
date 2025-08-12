import os
import shutil
import json

def load_categories(file_path):
    """Load categories from a JSON file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Categories file not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_category(extension, categories):
    """Return the category for a given file extension."""
    for cat, exts in categories.items():
        if extension in exts:
            return cat
    return "Others"

def organize_files(folder_path, categories, simulate):
    """Organize files into category folders."""
    counts = {cat: 0 for cat in categories}
    counts["Others"] = 0

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if not os.path.isfile(file_path):
            continue

        extension = os.path.splitext(file_name)[1].lower()
        category = get_category(extension, categories)
        category_folder = os.path.join(folder_path, category)

        if simulate:
            print(f"[SIMULATE] Would move '{file_name}' → '{category}/'")
        else:
            os.makedirs(category_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(category_folder, file_name))
            print(f"Moved '{file_name}' → '{category}/'")

        counts[category] += 1

    return counts

def print_summary(counts):
    """Print a summary of moved files."""
    print("\nSummary:")
    for cat, count in counts.items():
        print(f"{cat}: {count}")

# --- Main Program ---
if __name__ == "__main__":
    folder_path = input("Please type in the full path of the folder containing your files: ")
    simulate_input = input("Do you want to run in simulate mode? (yes/no): ").strip().lower()
    simulate = (simulate_input == "yes")

    categories = load_categories("categories.json")
    counts = organize_files(folder_path, categories, simulate)
    print_summary(counts)

