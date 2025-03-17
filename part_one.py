def driver():  # The main function that runs the program
    print("-------------------------")
    print("Categorizing sequences...")
    print("-------------------------")
## List of DNA/RNA sequences
    all_sequences = [
        "GGGGGAAAGGCCCCTTTAAAACCCCTTTTTAAAACCCCCGGGAAAATTTTAAA",
        "GGGGGAAAUUCCCCTTTAAAACCCCUUUUUAAAACCCCCGGGAAAATTTTAAA",
        "CCCAAAAATTTTCCCCGGGTTAAAATTTTTGGGGGAAACCCGGGGAAAACCCCC",
        "CCCAAAAAGGGGCCCCCGGGGAAAACCCCGGGGGAAACCCGGGGAAAACCCCC"
    ]
# Dictionary to store categorized sequences
    categorized_sequences = {}
    categorized_sequences["undetermined"] = [] # Sequences that can't be identified
    categorized_sequences["dna"] = [] # dna sequances
    categorized_sequences["rna"] = [] # rna sequanses
    
# The issue is that category is returned as an integer (0, 1, or -1) from categorize_strand(sequence), but categorized_sequences uses string keys ("dna", "rna", and "undetermined")
#Since the dictionary keys are strings, using an integer key (0, 1, or -1) causes a KeyError.
# Loop through each sequence and categorize it
    for sequence in all_sequences:
        category = categorize_strand(sequence) # Get category as a number (0, 1, or -1)
        #bug==> Map numeric category to corresponding dictionary key
        if category == 0:
            category_key = "dna"
        elif category == 1:
            category_key = "rna"
        else:
            category_key = "undetermined"
        categorized_sequences[category_key].append(sequence) # Store in the correct category


    print("-------------------------")
    print("Encoding sequences for storage...")
    print("-------------------------")

    encoded_sequences = [] # List to store encoded sequences

    for sequence in all_sequences:
        encoded_strand = encode_strand(sequence) # Compress the sequence
        encoded_sequences.append(encoded_strand) # Add to list

    print("-------------------------")
    print("Listing undetermined sequences for review...")
    print("-------------------------")
#bug3==>prints uncategorized sequenses. 
    for sequence in categorized_sequences["undetermined"]:
        print(sequence) # Display sequences that couldn't be identified

# Returns 0 for DNA (Contains "T" bases)
# Returns 1 for RNA (Contains "U" bases)
# Returns -1 if the strand cannot be categorized: 
#   - Contains both "T" and "U" in the same strand 
#   - There are no "T" or "U" bases in the strand
def categorize_strand(strand): # Function to categorize a strand
    is_t_present = False  # Track if "T" exists
    is_u_present = False # Track if "U" exists

    for base in strand: # Loop through each character in the sequence
        if base == "T":
            is_t_present = True

        if base == "U":
            is_u_present = True

    has_both_bases = (is_t_present and is_u_present) # If both "T" and "U" exist
    has_neither_base = (not is_t_present and not is_u_present)  # If neither "T" nor "U" exist
    if (has_both_bases or has_neither_base):
        return -1 # Undetermined category

    return 0 if is_t_present else 1 # Return 0 for DNA, 1 for RNA
# Function to encode a DNA/RNA sequence
# Uses Run-Length Encoding (RLE) to compress repeated letters
def encode_strand(strand):
    if not strand: # If the sequence is empty, return an empty string
        return ""

    encoding = [] # List to store encoded data
    count = 1 # Count occurrences of each letter

    for index in range(1, len(strand)): # Start from second character
        if strand[index - 1] == strand[index]: # If same as previous letter
            count += 1  # Increase count
        else:#If a new character is found, store the previous character with its count
            new_entry = strand[index - 1] + str(count)# small bug==> converts the count into a string.
            encoding.append(new_entry) # Store previous letter and count
            count = 1 # Reset count
    #bug==> Add the last character and its count after the loop. Actually we were not storing data in our encoding list  
    new_entry = strand[-1] + str(count)
    encoding.append(new_entry)

    return "".join(encoding)  # Join list into a single string

# Function to decode a compressed strand back to original
def decode_strand(encoding):
    if not encoding: # If empty, return empty string
        return ""

    strand = [] # List to store expanded sequence

    for index in range(0, len(encoding) - 1, 2): # Loop over encoded pairs
        letter = encoding[index] # Get the letter
        count = int(encoding[index + 1]) # Get the count
        next_base = [letter] * count # Repeat the letter count times
        strand.extend(next_base) # Add to the list

    return "".join(strand) # Join list into a string
driver()