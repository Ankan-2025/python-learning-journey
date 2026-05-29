dna_sequence= ("ATGCGT")
if(dna_sequence[0] == "A"):
    complementary = "T"
    if(dna_sequence[1] == "T"):
        complementary = "T" + "A"
        if(dna_sequence[2] == "G"):
            complementary = "TA" + "C"
            if(dna_sequence[3] == "C"):
                complementary = "TAC" + "G"
                if(dna_sequence[4] == "G"):
                    complementary = "TACG" + "C"
                    if(dna_sequence[5] == "T"):
                        complementary= "TACGC" + "A"
                        print(complementary)