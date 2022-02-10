import plot_depth

id = "D20-160027"
genome_size = 4653851

plot_depth.plot_depth("./reports/" + id + ".depth", "plots/tests/" + id + "_depth_raw.png", "Raw Depth: Sample " + id, genome_size, False)