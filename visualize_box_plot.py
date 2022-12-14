import pandas as pd
import matplotlib.pyplot as plt 

def get_cmap(n, name='hsv'):
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.cm.get_cmap(name, n)

def visualize_box_plot(csv_file):
    #Read csv file
    df = pd.read_csv(csv_file)

    label_ = []
    data_ = []
    for i in range(16):
        row_data = df.iloc[i].tolist()
        label_.append(row_data[0])
        data_.append(row_data[1::])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    bp = ax.boxplot(data_, patch_artist = True,
                notch ='True', vert = 0)
    colors = get_cmap(21)
    for i,patch, in enumerate(bp['boxes']):
        patch.set_facecolor(colors(i))
 
    # changing color and linewidth of
    # whiskers
    for whisker in bp['whiskers']:
        whisker.set(color =colors(17),
                    linewidth = 1.5,
                    linestyle =":")
    
    # changing color and linewidth of
    # caps
    for cap in bp['caps']:
        cap.set(color =colors(18),
                linewidth = 2)
    
    # changing color and linewidth of
    # medians
    for median in bp['medians']:
        median.set(color =colors(19),
                linewidth = 3)
    
    # changing style of fliers
    for flier in bp['fliers']:
        flier.set(marker ='D',
                color =colors(20),
                alpha = 0.5)
        
    # x-axis labels
    ax.set_yticklabels(label_)
    
    plt.title("Box Plot of Freight Revenue Generated by Each zone from March 2020 to January 2021", loc='center', wrap=True)

    fig.savefig('box_plot.png', bbox_inches="tight")

if __name__=="__main__":
    data_file = 'RS_Session_253_AU1417.B.csv'
    visualize_box_plot(data_file)
