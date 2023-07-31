# Sea Level Predictor

In this project, you will analyze a dataset of the global average sea level change since 1880 and use the data to predict the sea level change through the year 2050.

## Prerequisites

Before starting the project, make sure you have the following:

1. Access to the freeCodeCamp.org YouTube channel videos:
   - [Python for Everybody Video Course (14 hours)](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGpfAfDBiblRfl5p)
   - [How to Analyze Data with Python Pandas (10 hours)](https://www.youtube.com/watch?v=8y8Z6S0is3U)

2. Import the project on [Replit](https://replit.com/github/freeCodeCamp/boilerplate-sea-level-predictorvvvvvvvvvvvvvvvvvv) and set up the environment as instructed.

3. Familiarity with Python programming, Matplotlib, Seaborn, Scipy, and the Pandas library.

## Project Description

### Dataset

The dataset, `epa-sea-level.csv`, contains two columns:

- Year: year of the data
- CSIRO Adjusted Sea Level: global average sea level change in inches since 1880

### Tasks

You are required to complete the following tasks in `sea_level_predictor.py`:

1. Use Pandas to import the data from `epa-sea-level.csv`.

2. Use Matplotlib to create a scatter plot using the `Year` column as the x-axis and the `CSIRO Adjusted Sea Level` column as the y-axis.

3. Use the `linregress` function from Scipy's `stats` module to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.

4. Plot a new line of best fit using only the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.

The x label should be "Year", the y label should be "Sea Level (inches)", and the title should be "Rise in Sea Level".

### Development

#### Testing
To test your implementation, you can use `main.py`. Click the "run" button, and `main.py` will execute the functions defined in `sea_level_predictor.py`.

### Submitting
Once you have completed the project, copy your project's URL from Replit and submit it to freeCodeCamp to complete the certification requirements.

Happy predicting sea level changes!
