import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np


def visualize_bar_plot(csv_file):
    #Read csv file
    df = pd.read_csv(csv_file)
    #bar x_axis
    x_axis = df.columns[1::].tolist()
    r = np.arange(len(x_axis))
    width = 0.2
    l1 = df.iloc[0].tolist()
    l2 = df.iloc[1].tolist()
    l3 = df.iloc[3].tolist()
    l4 = df.iloc[4].tolist()

    fig = plt.figure()
    plt.bar(r, l1[1::], width = width, edgecolor = 'black', label = l1[0])
    plt.bar(r+width, l2[1::], width = width, edgecolor = 'black', label = l2[0])
    plt.bar(r+2*width, l3[1::], width = width, edgecolor = 'black', label = l3[0])
    plt.bar(r+3*width, l4[1::], width = width, edgecolor = 'black', label = l4[0])
    
    plt.xticks(r+3*width/2, x_axis)
    plt.xlabel("Years")
    plt.ylabel("Quantity in '000 Tonnes",loc='center',wrap=True)
    plt.title("Capacity v/s Production of Crude Steel by Public & Private Sector in India from 2013-14 to 2018-19", loc='center', wrap=True)
    plt.legend()
    plt.ylim([0,160000])
    fig.savefig('bar_plot.png')

if __name__=="__main__":
    data_file = 'Capacity_Utilisation_in_Crude_Steel_Production_0.csv'
    visualize_bar_plot(data_file)
