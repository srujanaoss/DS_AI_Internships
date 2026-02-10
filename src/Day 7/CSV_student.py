import csv  
with open("Day 6/students.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
