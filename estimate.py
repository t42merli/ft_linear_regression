import csv

def promptMileAge():
    print("Car mile age: ")
    return input()

mileage = ""

while (mileage.isdigit() == False):
	mileage = promptMileAge()
	if(mileage.isdigit() == False):
		print("please enter a valid digit.")

file = open("teta.csv", "r")

reader = csv.reader(file)
for row in reader:
	teta = row

print ("Estimated price : ", float(teta[0]) + (float(teta[1]) * float(mileage)))
