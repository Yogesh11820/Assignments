import csv

def read_csv(s):
    with open(s,'r') as csv_file:
       csv_reader = csv.reader(csv_file)
       for line in csv_reader:               # Convert data in list
          print(line)
     
    with open(s,'r') as csv_file:
       for row in csv.DictReader(csv_file):   # Convert data in dictionary
        print(row)

file_name = input("Enter the file name: ")
read_csv(file_name)