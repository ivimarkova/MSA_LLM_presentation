 from Bio import Phylo
 import matplotlib.pyplot as plt
 # Write the Newick string to a temporary file
 newick_tree =
"((Seq1:0.2,Seq2:0.3):0.5,(Seq3:0.1,Seq4:0.4):0.7);"
 with open("temp_tree.newick", "w") as file:
 file.write(newick_tree)
 # Read and parse the tree from the file
 tree = Phylo.read("temp_tree.newick", "newick")
 # Plot the tree
 fig = plt.figure(figsize=(8, 6))
 ax = fig.add_subplot(1, 1, 1)
 Phylo.draw(tree, do_show=False, axes=ax)
 plt.title("Phylogenetic Tree")
 plt.show()