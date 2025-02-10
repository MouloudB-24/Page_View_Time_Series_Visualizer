import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.pyplot import legend
from pandas.plotting import register_matplotlib_converters
import matplotlib.dates as mdates
import calendar
register_matplotlib_converters()

# Import data
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=['date'])

# Clean data
limit_low, limit_high = df['value'].quantile([0.025, 0.975])
df = df[df['value'].between(limit_low, limit_high)]


# Line chart
def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 5), dpi=200)
    ax.plot(df.index, df['value'], color='red', linewidth=1)

    # Set the title and labels
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Improved date display
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

    # Save image and return fig
    fig.savefig('line_plot.png')
    return fig


# Bar chart
def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_copy = df.copy()
    df_copy['year'] = df_copy.index.year
    df_copy['month'] = df_copy.index.strftime('%B')
    df_copy['month_num'] =df_copy.index.month
    df_bar = df_copy.groupby(['year', 'month', 'month_num'])['value'].mean().reset_index()

    # Sort data by year, then by month
    df_bar.sort_values(['year', 'month_num'], inplace=True)

    # Create a pivot table
    pivot_table = df_bar.pivot(index='year', columns='month', values='value')

    # Reorder columns from January to December
    pivot_table = pivot_table.reindex(columns=[calendar.month_name[i] for i in range(1, 13)])

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
    pivot_table.plot(kind='bar', ax=ax)

    # Customize graph
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months')
    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.strftime('%b')

    # Configure style
    sns.set_style("whitegrid")

    # Define color palette
    year_palette = sns.color_palette('husl', len(df_box['year'].unique()))
    month_palette = sns.color_palette('Set2', 12)

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))

    # Year-wise box (annual trend)
    sns.boxplot(x='year',
                y='value',
                data=df_box,
                ax=axes[0],
                hue='year',
                palette=sns.color_palette('husl', 4),
                legend=False
                )
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')


    # Month-wise box (Seasonality)
    sns.boxplot(x='month',
                y='value',
                data=df_box,
                ax=axes[1],
                hue='month',
                order=[calendar.month_abbr[i] for i in range(1, 13)],
                palette=sns.color_palette('Set2', 12)
                )
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig


if __name__ == '__main__':
    #draw_line_plot()
    draw_box_plot()