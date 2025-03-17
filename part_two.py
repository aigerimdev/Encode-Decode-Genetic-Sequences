from part_one import decode_strand, encode_strand

def driver():
    print("-------------------------")
    print("Encoding all sequences...")
    print("-------------------------")

    all_sequences = [
        "GGGGGAAAGGCCCCTTTAAAACCCCTTTTTAAAACCCCCGGGAAAATTTTAAA",
        "GGGGGAAAUUCCCCTTTAAAACCCCUUUUUAAAACCCCCGGGAAAATTTTAAA",
        "CCCAAAAATTTTCCCCGGGTTAAAATTTTTGGGGGAAACCCGGGGAAAACCCCC",
        "CCCAAAAAGGGGCCCCCGGGGAAAACCCCGGGGGAAACCCGGGGAAAACCCCC"
    ]
    encoded_sequences = [] # List to store encoded sequences

    for sequence in all_sequences: # Loop through each sequence
        encoded_strand = encode_strand(sequence) # Compress sequence
        encoded_sequences.append(encoded_strand) # Store encoded sequence


    print("-------------------------")
    print("Categorizing encoded sequences...")
    print("-------------------------")
 # Dictionary to store categorized sequences (using numbers as keys)
    categorized_sequences = {}
    categorized_sequences[-1] = []  # strands that can't be determined
    categorized_sequences[0] = []  # dna sequances
    categorized_sequences[1] = []  # rna equances

    for sequence in encoded_sequences: # Loop through encoded sequences
        category = categorize_strand(sequence) # Get category (0, 1, or -1)
        categorized_sequences[category].append(sequence) # Store in the correct category


    print("-------------------------")
    print("Decoding and listing undetermined sequences for review...")
    print("-------------------------")

    for sequence in categorized_sequences[-1]: # Loop through undetermined sequences
        decoded = decode_strand(sequence) # Convert back to original sequence
        print(decoded) # Print undecided sequences


# Returns 0 for DNA (Contains "T" bases)
# Returns 1 for RNA (Contains "U" bases)
# Returns -1 if the strand cannot be categorized:
#   - Contains both "T" and "U" in the same strand
#   - There are no "T" or "U" bases in the strand
def categorize_strand(strand):
    is_t_present = False # Track if "T" exists
    is_u_present = False # Track if "U" exists

    for base in strand:  # Loop through every character
        if base == "T":
            is_t_present = True
        if base == "U":
            is_u_present = True

    # Check if both "T" and "U" are present → Undetermined
    if is_t_present and is_u_present:
        return -1  #Both T and U present → Undetermined

    # Check if neither "T" nor "U" are present → Undetermined
    if not is_t_present and not is_u_present:
        return -1  #No T or U → Undetermined

    return 0 if is_t_present else 1  # Return 0 for DNA, 1 for RNA

#  has_both_bases = is_t_present and is_u_present
    # has_neither_base = (not is_t_present) and (not is_u_present)
    # if (has_both_bases or has_neither_base):
    #     return -1