# San Francisco Crime Geographical Clustering

## Overview
The San Francisco Crime Geographical Clustering project analyzes crime data from San Francisco between 2003 and 2014. 
By utilizing the real San Francisco Crime Dataset, we focus on geographical data (latitude and longitude) to identify crime hotspots through clustering techniques.

## Features 
1. **Data Collection**:
   - Gather crime data from public sources (e.g., police department databases, open data portals).
   - Ensure the dataset includes relevant fields such as location (latitude and longitude), crime type, date, and time.

2. **Data Preprocessing**:
   - Clean the dataset by handling missing values and removing duplicates.
   - Convert data types to ensure latitude and longitude are in float format.
   - Filter data for specific time periods or crime categories if necessary.

3. **Exploratory Data Analysis (EDA)**:
   - Visualize crime data using histograms, bar charts, or scatter plots to understand distributions and trends.
   - Identify hotspots or patterns in crime occurrences using geographical visualizations.

4. **Clustering Techniques**:
   - Apply clustering algorithms (e.g., K-Means, DBSCAN) to group similar crime incidents based on geographical locations.
   - Determine the optimal number of clusters using methods like the Elbow Method or Silhouette Score.

5. **Geospatial Analysis**:
   - Utilize libraries like GeoPandas or Folium for advanced geographical data manipulation and visualization.
   - Map clusters on a geographical map to visualize crime hotspots.

6. **Visualization**:
   - Create interactive maps using Plotly or other visualization libraries to display crime clusters.
   - Add features like hover data to provide additional information about each cluster (e.g., number of incidents, types of crimes).

7. **Insights and Reporting**:
   - Analyze clustering results to derive insights (e.g., identifying high-crime areas, trends over time).
   - Generate reports or dashboards to communicate findings to stakeholders (e.g., law enforcement, community organizations).

## Project Goals
- Develop a data preprocessing pipeline to clean and prepare the San Francisco crime dataset for analysis.
- Implement clustering algorithms to identify and visualize crime hotspots across the city.
- Analyze the effectiveness of the K-Means clustering method in grouping similar crime incidents based on geographical coordinates.
- Provide actionable insights and visual representations of crime patterns to assist law enforcement and community stakeholders in decision-making.

## Requirements
- **Python**: Version 3.x
- **Libraries**: Pandas, NumPy, Plotly, Scikit-learn, Matplotlib

## Usage
- Import libraries, scale, and prepare the dataset.
- Decide on the number of clusters using the Elbow Method (finding the optimal K value).
- Build the model and perform the clustering operation using the K-means algorithm.

## Dataset
- **Source**: [Kaggle San Francisco Crime Dataset](https://www.kaggle.com/competitions/sf-crime/data?select=train.csv.zip)
- **File**: `train.csv`
- **Format**: Comma-separated values containing crime records of SFO.

### Relevant Features
- Dates, X, Y 

### Irrelevant Features
- Category, Descript, DayOfWeek, PdDistrict, Resolution, Address

## Concepts

### K Means Clustering
K-means is a popular clustering algorithm used in machine learning and data analysis. It partitions a dataset into K distinct clusters based on feature similarity. Here’s a brief overview of how it works:

1. **Initialization**: Choose K initial centroids randomly from the dataset.
2. **Assignment**: Assign each data point to the nearest centroid, forming K clusters.
3. **Update**: Calculate new centroids by taking the mean of all data points assigned to each cluster.
4. **Repeat**: Repeat the assignment and update steps until the centroids no longer change significantly or a maximum number of iterations is reached.

#### Key Points:
- **Distance Metric**: K-means typically uses Euclidean distance to measure the distance between points and centroids.
- **Scalability**: Efficient for large datasets but sensitive to the initial placement of centroids.
- **Applications**: Commonly used in market segmentation, social network analysis, organization of computing clusters, and image compression.

### Choosing the Number of Clusters (K) in K-Means Clustering
To select the range for K in K-Means clustering:

1. **Data Size**: Consider the dataset size; larger datasets may need a wider range.
2. **Domain Knowledge**: Use insights from the domain to estimate a reasonable number of clusters.
3. **Elbow Method**: Start with a range (e.g., 1 to 10 or 1 to 20) and adjust based on the inertia plot to find the "elbow" point.
4. **Experimentation**: Test different ranges and values to evaluate their impact on clustering results.

### Inertia in K-Means Clustering
Inertia measures how tightly the data points in each cluster are packed around their centroids. It is calculated as the sum of squared distances between each data point and its assigned cluster centroid. Lower inertia values indicate more compact clusters.

#### Significance:
- **Cluster Compactness**: Lower inertia means better-defined clusters.
- **Model Evaluation**: Inertia helps assess the performance of different K-Means models.
- **Elbow Method**: Used to determine the optimal number of clusters (K) by plotting inertia against K values.

### The Elbow Method
The Elbow Method is a technique used to determine the optimal number of clusters (K) in K-means clustering. Here's a brief overview of how it works:
1. **Run K-means Clustering**: Perform K-means clustering on the dataset for a range of K values (e.g., from 1 to 10).
2. **Calculate Inertia**: For each K, calculate the inertia (within-cluster sum of squares).
3. **Plot the Results**: Create a plot with the number of clusters (K) on the x-axis and the inertia on the y-axis.
4. **Identify the "Elbow" Point**: Look for a point on the plot where the rate of decrease in inertia sharply changes, indicating the optimal number of clusters.

### Lambda
Python's lambda is a small, anonymous function defined using the `lambda` keyword. Unlike regular functions defined with `def`, lambda functions are typically used for short, simple operations.

#### Key Features:
1. **Anonymous**: Lambda functions do not have a name and are often used for short-term needs.
2. **Syntax**: The syntax for a lambda function is:
   ```
   lambda arguments: expression
   ```
3. **Single Expression**: Lambda functions can only contain a single expression.
4. **Return Value**: The result of the expression is automatically returned.

#### When to Use a Lambda Function:
- For short operations or temporary use.
- In functional programming contexts with `map()`, `filter()`, or `reduce()`.

### MinMaxScaler
MinMaxScaler is used to scale features to a specific range, typically between 0 and 1. This is important in machine learning, especially for algorithms like KMeans, which are sensitive to the scale of the data.

### .loc 
Using `.loc` ensures that you're modifying the DataFrame correctly and avoids the `SettingWithCopyWarning`. It is a best practice when working with pandas DataFrames, especially with slices or filtered DataFrames.

### Why use .copy() ?
Adding `.copy()` when creating `df_filtered_by_year` ensures that you're working with a separate copy of the DataFrame, preventing the `SettingWithCopyWarning` when modifying it.

## License
This project is licensed under the MIT License.

## Author
Developed by Yash Mittal. Version 1.0