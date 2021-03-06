import pandas as pd # needed to read in and loop through meta file

import functional_analysis

# Set the file-name
filename = '../../data/metafile.csv'

# Read in the meta file
df = pd.read_csv(filename)

# Filter for only files with a GFF
df2 = df.dropna()

# Holder for all the gene names
all_gene_names = []

# For every list is the meta file
for index, row in df2.iterrows():
    # print('On row ' + str(index))

    # Collect the VCF
    vcfFileName = '../../../../joseline/data_for_analysis/' + row['sample name'] + '-4500T/' + row['sample name'] + '.vcf'
    # print(vcfFileName)

    # Collect the GFF file
    gffFileName = '../../data/GFFs/' + row['GFF File Name']
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

    # Get number of mutations
    nSNPS = functional_analysis.countVariants(Lines)

    # Get the names of genes with SNPS
    gene_names = functional_analysis.nVariantsPerGene(Lines, geneArray)

    # Test
    # print(gene_names)

    # Append to list for all organisms
    all_gene_names.append(gene_names)

# Save results from all to a file
textfile = open("../../results/functional_analysis/gene_names_from_all_samples.txt", "w")
for element in all_gene_names:
    textfile.write(element + "\n")
textfile.close()


    
