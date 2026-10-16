import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv('iris_data.csv')
species_counts = df['Species'].value_counts()
#species = df['Species']
petal_length = (df['PetalLengthCm'] < 1.2).sum()
petal_length3 = (1.5 < df['PetalLengthCm']).sum()
petal_length2 = 150 - petal_length - petal_length3


fig = plt.figure(figsize = (7, 7)) 
ax1 = fig.add_subplot (211)
ax2 = fig.add_subplot (212)
ax1.pie(species_counts, labels = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])
ax2.pie([petal_length, petal_length2, petal_length3], labels = ['<1.2', '1.5> >1.2', '>1.5'])

#print(petal_length, petal_length2, petal_length3)
plt.show()