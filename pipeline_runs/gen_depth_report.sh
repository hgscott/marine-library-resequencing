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
    # Get the full reference id
    id=$(basename "$dir")

    # Remove the "-4500T" from the id
    # Hardcoded for the length of the shortname
    shortname=$(echo $id | cut -c1-10)

    # Get the full path for the sorted bam file 
    filename="${dir}/${shortname}.sorted.bam"

    # Set the output path to save in the working directory
    out="${shortname}.depth"

    # Generate the depth report
    samtools depth "$filename" > "$out"
done

# There were a few files without a sorted bam at that path
# [E::hts_open_format] Failed to open file "../../../joseline/data_for_analysis/D20-160069-4500T/D20-160069.sorted.bam" : No such file or directory
# samtools depth: Could not open "../../../joseline/data_for_analysis/D20-160069-4500T/D20-160069.sorted.bam": No such file or directory
# [E::hts_open_format] Failed to open file "../../../joseline/data_for_analysis/D20-160070-4500T/D20-160070.sorted.bam" : No such file or directory
# samtools depth: Could not open "../../../joseline/data_for_analysis/D20-160070-4500T/D20-160070.sorted.bam": No such file or directory
# [E::hts_open_format] Failed to open file "../../../joseline/data_for_analysis/D20-160077-4500T/D20-160077.sorted.bam" : No such file or directory
# samtools depth: Could not open "../../../joseline/data_for_analysis/D20-160077-4500T/D20-160077.sorted.bam": No such file or directory
# [E::hts_open_format] Failed to open file "../../../joseline/data_for_analysis/D20-160080-4500T/D20-160080.sorted.bam" : No such file or directory
# samtools depth: Could not open "../../../joseline/data_for_analysis/D20-160080-4500T/D20-160080.sorted.bam": No such file or directory
# [E::hts_open_format] Failed to open file "../../../joseline/data_for_analysis/D20-160084-4500T/D20-160084.sorted.bam" : No such file or directory
# samtools depth: Could not open "../../../joseline/data_for_analysis/D20-160084-4500T/D20-160084.sorted.bam": No such file or directory
# [E::hts_open_format] Failed to open file "../../../joseline/data_for_analysis/D20-160085-4500T/D20-160085.sorted.bam" : No such file or directory
# samtools depth: Could not open "../../../joseline/data_for_analysis/D20-160085-4500T/D20-160085.sorted.bam": No such file or directory
