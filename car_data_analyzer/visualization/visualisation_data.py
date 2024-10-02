import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from typing import Dict, Any

# Константи
FIGURE_SIZE = (12, 8)
FONT_TITLE = {'fontsize': 20, 'fontweight': 'bold'}
FONT_LABEL = {'fontsize': 14}
GRID_STYLE = {'linestyle': '--', 'alpha': 0.7}


def setup_plot(figsize: tuple = FIGURE_SIZE) -> None:
    """Настройка на основните параметри на графиката."""
    plt.figure(figsize=figsize)
    sns.set(style="whitegrid")


def finalize_plot(title: str, xlabel: str, ylabel: str, grid: bool = True) -> None:
    """Финализиране на графиката с добавяне на заглавие, етикети и мрежа."""
    plt.title(title, **FONT_TITLE)
    plt.xlabel(xlabel, **FONT_LABEL)
    plt.ylabel(ylabel, **FONT_LABEL)
    if grid:
        plt.grid(True, **GRID_STYLE)
    plt.tight_layout()
    plt.show()


def plot_distribution(data: pd.DataFrame, column: str, color: str, title: str, xlabel: str, ylabel: str) -> None:
    """Създаване на хистограма за разпределението на данните."""
    setup_plot()
    sns.histplot(data[column], bins=20, kde=True, color=color)
    finalize_plot(title, xlabel, ylabel)


def plot_top_heaviest_cars(df_car_data: pd.DataFrame) -> None:
    """Визуализация на 10-те най-тежки автомобила."""
    setup_plot()
    top_heaviest = df_car_data.nlargest(10, 'Weight_in_kg')[['Weight_in_kg', 'Name']]
    colors = sns.color_palette("coolwarm", len(top_heaviest))
    bars = plt.barh(top_heaviest['Name'], top_heaviest['Weight_in_kg'], color=colors)
    for bar in bars[::-1]:
        plt.text(bar.get_width() - 1, bar.get_y() + bar.get_height() / 2,
                 f'{bar.get_width():.1f} kg', va='center', ha='right', fontsize=14, color='black',
                 fontweight='bold')
    finalize_plot('Top 10 Heaviest Cars (in kg)', 'Weight in kg', 'Car Name')


def plot_cars_by_year(df_car_data: pd.DataFrame) -> None:
    """Визуализация на броя автомобили по години."""
    setup_plot()
    df_car_data['Year'].value_counts().sort_index().plot(kind='line', marker='o', color='steelblue')
    finalize_plot('Number of Cars by Year', 'Year', 'Number of Cars')


def plot_cars_by_manufacturer(df_car_data: pd.DataFrame) -> None:
    """Визуализация на броя автомобили по производител."""
    setup_plot()
    df_car_data['Origin'].value_counts().plot(kind='bar', color='salmon')
    finalize_plot('Number of Cars by Manufacturer', 'Manufacturer', 'Number of Cars')


def plot_correlation_matrix(df_car_data: pd.DataFrame) -> None:
    """Визуализация на корелационна матрица."""
    setup_plot()
    correlation_matrix = df_car_data[['Horsepower', 'Weight_in_kg', 'Liters_per_100km', 'Acceleration']].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
    finalize_plot('Correlation Matrix', '', '', grid=False)


def plot_cars_by_range(df_car_data: pd.DataFrame, column: str, bins: list, labels: list, color: str,
                       title: str) -> None:
    """Визуализация на броя автомобили по определен диапазон."""
    df_car_data[f'{column}_Range'] = pd.cut(df_car_data[column], bins=bins, labels=labels)
    range_counts = df_car_data[f'{column}_Range'].value_counts().sort_index()

    setup_plot()
    range_counts.plot(kind='bar', color=color)
    finalize_plot(title, f'{column} Range', 'Number of Cars')


def visualize_data(df_car_data: pd.DataFrame) -> None:
    """Основна функция за визуализация на всички графики."""
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


def generate_summary_statistics(df_car_data: pd.DataFrame) -> Dict[str, Any]:
    """Генериране на обобщаващи статистики за данните."""
    summary = {
        "total_cars": len(df_car_data),
        "average_horsepower": df_car_data['Horsepower'].mean(),
        "average_weight": df_car_data['Weight_in_kg'].mean(),
        "most_common_origin": df_car_data['Origin'].mode().iloc[0],
        "year_range": (df_car_data['Year'].min(), df_car_data['Year'].max())
    }
    return summary


def print_summary_statistics(summary: Dict[str, Any]) -> None:
    """Отпечатване на обобщаващи статистики."""
    print("Summary Statistics:")
    print(f"Total number of cars: {summary['total_cars']}")
    print(f"Average horsepower: {summary['average_horsepower']:.2f}")
    print(f"Average weight (kg): {summary['average_weight']:.2f}")
    print(f"Most common origin: {summary['most_common_origin']}")
    print(f"Year range: {summary['year_range'][0]} - {summary['year_range'][1]}")


def analyze_and_visualize_data(df_car_data: pd.DataFrame) -> None:
    """Основна функция за анализ и визуализация на данните."""
    summary = generate_summary_statistics(df_car_data)
    print_summary_statistics(summary)
    visualize_data(df_car_data)
