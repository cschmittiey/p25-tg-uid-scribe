import csv
import os
import re

# Define filenames for the CSVs
talkgroup_csv = 'talkgroups.csv'
unitid_csv = 'unitids.csv'

# Check if CSV files exist and create them if they do not, with headers
def initialize_csvs():
    if not os.path.isfile(talkgroup_csv):
        with open(talkgroup_csv, 'w', newline='') as tgfile:
            writer = csv.writer(tgfile)
            writer.writerow(["TalkGroup ID", "Name"])
    
    if not os.path.isfile(unitid_csv):
        with open(unitid_csv, 'w', newline='') as uidfile:
            writer = csv.writer(uidfile)
            writer.writerow(["Unit ID", "Name"])

def record_entry(entry_type, entry_id, name):
    filename = talkgroup_csv if entry_type == 'tg' else unitid_csv
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([entry_id, name])

# Regex patterns for parsing tg, uid and the associated name
tg_pattern = re.compile(r'\btg\s+(\d+)', re.IGNORECASE)
uid_pattern = re.compile(r'\buid\s+(\d+)', re.IGNORECASE)

def extract_data(input_str):
    entry_type = "tg" if "tg" in input_str else "uid"
    id_pattern = tg_pattern if entry_type == "tg" else uid_pattern
    id_match = id_pattern.search(input_str)
    name = id_pattern.sub("", input_str).strip()  # Remove the ID part, remaining part is the name
    return entry_type, id_match.group(1), name

def process_input(user_input):
    entry_type, entry_id, name = extract_data(user_input)
    if entry_id and name:
        record_entry(entry_type, entry_id, name)
        print(f"{entry_type.upper()} ID {entry_id} with name '{name}' recorded successfully!")
    else:
        print("Invalid input format. Try again.")

def main():
    initialize_csvs()
    print("Welcome to the Talkgroup and Unit ID Interface.")
    print("Type 'exit' to quit. Input data in any order, for example: '12345 tg fireground ops'.")

    while True:
        user_input = input("Enter your data: ").strip()
        if user_input == 'exit':
            break
        process_input(user_input)

if __name__ == "__main__":
    main()
