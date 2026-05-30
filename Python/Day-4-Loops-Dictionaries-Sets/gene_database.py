gene = {
    "TP53": "Tumor Suppressor",
    "BRCA1": "DNA Repair",
    "EGFR": "Growth Receptor"
}
print(gene)
gene.update({"MYC": "Cell Growth Regulation"})
print(gene)
print(gene.get("TP53"))

            