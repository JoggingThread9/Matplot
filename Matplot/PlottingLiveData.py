from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

index = count()


def animate(i):
    data = pd.read_csv('data6.csv')
    xVal = data['xVal']
    yVal1 = data['yVal1']
    yVal2 = data['yVal2']

    plt.cla()

    plt.plot(xVal, yVal1, label='Channel 1')
    plt.plot(xVal, yVal2, label='Channel 2')

    plt.legend(loc="upper left")

    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.show()
