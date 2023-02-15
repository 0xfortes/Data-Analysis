import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('/path')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    fig, ax = plt.subplots()
    plt.scatter(x, y)

    # Create first line of best fit
    res = linregress(x, y)
    x_axis_pred = pd.Series([i for i in range(1880, 2050)])
    y_axis_pred = res.slope*x_axis_pred + res.intercept
    plt.plot(x_axis_pred, y_axis_pred, 'r')

    # Create second line of best fit
    # Pick the data from 2000 to the last year of the dataset
    # Create new axis 
    df_second = df.loc[df['Year'] >= 2000]
    second_x = df_second['Year']
    second_y = df_second['CSIRO Adjusted Sea Level']
    second_res = linregress(second_x, second_y)
    x_axis_pred2 = pd.Series([i for i in range(2000, 2050)])
    y_axis_pred2 = second_res.slope*x_axis_pred2 + second_res.intercept
    plt.plot(x_axis_pred2, y_axis_pred2, 'black')


    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (Inches)')
    ax.set_title('Sea Level Rise Over Time')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()