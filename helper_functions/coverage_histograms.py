import pandas as pd
import matplotlib.pyplot as plt

def plot_depth_file(file_path, id, out_dir=".plots/"):
    """ Takes a depth file, reads it in to a dataframe, gets the distribution of
    the depths and saves a plot of the coverage histogram
    
    Args:
        file_path (string): Path to the depth report file
        id (string): Sample name for the output file name
        out_dir (string): Path to the folder where you want to save the plot
    
    Returns:
        Nothing, saves a plot in the specified output directory
    """
    # Read in the file and make a dataframe
    report_df = read_depth_report(file_path)

    # Get the distribution of the depths
    x, y = get_coverage_counts(report_df)

    # Plot the distribution
    plot_coverage_histogram(x, y, id, out_dir)


def read_depth_report(file_path):
    """ Read in a .depth file and make a pandas data frame of columns with the
    following names and types:
        * genome_id (string)
        * position (int)
        * depth_count (int)
    
    Args:
        file_path (string): Path to the depth report file
    
    Returns:
        report_df (Pandas.DataFrame): Dataframe with the info from the dept
            report file. The columns are genome_id (string), position (int), and
            and depth_count (int)
    
    """
    # Create a dictionary with the column names as the keys and data types as
    # the values
    type_dict = {'genome_id': 'string', 'position': 'int', 'depth_count': 'int'}

    # Import the depth report as a tsv
    report_df = pd.import_csv(file_path,
                              sep='\t',
                              names=type_dict.keys(),
                              dtype=type_dict)
    
    # Return the dataframe
    return(report_df)


# Function: Take the pandas df, get the distribution counts
def get_coverage_counts(report_df):
    """ Make lists of the range of depth values and their counts
    
    Args:
        report_df (Pandas.DataFrame): Dataframe with the info from the dept
            report file. The columns are genome_id (string), position (int), and
            and depth_count (int)
    
    Returns:
        x ([int]): Coverage values
        y ([int]): Number of times the coverage values occurs in the depth file
    
    """
    # Make a list of just the depth values
    depths = report_df['depth_count'].to_list()

    # Get a list of the depths in the report and the counts for each depth
    x = [*range(min(depths), max(depths) + 1)]
    y = []

    for i in x:
        y.append(depths.count(i))

    # Return x and y
    return x, y


# Function: Plot the distribution counts
def plot_coverage_histogram(x, y, id, out_dir=".plots/"):
    """ Make and save a coverage histogram plot
    
    Args:
        x ([int]): Coverage values
        y ([int]): Number of times the coverage values occurs in the depth file
    
    Returns:
        Nothing, saves a plot in the specified output directory
    """
    # Plot
    plt.bar(x, y)
    plt.xlabel('Mapped Read Depth')
    plt.ylabel('Number of Reference Bases')

    # Save
    plt.savefig(out_dir + id + "_coverage_histogram.png")
    plt.close


# TODO: Function: Check the interquartile range is within some value
def check_IQR(depth_dist):
    """
    
    Args:
    
    Returns:
    
    """
    pass