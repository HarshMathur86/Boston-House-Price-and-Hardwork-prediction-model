import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

X = pd.read_csv("Hardwork_Training Data/Linear_X_Train.csv").values
Y = pd.read_csv("Hardwork_Training Data/Linear_Y_Train.csv").values

theta = np.load('Theta_list.npy')

#100, 2
T0 = theta[:,0]
T1 = theta[:,1]

plt.ion()
for i in range(0, 50, 5):
    y_ = T1[i]*X + T0#this is the addition of two array and in the plot function two array will be given to plot the line

    plt.scatter(X, Y)

    plt.plot(X,y_,'red')
    plt.draw()
    plt.pause(1)
    plt.clf()

