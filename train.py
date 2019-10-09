import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

print("training model")

data = pd.read_csv('data.csv')
mileage = np.array(data['km'])
price = np.array(data['price'])
learningRate = 0.01
m = mileage.size

teta0 = 0
teta1 = 0
i = 0
while(i < 10):
    estimatePrice = teta0 + teta1 * mileage
    error = (estimatePrice - price)
    derrivate1 = (np.sum(error) / m)
    derriveate2 = (np.sum(error) / m)
    print(derrivate1, derriveate2)
    teta0 = teta0 - learningRate * (np.sum(error) / m)
    teta1 = teta1 - learningRate * (np.sum(error * mileage) / m)
    i += 1

print(teta0, teta1)

# print(teta0, teta1)

# print("done", teta0, teta1)
