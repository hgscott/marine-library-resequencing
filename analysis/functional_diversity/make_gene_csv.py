from Bio import SeqIO

def main():
    gb_file1 = "../../../../Library_genomes/gbk/293.22.gbk"
    gb_file2 = "../../../../Library_genomes/gbk/272943.71.gbk"
    gbks = [gb_file1, gb_file2]

    # Make an empty matrix

    # Update the matrix with each set of gene names

    gb_record = SeqIO.read(open(gb_file,"r"), "genbank")
    gene_names = get_genes_in_gb(gb_record)
    print(len(gene_names))

    # Save as a csv

def get_genes_in_gb(gb_record):
    """
    Get a list of all genes in a given genbank file
    
    Args:
    - gb_record (): Open genbank file
    
    Returns:
    - A list of gene names
    """
    # Make an empty list to hold all of the gene names
    gene_names = []

    # Loop through the features and check if the feature is a gene and is named
    for feature in gb_record.features:
        if feature.type == "gene":
            if "gene" in feature.qualifiers:
                # Add the gene name to the list
                name = feature.qualifiers["gene"][0]
                gene_names.append(name)
                
    return(gene_names)


if __name__ == "__main__":
   main()