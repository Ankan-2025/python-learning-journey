dna_sequence = ("ATGCGTACCGTA")
count_A = 0
count_G = 0
count_T = 0
count_C = 0
i = 0
while( i < len(dna_sequence)):
    if(dna_sequence[i] == "A"):
        count_A += 1
    elif(dna_sequence[i] == "T"):
        count_T += 1
    elif(dna_sequence[i] == "G"):
        count_G += 1
    elif(dna_sequence[i] == "C"):
        count_C += 1
    i += 1
print(count_A)
print(count_G)
print(count_T)
print(count_C)
    
        
