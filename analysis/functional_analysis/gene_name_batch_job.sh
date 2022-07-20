#!/bin/bash -l
#$ -l h_rt=25:00:00     # Specify the hard time limit for the job
#$ -j y                 # Merge the error and output streams into a single file
#$ -P hfsp
#$ -N SNP-genes         # Give job a name

module load python3

export PYTHONPATH=$PYTHONPATH:/projectnb/hfsp/Challenge21/helen/marine-library-resequencing/helper_functions

python gene_names_of_all_SNPs.py