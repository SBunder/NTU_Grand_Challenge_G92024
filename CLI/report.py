import os
import csv
import shutil
import zipfile
zname = ""
def new(name, age):
    # Create the user's folder if it doesn't exist
    user_folder = os.path.join("users", "Current_User")
    global zname
    zname = f"{name}_{age}"
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)
    else:
        # If the folder exists, wipe its contents
        for filename in os.listdir(user_folder):
            file_path = os.path.join(user_folder, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

    # Create a CSV file with the provided name and age
    csv_name = f"{name}_{age}.csv"
    csv_path = os.path.join(user_folder, csv_name)
    with open(csv_path, "w", newline="") as csvfile:
        fieldnames = ["Name", "Age", "AHR", "ASPO2", "ABT", "Photos","PhotoAnalyst", "severity", "email"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        # Write two rows
        writer.writerow({"Name": "", "Age": "", "AHR": "", "ASPO2": "", "ABT": "", "Photos": "", "PhotoAnalyst": "", "severity": "", "email": ""})


def add2report(column, data):
    # Append data to the specified column in the CSV file
    user_folder = os.path.join("users", "Current_User")
    csv_files = [f for f in os.listdir(user_folder) if f.endswith(".csv")]
    if not csv_files:
        print("No CSV file found.")
        return
    csv_path = os.path.join(user_folder, csv_files[0])  # Assuming only one CSV file exists
    
    # Read existing rows from the CSV file
    rows = []
    fieldnames = []
    if os.path.exists(csv_path):
        with open(csv_path, "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            fieldnames = reader.fieldnames
            for row in reader:
                rows.append(row)
    
    # Check if row 2 exists, if not, generate one
    if len(rows) < 2:
        if not fieldnames:
            print("CSV file is empty. Generating fieldnames.")
            fieldnames = ["Name", "Age", "AHR", "ASPO2", "ABT", "Photos","PhotoAnalyst", "severity", "email"]
        new_row = {field: "" for field in fieldnames}
        rows.append(new_row)
    
    # Update data in row 2 of the rows list
    rows[1][column] = data
    
    # Write the updated rows back to the CSV file
    with open(csv_path, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print("Data added to row 2 of CSV file:", data)  # Print debug message





def packreport():
    # Compress everything in the user's folder into a zip file
    user_folder = os.path.join("users", "Current_User")
    global zname
    zipname = zname + ".zip"
    zip_name = os.path.join("users", zipname)
    with zipfile.ZipFile(zip_name, "w") as zipf:
        for root, dirs, files in os.walk(user_folder):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, user_folder)
                zipf.write(file_path, arcname=arcname)

