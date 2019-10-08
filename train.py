import panda as pd
import numpy as np
from estimatePrice import estimatePrice

print("training model")

data = pd.read_csv('data.csv')
km = data['km']
price = data['price']
