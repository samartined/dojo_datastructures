import csv

def main():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
