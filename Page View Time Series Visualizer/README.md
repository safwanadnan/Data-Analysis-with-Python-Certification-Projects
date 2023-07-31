# Page View Time Series Visualizer

In this project, you will visualize time series data using line charts, bar charts, and box plots. You will use Pandas, Matplotlib, and Seaborn to visualize a dataset containing the number of page views each day on the freeCodeCamp.org forum from 2016-05-09 to 2019-12-03. The data visualizations will help you understand the patterns in visits and identify yearly and monthly growth.

## Prerequisites

Before starting the project, make sure you have the following:

1. Access to the freeCodeCamp.org YouTube channel videos:
   - [Python for Everybody Video Course (14 hours)](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGpfAfDBiblRfl5p)
   - [How to Analyze Data with Python Pandas (10 hours)](https://www.youtube.com/watch?v=8y8Z6S0is3U)

2. Import the project on [Replit](https://replit.com/github/freeCodeCamp/boilerplate-page-view-time-series-visualizer) and set up the environment as instructed.

3. Familiarity with Python programming, Matplotlib, Seaborn, and the Pandas library.

## Project Description

### Dataset

The dataset, `fcc-forum-pageviews.csv`, contains the following columns:

- date: date of the data (YYYY-MM-DD)
- page_views: number of page views on that date

### Tasks

You are required to complete the following tasks in `page_view_time_series_visualizer.py`:

1. Use Pandas to import the data from "fcc-forum-pageviews.csv". Set the index to the date column.

2. Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.

3. Create a `draw_line_plot` function that uses Matplotlib to draw a line chart similar to `examples/Figure_1.png`. The title should be "Daily freeCodeCamp Forum Page Views 5/2016-12/2019". The label on the x-axis should be "Date" and the label on the y-axis should be "Page Views".

4. Create a `draw_bar_plot` function that draws a bar chart similar to `examples/Figure_2.png`. It should show average daily page views for each month grouped by year. The legend should show month labels and have a title of "Months". On the chart, the label on the x-axis should be "Years" and the label on the y-axis should be "Average Page Views".

5. Create a `draw_box_plot` function that uses Seaborn to draw two adjacent box plots similar to `examples/Figure_3.png`. These box plots should show how the values are distributed within a given year or month and how it compares over time. The title of the first chart should be "Year-wise Box Plot (Trend)" and the title of the second chart should be "Month-wise Box Plot (Seasonality)". Make sure the month labels on the bottom start at Jan, and the x and y-axes are labeled correctly.

### Development

#### Testing
To test your implementation, you can use `main.py`. Click the "run" button, and `main.py` will execute the functions defined in `page_view_time_series_visualizer.py`.

### Submitting
Once you have completed the project, copy your project's URL from Replit and submit it to freeCodeCamp to complete the certification requirements.

Happy visualizing time series data!
