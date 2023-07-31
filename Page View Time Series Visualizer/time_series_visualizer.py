import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting the index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',
                 parse_dates=['date'],
                 index_col='date')

# Clean data
lower_bound = df['value'].quantile(0.025)
upper_bound = df['value'].quantile(0.975)
df = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]


def draw_line_plot():
  # Draw line plot
  fig, ax = plt.subplots(figsize=(12, 6))
  ax.plot(df.index, df['value'], color='r')
  ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
  ax.set_xlabel("Date")
  ax.set_ylabel("Page Views")
  plt.xticks(rotation=45)

  # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig


def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  df_bar = df.copy()
  df_bar['year'] = df_bar.index.year
  df_bar['month'] = df_bar.index.strftime('%b')
  df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

  # Draw bar plot
  fig, ax = plt.subplots(figsize=(10, 7))
  ax = df_bar.plot(kind='bar', legend=True, ax=ax)
  ax.set_xlabel("Years")
  ax.set_ylabel("Average Page Views")
  ax.legend(title='Months',
            labels=[
              'January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December'
            ])

  # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig


def draw_box_plot():
  # Prepare data for box plots (this part is done!)
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df_box.date]
  df_box['month'] = [d.strftime('%b') for d in df_box.date]

  # Draw box plots (using Seaborn)
  fig, axes = plt.subplots(1, 2, figsize=(20, 8))
  sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
  sns.boxplot(x='month',
              y='value',
              data=df_box,
              ax=axes[1],
              order=[
                'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
                'Oct', 'Nov', 'Dec'
              ])
  axes[0].set_title("Year-wise Box Plot (Trend)")
  axes[0].set_xlabel("Year")
  axes[0].set_ylabel("Page Views")
  axes[1].set_title("Month-wise Box Plot (Seasonality)")
  axes[1].set_xlabel("Month")
  axes[1].set_ylabel("Page Views")

  # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig