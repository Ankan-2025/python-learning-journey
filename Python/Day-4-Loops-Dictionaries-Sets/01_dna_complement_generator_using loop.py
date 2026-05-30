dna_sequence = ("ATGCGTACCGTA")
i = 0
complement = ""
while (i < len(dna_sequence)):
    if(dna_sequence[i] == "A"):
        complement += "T"
    elif(dna_sequence[i] == "T"):
        complement += "A"
    elif(dna_sequence[i] == "G"):
        complement += "C"
    elif(dna_sequence[i] == "C"):
        complement += "G"
    i += 1
print(complement)
    
