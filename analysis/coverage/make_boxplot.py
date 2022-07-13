# Import helper functions needed
import coverage_histograms

# Set the directory with the depth reports
depth_path = '../../data/depth_reports/'

# Set the output directory
out_dir = '../../results/plots/coverage/boxplots/'

coverage_histograms.dir_to_boxplot(depth_path, out_dir)