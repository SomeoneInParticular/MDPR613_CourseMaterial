# Import our required packages
import pandas as pd
import numpy as np

from matplotlib import pyplot as plt

# Load the data from 'iris_data.tsv'
df = pd.read_csv('iris_data.tsv', sep='\t')

# Plot petal length as a function of petal width as a scatter plot, species coded by icon
# HINT: Iterate through the combinations you want and plot each in turn
species = ['Setosa', 'Verginica', 'Versicolour']
markers = ['*', 'x', 'o']

for i in range(3):
    sub_df = df[df.loc[:, "Species"] == species[i]]
    plt.scatter(
        x=sub_df.loc[:, "Petal Width"],
        y=sub_df.loc[:, "Petal Length"],
        marker=markers[i],
        label=species[i]
    )

## Add our title and axis labels
plt.title("Petal Length vs. Petal Width in Iris Species")
plt.xlabel("Petal Width")
plt.ylabel("Petal Length")

## Add a legend for readability
plt.legend()

## Save and reset the plotting space for the next plot
plt.savefig('petal_plot.svg')
plt.close()


# Plot max sepal length per species as a bar plot, color coded with a legend
# HINT: Remember the 'x' argument species the position of the bars on the *current* plot!
colours = ["red", "green", "blue"]

for i in range(3):
    ## Calculate the maximum sepal length for this species
    sub_df = df[df.loc[:, "Species"] == species[i]]
    max_len = np.max(sub_df.loc[:, "Sepal Length"])
    ## Plot it in its unique location (just re-using 'i' in this case)
    plt.bar(
        x=i,
        height=max_len,
        color=colours[i],
        label=species[i]
    )

## Add our legend
plt.legend()

## Save and reset the plotting space for the next plot
plt.savefig('max_sepal.svg')
plt.close()
