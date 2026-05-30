dna_sequence = ("ATGCGTACCGTA")
count_G = 0
count_C = 0
i=0
while(i < len(dna_sequence)):
    if(dna_sequence[i] == "G"):
        count_G += 1
    elif(dna_sequence[i] == "C"):
        count_C += 1
    i += 1
print("GC %=", ((count_G+count_C)/len(dna_sequence)) * 100)
