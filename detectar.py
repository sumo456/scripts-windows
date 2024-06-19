import os
import hashlib
import csv
from tqdm import tqdm

def calculate_hash(file_path):
    hash_algo = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_algo.update(chunk)
    return hash_algo.hexdigest()

def find_duplicates(directory):
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_hash = calculate_hash(file_path)
                if file_hash in file_hashes:
                    file_hashes[file_hash].append(file_path)
                else:
                    file_hashes[file_hash] = [file_path]
            except Exception as e:
                print(f"Could not hash file {file_path}: {e}")
    return file_hashes

def write_duplicates_to_csv(duplicates, output_file):
    with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Hash', 'FilePath', 'FileName']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for hash_value, file_paths in duplicates.items():
            if len(file_paths) > 1:
                for file_path in file_paths:
                    file_name = os.path.basename(file_path)
                    writer.writerow({'Hash': hash_value, 'FilePath': file_path, 'FileName': file_name})

def main():
    directory = r"C:\Users\dsalvador\PLIMON GLOBAL , SLU\Europe Vegetable Oils, SL - Finanzas"
    output_file = r"C:\Users\dsalvador\OneDrive - PLIMON GLOBAL , SLU\Europe Vegetable Oils, SL - Finanzas.csv"

    print("Scanning directory for duplicates...")
    file_hashes = find_duplicates(directory)

    duplicates = {hash_value: paths for hash_value, paths in file_hashes.items() if len(paths) > 1}

    if duplicates:
        print("Writing duplicates to CSV...")
        write_duplicates_to_csv(duplicates, output_file)
        print(f"Duplicates have been written to {output_file}")
    else:
        print("No duplicates found.")

if __name__ == "__main__":
    main()
