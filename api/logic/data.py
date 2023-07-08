import pandas as pd
import numpy as np
import matplotlib
import os
matplotlib.use('Agg')

import matplotlib.pyplot as plt

def calc_derivative(x,y):
    dy = np.zeros(y.shape,np.cfloat)
    dy[0:-1] = np.diff(y)/np.diff(x)
    dy[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    
    dy = dy.real
    res = {'y': dy,'x':x}
    df = pd.DataFrame(res)
    df.to_csv(os.path.dirname(__file__)+"\\..\\static\\dy-result.csv")
    return dy

def visualise(x,y,dy):
    plt.plot(x,y)
    plt.plot(x,dy)
    os.remove(os.path.dirname(__file__)+"\\..\\static\\result.png")
    plt.savefig(os.path.dirname(__file__)+"\\..\\static\\result.png", bbox_inches="tight",
            pad_inches=0.3, transparent=True)
    plt.cla()

def api_dy():
    
    df = pd.read_csv(os.path.dirname(__file__)+'\\..\\static\\data.csv')
    
    x = df["x"].to_numpy()
    y = df["y"].to_numpy()
    # print(df)
    dy = calc_derivative(x,y)
    visualise(x,y,dy)
if __name__ == '__main__':
    api_dy()