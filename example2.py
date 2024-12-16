import matplotlib.pyplot as plt
import numpy as np

# Example data for alignment (replace with real data)
sequences = [
    "ATGCTAGC",
    "ATG-TAGC",
    "ATGCT-GC",
    "AT-C-TGC"
]
sequence_ids = ["Seq1", "Seq2", "Seq3", "Seq4"]

# Convert the alignment into a matrix
alignment_matrix = np.array([list(seq) for seq in sequences])

# Colors for different symbols
colors = {'A': 'green', 'T': 'blue', 'G': 'orange', 'C': 'purple', '-': 'lightgrey'}
colored_matrix = np.array([[colors.get(base, 'white') for base in row] for row in alignment_matrix])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 4))
for i, row in enumerate(colored_matrix):
    for j, color in enumerate(row):
        ax.add_patch(plt.Rectangle((j, len(alignment_matrix) - i - 1), 1, 1, color=color))

# Configure the axes
ax.set_xlim(0, alignment_matrix.shape[1])
ax.set_ylim(0, alignment_matrix.shape[0])
ax.set_xticks(range(alignment_matrix.shape[1]))
ax.set_yticks(range(alignment_matrix.shape[0]))
ax.set_yticklabels(sequence_ids)
ax.set_xticklabels(range(1, alignment_matrix.shape[1] + 1))
ax.set_xlabel("Position in Alignment")
ax.set_ylabel("Sequences")
ax.grid(False)
ax.set_title("Multiple Sequence Alignment Visualization")

# Display the plot
plt.show()
