#!/bin/bash -l

#$ -l h_rt=24:00:00   # Specify the hard time limit for the job
#$ -N depth-plots     # Give job a name
#$ -j y               # Merge the error and output streams into a single file
 
# Specify the version of MATLAB to be used
module load python3

# program name or command and its options and arguments
python make_plots.py