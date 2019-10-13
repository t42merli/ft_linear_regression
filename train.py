import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

print("Training model...\n")

data = pd.read_csv('data.csv')
mileage = np.array(data['km'])
max = np.amax(mileage)
min = np.amin(mileage)
normMA = (mileage - min) / (max - min)
price = np.array(data['price'])

learningRate = 0.1
m = mileage.size

theta0 = 0
theta1 = 0
sumerror = 1
while(np.absolute(sumerror) > 0.0001):
    estimatePrice = theta0 + theta1 * normMA
    sumerror = np.sum(estimatePrice - price)
    theta0 = theta0 - learningRate * (sumerror / m)
    theta1 = theta1 - learningRate * \
        (np.sum((estimatePrice - price) * normMA) / m)

print("New thetas: ")
print("theta0:", theta0, "theta1:", theta1)
print("\nSaving thetas and normlization ratio in model.csv...\n")

file = open("model.csv", "w")
csvWriter = csv.writer(file)
csvWriter.writerow([theta0, theta1])
csvWriter.writerow([min, max])
file.close()
print("Done. Here is a graph of the estimation function after training:")

y_plot = []
x_plot = []
i = 0
while (i < 300000):
    res = theta0 + theta1 * (i - min) / (max - min)
    y_plot.append(res)
    x_plot.append(i)
    i += 1000

plt.figure(figsize=(10, 10))
plt.scatter(mileage, price, color='red', label='GT')
plt.plot(x_plot, y_plot, color='black', label='pred')
plt.legend()
plt.show()
