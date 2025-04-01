import pandas as pd
import numpy as np
import time

# Define file paths 
file_paths = {
    "10": "points_10.csv",
    "100": "points_100.csv",
    "1000": "points_1000.csv",
    "100000": "points_100000.csv",
    "10000000": "points_10000000.csv",
}

# Function to load data from CSV
def load_points(file_path):
    df = pd.read_csv(file_path, header=None, names=["x", "y"])
    df["distance"] = np.sqrt(df["x"]**2 + df["y"]**2)
    return df

# Load data from all files
datasets = {size: load_points(path) for size, path in file_paths.items()}

# Implementing bucket sort with non-uniform bucket sizes
def bucket_sort(points, num_buckets=10):
    """Bucket sort for points distributed by area in the unit circle."""
    buckets = [[] for _ in range(num_buckets)]
    
    # Bucket boundaries reflecting the uniform area distribution
    bucket_limits = [(i / num_buckets) ** 2 for i in range(1, num_buckets + 1)]
    
    # Distribute points into buckets
    for dist in points["distance"]:
        for i, limit in enumerate(bucket_limits):
            if dist <= limit:
                buckets[i].append(dist)
                break
    
    # Sort individual buckets
    sorted_points = []
    for bucket in buckets:
        sorted_points.extend(sorted(bucket))
    
    return sorted_points

# Benchmarking bucket sort performance
sort_times = []

for size, df in datasets.items():
    distances = df["distance"].tolist()  # Convert DataFrame column to list
    
    # Timing bucket sort
    start_time = time.time()
    sorted_bucket = bucket_sort(pd.DataFrame({"distance": distances}), num_buckets=100)
    bucket_sort_time = time.time() - start_time
    
    # Store results
    sort_times.append({"Size": int(size), "Bucket Sort Time": bucket_sort_time})

# Convert to DataFrame
sort_results_df = pd.DataFrame(sort_times)

# Save results as an Excel file
excel_path = "bucket_sort_performance.xlsx"
sort_results_df.to_excel(excel_path, index=False)

print(f"Sorting performance saved to {excel_path}")
