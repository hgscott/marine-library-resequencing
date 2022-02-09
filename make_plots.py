from socket import gethostbyname_ex
import pandas as pd # needed to read in and loop through meta file
import os # needed to loop through all the files in the depth report directory

import plot_depth

# Read in the metafile
filename = 'metafile.csv'
df = pd.read_csv(filename)

# Path to where the depth reports are saves
depth_path = "./QC_depth/reports/"

# For every file in that directory
for filename in os.listdir(depth_path):
    # Path to that file
    file_path = depth_path + filename

    # Get the sample id
    id = filename.split('.')[0]

    # Get the genome size from the metafile
    genome_size = int(df.loc[df['sample name'] == id, 'genome size'].iloc[0])
    print(genome_size)

    # Skip if the genome size is empty
    if genome_size == None:
        print("NO GENOME SIZE")

    # Run the plotting functions
    # raw depth
    # plot_depth.plot_depth(file_path, "plots/" + id + "_depth_raw.png", "Raw Depth: Sample " + id, genome_size, False)
    
    # # normalize depth
    # plot_depth.plot_depth("QC_depth/D20-160027.depth", "plots/" + id + "_depth_normalized.png", "Normalized Depth: Sample " + id, genome_size, True)