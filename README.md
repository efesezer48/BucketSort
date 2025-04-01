# BucketSort

Bucket Sort Performance Benchmarking
Overview
This project implements and benchmarks a bucket sort algorithm optimized for sorting points in a 2D plane based on their Euclidean distance from the origin (0,0). The algorithm uses non-uniform bucket sizes to reflect the uniform area distribution within a unit circle. The code processes datasets of varying sizes (10, 100, 1,000, 100,000, and 10,000,000 points), measures the performance of the bucket sort, and exports the results to an Excel file.

Purpose
The goal of this project is to:

Demonstrate an efficient bucket sort implementation for distance-based sorting.
Analyze the algorithm’s performance across different dataset sizes.
Provide a reusable script for benchmarking sorting algorithms with CSV data.
Features
Loads 2D point data from CSV files.
Calculates Euclidean distances using NumPy for efficiency.
Implements a bucket sort with non-uniform bucket boundaries based on squared distance limits.
Benchmarks sorting time and saves results to an Excel file (bucket_sort_performance.xlsx).
Prerequisites
Python 3.x
Required libraries:

- pandas
- numpy
- openpyxl (for Excel file output)


Pre-provided datasets:
points_10.csv (10 points)
points_100.csv (100 points)
points_1000.csv (1,000 points)
points_100000.csv (100,000 points)
points_10000000.csv (10,000,000 points)
Ensure these files are in the same directory as the script. You can generate your own datasets or modify the file_paths dictionary to point to custom files.

Code Structure
Imports: Uses pandas for data handling, numpy for calculations, and time for benchmarking.
File Loading: The load_points function reads CSV files and computes Euclidean distances.
Bucket Sort: The bucket_sort function distributes points into buckets based on squared distance limits and sorts them.
Benchmarking: Measures execution time for each dataset and saves results to Excel.
Key Algorithm Details
Non-Uniform Buckets: Bucket boundaries are calculated as (i / num_buckets) ** 2 to ensure uniform area distribution within the unit circle.
Default Buckets: Set to 100 for benchmarking (adjustable via the num_buckets parameter)
Example Output
For aphysics bucket_sort_performance.xlsx might look like:

Size	Bucket Sort Time (s)
- 10	        ---------------    0.0023
- 100	        -------------    0.0051
- 1000	      ------------    0.0189
- 100000	    ---------    0.8924
- 10000000	 -----     92.3412
