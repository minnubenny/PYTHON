import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class IrisDatasetAnalyzer:
    def __init__(self, file_path):
        # Load data immediately upon initialization
        self.data = pd.read_csv("/home/minnu/Desktop/week 1/may 9/Iris.csv")

    def filter_species(self, species_name):
        # Filter dataset by species
        return self.data[self.data['Species'] == species_name]

    def show_summary_stats(self, species_name):
        # Display summary stats including count, percentiles, mean, std, min, max
        species_data = self.filter_species(species_name)
        if species_data is not None:
            sepal_length = species_data['SepalLengthCm'].values
            print(f"Summary Stats for {species_name}:")
            print(f"Count: {len(sepal_length)}")
            print(f"Mean Sepal Length: {np.mean(sepal_length):.2f} cm")
            print(f"Standard Deviation: {np.std(sepal_length):.2f} cm")
            print(f"Min: {np.min(sepal_length):.2f} cm")
            print(f"25th Percentile: {np.percentile(sepal_length, 25):.2f} cm")
            print(f"50th Percentile (Median): {np.median(sepal_length):.2f} cm")
            print(f"75th Percentile: {np.percentile(sepal_length, 75):.2f} cm")
            print(f"Max: {np.max(sepal_length):.2f} cm")

    def plot_sepal_length(self, species_name):
        # Plot the distribution of sepal length for the species
        species_data = self.filter_species(species_name)
        plt.hist(species_data['SepalLengthCm'], bins=10, color='green', edgecolor='black')
        plt.title(f'Sepal Length Distribution for {species_name}')
        plt.xlabel('Sepal Length (cm)')
        plt.ylabel('Frequency')
        plt.show()

# Example usage
if __name__ == "__main__":
    # Create an analyzer object
    analyzer = IrisDatasetAnalyzer('iris.csv')

    # Display summary stats and plot for Iris-setosa
    analyzer.show_summary_stats('Iris-setosa')
    analyzer.plot_sepal_length('Iris-setosa')
