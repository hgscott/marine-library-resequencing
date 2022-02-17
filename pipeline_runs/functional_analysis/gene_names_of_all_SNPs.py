import pandas as pd # needed to read in and loop through meta file
import os

import functional_analysis # The helper functions I wrote for functional analysis

# Set the path to the metafile
# This is assuming you are running this script from inside the directory where this file is saves
filename = '../../data/metafile.csv'

# Read in the meta file
df = pd.read_csv(filename)

# Filter for only files with a GFF
df2 = df[df['gff file name'].notna()]

# Holder for all the gene names
all_gene_names = []

# For every list is the meta file
for index, row in df2.iterrows():
    # print('On row ' + str(index))

    # Collect the VCF
    vcfFileName = '../../../../joseline/data_for_analysis/' + row['sample name'] + '-4500T/' + row['sample name'] + '.vcf'
    # You can uncomment the print statements to check if you are getting the right strings for the file paths
    # print(vcfFileName)

    # Collect the GFF file
    gffFileName = '../../data/GFFs/' + row['gff file name']
    # print(gffFileName)

    # Read in VCF file
    # Using readlines()
    vcfFile = open(vcfFileName, 'r')
    Lines = vcfFile.readlines()

    # Import GFF file, skipping the header lines
    gffArray = pd.read_csv(gffFileName, sep='\t', comment='#')
    # Give column names
    gffArray.columns =['Sequence', 'Source', 'Feature', 'Start', 'End', 'Score', 'Strand', 'Phase', 'Attributes']
    # Select only for genes
    geneArray = gffArray[gffArray["Feature"] == "gene"]

    # Get the number of mutations in that VCF file
    nSNPS = functional_analysis.countVariants(Lines)

    # Get the names of genes with SNPS
    gene_names = functional_analysis.nVariantsPerGene(Lines, geneArray)

    # Test
    # print(gene_names)

    # Append to list for all organisms
    all_gene_names.append(gene_names)

# Set the path to where you want to save the output file
out_dir = "../../results/functional_analysis/"
# If that folder does not exist, make it
isExist = os.path.exists(out_dir)
if not isExist:
    os.makedirs(out_dir)

# Save results from all to a fil
textfile = open(out_dir + "gene_names_from_all_samples.txt", "w")
for element in all_gene_names:
    textfile.write(element + "\n")
textfile.close()


    
