import csv
import numpy as np

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
teta = np.array(next(reader)).astype(np.float)
norm = np.array(next(reader)).astype(np.float)
mileage = float(mileage)

print("Estimated price:",
      teta[0] + teta[1] * ((mileage - norm[0]) / (norm[1] - norm[0])), "€")
