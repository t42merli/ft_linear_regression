import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

print("Training model...")

data = pd.read_csv('data.csv')
mileage = np.array(data['km'])
max = np.amax(mileage)
min = np.amin(mileage)
normMA = (mileage - min) / (max - min)
price = np.array(data['price'])

learningRate = 0.1
m = mileage.size

tetha0 = 0
tetha1 = 0
sumerror = 1
while(np.absolute(sumerror) > 0.0001):
    estimatePrice = tetha0 + tetha1 * normMA
    sumerror = np.sum(estimatePrice - price)
    tetha0 = tetha0 - learningRate * (sumerror / m)
    tetha1 = tetha1 - learningRate * \
        (np.sum((estimatePrice - price) * normMA) / m)

print("New tethas: ")
print("tetha0:", tetha0, "tetha1:", tetha1)

y_plot = []
x_plot = []
i = 0
while (i < 300000):
    res = tetha0 + tetha1 * (i - min) / (max - min)
    y_plot.append(res)
    x_plot.append(i)
    i += 1000

plt.figure(figsize=(10, 10))
plt.scatter(mileage, price, color='red', label='GT')
plt.plot(x_plot, y_plot, color='black', label='pred')
plt.legend()
plt.show()
