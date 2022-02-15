import pandas as pd

# Main function
# Take a file, read it, get the dists, plot
def plot_depth_file(depth_file, id, out_dir=".plots/"):
    pass

# Function: Take the file, make a pandas df
def read_depth_report(file_path):
    # Set the column names
    # Set the value types, str int and int

    # Import
    pass

# Function: Take the pandas df, get the distribution counts
def get_coverage_counts(report_df):
    # Make a list of just the depth values

    # x is the range of counts
    # set up y

    # For every value in x
    # Get the count

    # return x and y
    pass

# Function: Plot the distribution counts
def plot_coverage_histogram(x, y, id, out_dir=".plots/"):
    # matplot lib barchart
    # y labe; = Number of Reference Bases
    # X label = Mapped Read Depth
    pass

# TODO: Function: Check the interquartile range is within some value
def check_IQR(depth_dist):
    pass