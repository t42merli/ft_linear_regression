import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def normalize(arr):
    max = np.amax(arr)
    min = np.amin(arr)
    newAr = (arr - min) / (max - min)
    return newAr


data = pd.read_csv('data.csv')
mileage = np.array(data['km'])
price = np.array(data['price'])

normMA = normalize(mileage)
normP = normalize(price)

learningRate = 0.1
m = mileage.size

teta0 = 0
teta1 = 0
i = 0
sumerror = 1
while(np.absolute(sumerror) > 0.0001):
    estimatePrice = teta0 + teta1 * normMA
    sumerror = np.sum(estimatePrice - normP)
    teta0 = teta0 - learningRate * (sumerror / m)
    teta1 = teta1 - learningRate * \
        (np.sum((estimatePrice - normP) * normMA) / m)
    i += 1

print(teta0, teta1, i)
y_plot = []
x_plot = []
i = 0
while (i < 100):
    y_plot.append(teta0 + teta1 * (i/100))
    x_plot.append(i /100)
    i += 1

plt.figure(figsize=(10, 10))
plt.scatter(normMA, normP, color='red', label='GT')
plt.plot(x_plot, y_plot, color='black', label='pred')
plt.legend()
plt.show()
