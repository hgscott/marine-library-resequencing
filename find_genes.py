# Modules
import pandas as pd
import re
import os

################################################################################
# Main function
################################################################################
def main():
    # For every VCF file
    for fileName in os.listdir('VCF files/'):

        # Collect the correct file paths/names
        vcfFileName = 'VCF files/' + fileName
        gffFileName = 'GFFs/' + fileName.split('.')[0] + '.gff'

        # Read in VCF file
        # Using readlines()
        vcfFile = open(vcfFileName, 'r')
        Lines = vcfFile.readlines()

        # Import GFF file
        gffArray = pd.read_csv(gffFileName, sep='\t')
        # Give column names
        gffArray.columns =['Sequence', 'Source', 'Feature', 'Start', 'End', 'Score', 'Strand', 'Phase', 'Attributes']
        # Select only for genes
        geneArray = gffArray[gffArray["Feature"] == "gene"]

        # Get the number of variants
        nVariants = countVariants(Lines)
        # Print the results
        print(vcfFileName + ": " + str(nVariants))

        # # Get the number of variants per gene
        # nVariantsPerGene(Lines, geneArray)
        # # 



    

################################################################################
## FUNCTIONS
################################################################################
def countVariants(vcfFileLines):
    # Intitate a counter
    counter = 0

    # For every line of the VCF
    for line in vcfFileLines:

        # Skip if it's in the header
        if line.startswith('#'):
            continue

        # If not in the header, it is an entry, up the counter
        counter += 1

    # Return the counter
    return(counter)


def nVariantsPerGene(vcfFileLines, geneArray):
    # For every line of the VCF
    for line in Lines:

        # Skip if it's in the header
        if line.startswith('#'):
            continue

        # Split the line into a list
        cols = line.split()

        # Extract the position
        pos = int(cols[1])

        # Look for the position in the GFF
        resLine = geneArray[(geneArray["Start"] < pos) & (geneArray["End"] > pos)]
        resLine = resLine.reset_index()
        

        # Skip if there are no results
        if len(resLine) < 1:
            continue

        # Save the gene name
        info = resLine["Attributes"][0]
        geneName = re.search(';gene=(.*?);', info)
        
        # Skip if there are no results
        if geneName is None:
            continue
        
        # Print
        print(geneName.group(1))

################################################################################
# Run the main function
################################################################################
if __name__ == "__main__":
    main()