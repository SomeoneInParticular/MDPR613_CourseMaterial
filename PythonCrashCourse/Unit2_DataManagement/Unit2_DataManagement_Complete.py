# Import our required packages
import pandas as pd
import numpy as np

# Load the data from 'iris_data.tsv'
df = pd.read_csv('iris_data.tsv', sep='\t')

# Get the mean petal width for all irises
mean_petal_width = np.mean(df.loc[:, "Petal Width"])
print(f"Mean iris petal width: {mean_petal_width}")

# Get the standard deviation of Petal Length for Versicolor irises
versi_df = df[df.loc[:, "Species"] == "Versicolour"]
std_versi_petal_length = np.std(versi_df.loc[:, "Petal Length"])
print(f"Standard Deviation of versicolour iris petal length: {std_versi_petal_length}")


# Identify which species has the largest observed Sepal Length in the dataset
max_sepal_length = np.max(df.loc[:, "Sepal Length"])
max_species_vals = df[df.loc[:, "Sepal Length"] == max_sepal_length].loc[:, "Species"]
print(f"Species with the largest sepal length: {max_species_vals}")
