from Bio.Align import MultipleSeqAlignment
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import matplotlib.pyplot as plt

# Create example sequences
seq1 = SeqRecord(Seq("ATGCTAGC"), id="Seq1")
seq2 = SeqRecord(Seq("ATG-TAGC"), id="Seq2")
seq3 = SeqRecord(Seq("ATGCT-GC"), id="Seq3")
seq4 = SeqRecord(Seq("AT-C-TGC"), id="Seq4")

# Create the alignment
alignment = MultipleSeqAlignment([seq1, seq2, seq3, seq4])

# Extract the sequences and their IDs
sequence_ids = [record.id for record in alignment]
sequences = [str(record.seq) for record in alignment]

# Define the dimensions of the plot
num_sequences = len(sequences)
sequence_length = len(sequences[0])

# Create the figure
plt.figure(figsize=(sequence_length / 2, num_sequences / 2))

# Visualize the alignment as text
for i, seq in enumerate(sequences):
    for j, char in enumerate(seq):
        plt.text(j, num_sequences - i - 1, char, fontsize=8, ha='center', va='center')

# Set up the axes
plt.xticks(range(sequence_length), range(1, sequence_length + 1), fontsize=8)
plt.yticks(range(num_sequences), sequence_ids, fontsize=8)
plt.xlabel("Position in Alignment")
plt.ylabel("Sequence ID")
plt.title("Multiple Sequence Alignment")

# Set axis limits
plt.xlim(-0.5, sequence_length - 0.5)
plt.ylim(-0.5, num_sequences - 0.5)

# Hide the plot frame
plt.gca().set_frame_on(False)
plt.grid(False)

# Display the plot
plt.tight_layout()
plt.show()
