#!/bin/bash -l
#$ -l h_rt=75:00:00
#$ -j y
#$ -P hfsp
#$ -pe omp 10

module load samtools

# Set path to the folders, must end in a *
path=../../../joseline/data_for_analysis/*

# For every sample
for dir in $path
do
    # Get the reference id
    id=$(basename $dir)
    echo $id

    # Generate the depth report
    # samtools depth {ALIGNMENT}.bam > {GENOME}.depth
done
