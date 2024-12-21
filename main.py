# Importing the Libraries
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
import plotly.express as px

# Reading the dataset
df = pd.read_csv("SFO/train.csv")
# Printing the first five rows to check
# print(df.head())

# Truncating the irrelevant columns
df = df.drop(['Category','Descript','DayOfWeek','PdDistrict','Resolution','Address'], axis=1)
# Printing the first five rows to check
print("First five rows after dropping irrelevant columns: \n")
print(df.head())
print()

# Check for null data
print("Checking for null data in the dataset: \n")
print(df.isnull().sum())
print()

# Year filtering operation

# Start by removing the time from the datetime column
# NOTE: Using `lambda` the anonymous function.
extract_date = lambda x: (x["Dates"].split())[0]
df["Dates"] = df.apply(extract_date, axis=1)  # axis 1 refers to the horizontal direction meaning it applies to all the columns of each row.
# print(df.head())

# Split the Date and only keep the year
extract_year = lambda y: (y["Dates"].split('-'))[0]
df["Dates"] = df.apply(extract_year, axis=1)
# print(df.head())

# NOTE: This dataset contains data from 2003 to 2014. 

# Input from user asking for the year
user_year_input = input("Select a year (2003-2014): ")
print()

# Categorize dataset by year
df_filtered_by_year = df[(df.Dates == user_year_input)].copy()
# print(df_filtered_by_year.head())
print(f"First five rows of the dataset for the year {user_year_input}: \n")
print(df_filtered_by_year.head())
print()

# Scale the data for accurate results
scaler = MinMaxScaler()
# Y is latitude and X is longitude... 
scaler.fit(df_filtered_by_year[['X']])
df_filtered_by_year.loc[:, 'X_scaled'] = scaler.transform(df_filtered_by_year[['X']])

scaler.fit(df_filtered_by_year[['Y']])
df_filtered_by_year.loc[:, 'Y_scaled'] = scaler.transform(df_filtered_by_year[['Y']])
# print(df_filtered_by_year.head())
print("First five rows of the scaled dataset with clusters: \n")
print(df_filtered_by_year.head())
print()

# Check for number of clusters using Elbow Method
k_range = range(1, 15)

# Initialize empty list to hold inertia values of each K.
inertia_values = []

for k in k_range:
    kmeans_model = KMeans(n_clusters=k)
    kmeans_model.fit(df_filtered_by_year[['X_scaled', 'Y_scaled']])
    inertia_values.append(kmeans_model.inertia_)

# print(inertia_values)

# Plotting the graph
def plot_k():
    plt.xlabel('K')
    plt.ylabel('Inertia')
    plt.plot(k_range, inertia_values)
    plt.show()

# Ask the user if they want to see the plot
user_plot_response = input("Do you want to see the plot? (yes/no): ")

if user_plot_response.lower() == 'yes':
    plot_k()  # Call the plot function if the user wants to see the plot
else:
    print("Plot not displayed.")

df_inertia = pd.DataFrame({'K': k_range, 'Inertia': inertia_values})

print("Inertia values for different K values: \n")
print(df_inertia)
print()

# NOTE: Using Elbow Method, K = 5 (2014)

# K-Means model for K = 5
kmeans_final_model = KMeans(n_clusters=5)
predicted_clusters = kmeans_final_model.fit_predict(df_filtered_by_year[['X_scaled', 'Y_scaled']])
# print(predicted_clusters)

# Adding this new data as a column
df_filtered_by_year['cluster'] = predicted_clusters
print(df_filtered_by_year.head())
