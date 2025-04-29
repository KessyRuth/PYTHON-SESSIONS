# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Error handling while loading the dataset
try:
    # Loading the Iris dataset
    iris = load_iris()
    # Creating a DataFrame
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    # Map species numbers to names
    df['species'] = df['species'].map(dict(enumerate(iris.target_names)))
    print("Dataset loaded successfully.\n")
except Exception as e:
    print(f"Error loading dataset: {e}")


# Displaying the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Checking data types and missing values
print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

# No missing values in this dataset, but if there were:
# df = df.dropna()

# Basic Data Analysis
print("\nStatistical summary:")
print(df.describe())

# Grouping by species and computing mean for each feature
print("\nMean values grouped by species:")
print(df.groupby('species').mean())

# Observations
print("\nObservations:")
print(" - Setosa flowers tend to have smaller petal and sepal dimensions compared to Virginica and Versicolor.")
print(" - Petal length and petal width show significant differences among species, useful for classification.")

# Data Visualization

# 1. Line chart - Average feature values per species
df_grouped = df.groupby('species').mean()
df_grouped.plot(kind='line', marker='o')
plt.title('Average Feature Values per Species')
plt.xlabel('Species')
plt.ylabel('Feature Values')
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Bar chart - Average petal length per species
df_grouped['petal length (cm)'].plot(kind='bar', color=['skyblue', 'lightgreen', 'lightcoral'])
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.grid(axis='y')
plt.show()

# 3. Histogram - Distribution of Sepal Length
plt.hist(df['sepal length (cm)'], bins=20, color='purple', edgecolor='black')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# 4. Scatter plot - Sepal Length vs Petal Length
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species', style='species')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.grid(True)
plt.legend(title='Species')
plt.show()

# from sklearn.datasets import load_iris

#  iris = load_iris()
