import pandas as pd
import matplotlib.pyplot as plt
import os

def depth_file_to_histogram(file_path, id, out_dir=".plots/"):
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
    # Check if the file is empty
    if os.stat(file_path).st_size == 0:
        raise ValueError(f'Cannot process the file at {file_path} because the '
                         f'file is empty.')
    
    # Create a dictionary with the column names as the keys and data types as
    # the values
    type_dict = {'genome_id': 'string', 'position': 'int', 'depth_count': 'int'}

    # Import the depth report as a tsv
    report_df = pd.read_csv(file_path,
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
    # If the output directory does not exist, make it
    isExist = os.path.exists(out_dir)
    if not isExist:
        os.makedirs(out_dir)
    
    # Plot
    plt.figure()
    plt.bar(x, y)
    plt.xlabel('Mapped Read Depth')
    plt.ylabel('Number of Reference Bases')
    plt.title('Sequencing Coverage of ' + id)

    # Save
    plt.savefig(out_dir + id + "_coverage_histogram.png")
    plt.close()


# TODO: Function: Check the interquartile range is within some value
def check_IQR(depth_dist):
    """
    
    Args:
    
    Returns:
    
    """
    pass

def plot_boxplots(data, labels, out_dir="./plots"):
    """ Create a single figure with a boxplot for each sample
    
    Args:
        data ([[]]): A list of lists of depths, each sub-list is an individual
            sample
        out_dir (string): Path to location to save the plots
    
    Returns:
        Nothing, plot is saved in out_dir
    """
    # If the output directory does not exist, make it
    isExist = os.path.exists(out_dir)
    if not isExist:
        os.makedirs(out_dir)
    
    # Make the figure, create axes instance
    fig, ax = plt.subplots()

    # Make the figure very large (good for plotting all of the samples at once)
    fig.set_figheight(10)
    fig.set_figwidth(20)

    # Adding title
    ax.set_title('Depth Box Plot')
    
    # Creating plot
    ax.boxplot(data)

    # Axis Labels
    ax.set_ylabel('Mapped Read Depth')
    ax.set_ylim(0, 400) # This will cut a few things off
    ax.set_xticklabels(labels)
    plt.xticks(rotation = 45) # Rotates X-Axis Ticks by 45-degrees

    # Save
    plt.savefig(out_dir + "coverage_boxplots.png")
    plt.close()

def collect_depth_list(report_df):
    depths = report_df['depth_count'].to_list()
    return(depths)

def  dir_to_boxplot(dir_path, out_dir="./plots"):
    """ Take directory of depth  reports and make a single file with a boxplot
    for each sample
    
    Args:
        dir_path(string): Path to the directory containing the depth reports
        out_dir (string): Path to location to save the plots
    
    Returns:
        Nothing, plot is saved in out_dir
    
    """
    # Initialize the list of labels and data
    labels = []
    data = []

    for filename in os.listdir(dir_path):
        # Path to that file
        file_path = dir_path + filename

        # Check that file is a file, if it is not, skip
        isFile = os.path.isfile(file_path)
        if not isFile:
            continue

        # Add the id to the label list
        id = filename.split('.')[0]
        labels.append(id)

        # Read in the file and make a dataframe
        report_df = read_depth_report(file_path)

        # Add the depth list to the data list
        data.append(collect_depth_list(report_df))

    # Make the plot
    print(labels)
    plot_boxplots(data, labels, out_dir)