DNA = "ATGCGTACCGTA"
count_G=DNA.count("G")
count_C=DNA.count("C")
sequence_length=len(DNA)
GC_content= ((count_G + count_C)/sequence_length)*100
print("GC content % = ",round(GC_content, 2))