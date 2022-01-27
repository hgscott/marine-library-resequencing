import random
import pandas as pd
import re
from collections import Counter

# Give a results file
results = 'results/sample27.csv'

# Give a GFF
gffFileName = 'GFFs/sample27.gff'

# Define length of genome
lenGenome = 4653851

# Number of variants
nVariants = 26945

# Number of simulations to run
nSim = 10

# Read in the results file and make a dict of the results
res = dict()

resFile = open(results, 'r')
Lines = resFile.readlines()

for line in Lines:
    # Get gene name
    gene = line.split()[1]
    # Get number
    nVar = int(line.split()[0])
    # Add to dictionary
    res[gene] = nVar

# Import GFF file
gffArray = pd.read_csv(gffFileName, sep='\t')
# Give column names
gffArray.columns =['Sequence', 'Source', 'Feature', 'Start', 'End', 'Score', 'Strand', 'Phase', 'Attributes']
# Select only for genes
geneArray = gffArray[gffArray["Feature"] == "gene"]

# Make a dictionary to hold the p-values
pValues = dict()

for i in range(nSim):
    # Print a counter to keep an eye on how fast things are running
    # if i % 10 == 0:
    print(i)
    

    # Generate random positions for the total number of variants
    generatedVars = []
    for variant in range(nVariants):
        pos = random.randrange(lenGenome + 1)
        generatedVars.append(pos)

    # print(generatedVars)

    # Find the gene for each of the generated varaints
    genes = []
    for pos in generatedVars:
        # Find which line in the gff it is included in
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
        genes.append(geneName.group(1))

    sim = Counter(genes)

    # Check if the entries match or exceed the number if variants I saw
    for entry in res:
        # Pull the number of variants for that gene
        nVarRes = res[entry]

        # Is there an entry in the simulation for the gene
        if entry in sim.keys():
            # Pull the entry in the simulation for that gene
            nVarSim = sim[entry]   
        else:
            continue

        # Check if the number of variants is equal of higher in the simulation
        if nVarSim >= nVarRes:
            # Is there an entry in the simulation for the gene
            if entry in pValues.keys():
                # Increase the counter by 1
                pValues[entry]  += 1 
            else:
                # Add an entry and se the counter to 1
                pValues[entry]  = 1
        else:
            # Is there an entry in the simulation for the gene
            if entry in pValues.keys():
                # Increase the counter by 1
                continue
            else:
                # Add an entry and se the counter to 1
                pValues[entry]  = 0


    # print(pValues)

print(pValues)