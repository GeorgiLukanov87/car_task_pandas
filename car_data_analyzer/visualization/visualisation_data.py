# visualisation_data/visualisation_data.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def setup_plot(figsize=(12, 8)):
    plt.figure(figsize=figsize)
    sns.set(style="whitegrid")


def finalize_plot(title, xlabel, ylabel, grid=True):
    plt.title(title, fontsize=20, fontweight='bold')
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    if grid:
        plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


def plot_distribution(data, column, color, title, xlabel, ylabel):
    setup_plot()
    sns.histplot(data[column], bins=20, kde=True, color=color)
    finalize_plot(title, xlabel, ylabel)


def plot_top_heaviest_cars(df_car_data):
    setup_plot()
    top_heaviest = df_car_data.nlargest(10, 'Weight_in_kg')[['Weight_in_kg', 'Name']]
    colors = sns.color_palette("coolwarm", len(top_heaviest))
    bars = plt.barh(top_heaviest['Name'], top_heaviest['Weight_in_kg'], color=colors)
    for bar in bars[::-1]:
        plt.text(bar.get_width() - 1, bar.get_y() + bar.get_height() / 2,
                 f'{bar.get_width():.1f} kg', va='center', ha='right', fontsize=12, color='black',
                 fontweight='bold')
    finalize_plot('Top 10 Heaviest Cars (in kg)', 'Weight in kg', 'Car Name')


def plot_cars_by_year(df_car_data):
    setup_plot()
    df_car_data['Year'].value_counts().sort_index().plot(kind='line', marker='o', color='steelblue')
    finalize_plot('Number of Cars by Year', 'Year', 'Number of Cars')


def plot_cars_by_manufacturer(df_car_data):
    setup_plot()
    df_car_data['Origin'].value_counts().plot(kind='bar', color='salmon')
    finalize_plot('Number of Cars by Manufacturer', 'Manufacturer', 'Number of Cars')


def plot_correlation_matrix(df_car_data):
    setup_plot()
    correlation_matrix = df_car_data[['Horsepower', 'Weight_in_kg', 'Liters_per_100km', 'Acceleration']].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
    finalize_plot('Correlation Matrix', '', '', grid=False)


def plot_cars_by_range(df_car_data, column, bins, labels, color, title):
    df_car_data[f'{column}_Range'] = pd.cut(df_car_data[column], bins=bins, labels=labels)
    range_counts = df_car_data[f'{column}_Range'].value_counts().sort_index()

    setup_plot()
    range_counts.plot(kind='bar', color=color)
    finalize_plot(title, f'{column} Range', 'Number of Cars')


def visualize_data(df_car_data):
    plot_distribution(df_car_data, 'Horsepower', 'skyblue', 'Distribution of Horsepower', 'Horsepower',
                      'Number of Cars')
    plot_top_heaviest_cars(df_car_data)
    plot_cars_by_year(df_car_data)
    plot_cars_by_manufacturer(df_car_data)
    plot_distribution(df_car_data, 'Liters_per_100km', 'lightgreen', 'Distribution of Liters per 100 km',
                      'Liters per 100 km', 'Number of Cars')
    plot_distribution(df_car_data, 'Acceleration', 'lightcoral', 'Distribution of Acceleration',
                      'Acceleration (0-60 mph)', 'Number of Cars')
    plot_correlation_matrix(df_car_data)

    liters_bins = [0, 5, 10, 15, 20, 25]
    liters_labels = ['0-5', '5-10', '10-15', '15-20', '20-25']
    plot_cars_by_range(df_car_data, 'Liters_per_100km', liters_bins, liters_labels, 'orchid',
                       'Number of Cars by Liters per 100 km Range')

    acceleration_bins = [0, 5, 10, 15, 20, 25]
    acceleration_labels = ['0-5', '5-10', '10-15', '15-20', '20-25']
    plot_cars_by_range(df_car_data, 'Acceleration', acceleration_bins, acceleration_labels, 'plum',
                       'Number of Cars by Acceleration Range')
