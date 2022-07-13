import os # Needed to loop through all the files in a directory

# Import helper functions needed
import coverage_histograms

# Set the directory with the depth reports
depth_path = '../../data/depth_reports/'

# Set the output directory
out_dir = '../../results/plots/coverage/coverage_histograms/'

# Loop through all of the depth reports
for filename in os.listdir(depth_path):
    # Path to that file
    file_path = depth_path + filename

    # Get the sample id
    id = filename.split('.')[0]

    # Run the plotting function
    coverage_histograms.plot_depth_file(file_path, id, out_dir)

