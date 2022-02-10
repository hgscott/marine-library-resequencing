# !/usr/bin/env python3
# -*- coding: utf-8 -*-
 
import seaborn as sns
import numpy as np # FIXME: Remove if not needed
 
from matplotlib import (pyplot as plt,
                        lines)
 
 
def parse_depth(depth_input, genome_size):
    """Parse depth file.
 
    Args:
        depth_input (str): Path to depth file.
        genome_size (int): Genome size.
 
    Returns:
        list: List with depth.
 
    """

    # Make an empty array the length of the genome
    depth = [0] * genome_size
    references = set()
    i = 0
 
    with open(depth_input) as depth_object:
        for row in depth_object:
            genome_id, position, depth_count = row.split()
 
            references.add(genome_id)

            # Can only handle single contigs because the positions repeat, you'll overwrite your depth count
            # if len(references) > 1:
            #     raise Exception(' This script only handles one genome - contig.')
 
            # depth[int(position)-1] = int(depth_count)
            depth[i] = int(depth_count)
            i += 1
 
    return depth
 
 
def plot_depth(depth_report, output_name, plot_title, genome_size, normalize=False, depth_cut_off=20):
    """Plot genome Depth across genome.
 
    Args:
        depth_report (str): Path to samtool's depth file.
        output_name (str): Path to output PNG image.
        plot_title (str): Plot title.
        genome_size (int): Genome size.
        normalize (bool): If `True`, normalizes the depth by the largest depth (default = `False`).
        depth_cut_off (int): Plot a line to represent a targeted depth (default = 20).
 
    """
    data = parse_depth(depth_report, genome_size)
    
    plt.figure(figsize=(50,1))
    plt.plot(range(0, genome_size), data)
    plt.title(plot_title)
    plt.xlabel('Genome Position (bp)')
    plt.ylabel('Depth')

    plt.savefig(output_name, bbox_inches='tight', dpi=400)
    plt.close()
 
    # print("Done :)")