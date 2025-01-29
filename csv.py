import csv

# Assuming 'data.csv' has headers: name, age, city
with open('data.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"{row['name']} is {row['age']} years old and lives in {row['city']}.")
