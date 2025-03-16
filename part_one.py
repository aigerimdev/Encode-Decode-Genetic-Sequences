def driver():
    print("-------------------------")
    print("Categorizing sequences...")
    print("-------------------------")

    all_sequences = [
        "GGGGGAAAGGCCCCTTTAAAACCCCTTTTTAAAACCCCCGGGAAAATTTTAAA",
        "GGGGGAAAUUCCCCTTTAAAACCCCUUUUUAAAACCCCCGGGAAAATTTTAAA",
        "CCCAAAAATTTTCCCCGGGTTAAAATTTTTGGGGGAAACCCGGGGAAAACCCCC",
        "CCCAAAAAGGGGCCCCCGGGGAAAACCCCGGGGGAAACCCGGGGAAAACCCCC"
    ]

    categorized_sequences = {}
    categorized_sequences["undetermined"] = [] # strands that can't be determined
    categorized_sequences["dna"] = [] # dna strands
    categorized_sequences["rna"] = [] # rna strands
# The issue is that category is returned as an integer (0, 1, or -1) from categorize_strand(sequence), but categorized_sequences uses string keys ("dna", "rna", and "undetermined")
#Since the dictionary keys are strings, using an integer key (0, 1, or -1) causes a KeyError.
    for sequence in all_sequences:
        category = categorize_strand(sequence)
        #bug==> Map numeric category to corresponding dictionary key
        if category == 0:
            category_key = "dna"
        elif category == 1:
            category_key = "rna"
        else:
            category_key = "undetermined"
        categorized_sequences[category_key].append(sequence)

    print("-------------------------")
    print("Encoding sequences for storage...")
    print("-------------------------")

    encoded_sequences = []

    for sequence in all_sequences:
        encoded_strand = encode_strand(sequence)
        encoded_sequences.append(encoded_strand)

    print("-------------------------")
    print("Listing undetermined sequences for review...")
    print("-------------------------")
#bug3==>prints uncategorized sequenses. 
    for sequence in categorized_sequences["undetermined"]:
        print(sequence)

# Returns 0 for DNA (Contains "T" bases)
# Returns 1 for RNA (Contains "U" bases)
# Returns -1 if the strand cannot be categorized: 
#   - Contains both "T" and "U" in the same strand 
#   - There are no "T" or "U" bases in the strand
def categorize_strand(strand):
    is_t_present = False
    is_u_present = False

    for base in strand:
        if base == "T":
            is_t_present = True

        if base == "U":
            is_u_present = True

    has_both_bases = (is_t_present and is_u_present)
    has_neither_base = (not is_t_present and not is_u_present)
    if (has_both_bases or has_neither_base):
        return -1

    return 0 if is_t_present else 1

def encode_strand(strand):
    if not strand:
        return ""

    encoding = []
    count = 1

    for index in range(1, len(strand)):
        if strand[index - 1] == strand[index]:
            count += 1
        else:#If a new character is found, store the previous character with its count
            new_entry = strand[index - 1] + str(count)# small bug==> converts the count into a string.
            encoding.append(new_entry)
            count = 1
    #bug==> Add the last character and its count after the loop. Actually we were not storing data in our encoding list  
    new_entry = strand[-1] + str(count)
    encoding.append(new_entry)

    return "".join(encoding)

def decode_strand(encoding):
    if not encoding:
        return ""

    strand = []

    for index in range(0, len(encoding) - 1, 2):
        letter = encoding[index]
        count = int(encoding[index + 1])
        next_base = [letter] * count
        strand.extend(next_base)

    return "".join(strand)
driver()