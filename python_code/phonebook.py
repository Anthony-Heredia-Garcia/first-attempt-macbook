import csv

with open("/Users/tonydacoder/Downloads/Phonebook - Sheet1.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Name"], row['Phone Number'])