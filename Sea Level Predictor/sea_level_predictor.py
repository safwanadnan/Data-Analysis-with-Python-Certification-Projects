import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], label='Data')

    # Create first line of best fit using all data
    slope_all, intercept_all, _, _, _ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_all = range(1880, 2051)
    line_all = [(slope_all * year + intercept_all) for year in years_all]
    plt.plot(years_all, line_all, label='Best Fit (1880-2050)', color='red')

    # Create second line of best fit using data from year 2000 onwards
    data_from_2000 = data[data['Year'] >= 2000]
    slope_2000, intercept_2000, _, _, _ = linregress(data_from_2000['Year'], data_from_2000['CSIRO Adjusted Sea Level'])
    years_2000_onwards = range(2000, 2051)
    line_2000_onwards = [(slope_2000 * year + intercept_2000) for year in years_2000_onwards]
    plt.plot(years_2000_onwards, line_2000_onwards, label='Best Fit (2000-2050)', color='green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
