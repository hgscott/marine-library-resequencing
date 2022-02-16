# Functions associated with the functional analysis of VCF files

import re

def countVariants(vcfFileLines):
    """Return the number of variants in a VCF file"""
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
    """Print the name of every gene with a SNP in it"""
    # Make a list to hold all the gene names
    gene_names = []

    # For every line of the VCF
    for line in vcfFileLines:

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
        gene_names.append(geneName.group(1))

    return(gene_names)