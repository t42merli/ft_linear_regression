import csv
from estimatePrice import estimatePrice

def isValid(value):
    return value.replace('.', '', 1).isdigit()


def promptMileAge():
    print("Car mile age: ")
    return input()


mileage = ""

while (isValid(mileage) == False):
    mileage = promptMileAge()
    if(isValid(mileage) == False):
        print("please enter a valid digit.")

file = open("teta.csv", "r")

reader = csv.reader(file)
teta = next(reader)

print("Estimated price:", float(teta[0]) + (float(teta[1]) * float(mileage)), "€")
