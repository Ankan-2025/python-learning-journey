# Day 3 - Lists & Tuples 🐍🧬

## Topics Learned
- Lists — creation, indexing, slicing
- List Methods (`append`, `insert`, `sort`, `reverse`, `copy`, `remove`, `pop`)
- Tuples — immutable sequences
- Tuple Methods (`count`, `index`)

---

## Bioinformatics Connection 🔬

| Python Concept | Bioinformatics Use |
|----------------|-------------------|
| `list` | Store gene names, sequences, and analysis scores |
| `.append()` | Add newly discovered genes to a dataset |
| `.sort()` | Sort genes alphabetically or by expression level |
| `tuple` | Store fixed genomic coordinates |
| `list slicing` | Extract subsequence regions |

---

## Practice Problems

### 🧬 Bioinformatics Problems
1. Gene List Manager — store, access, and append cancer-related genes
2. DNA Complement Generator — generate a complementary DNA strand

### 🐍 Python Problems
3. Favourite Movies List using `append()`
4. Palindrome Checker using `copy()` and `reverse()`
5. Grade Counter and Sorter

---

## Files Added
- `gene_list_manager.py`
- `dna_complement_generator.py`
- `favourite_movies.py`
- `palindrome_checker.py`
- `grade_counter.py`

---

## Example — Gene List
```python
gene_list = ["TP53", "BRCA1", "EGFR"]
gene_list.append("MYC")
print(gene_list[:2])   # First 2 genes
print(gene_list[-1])   # Last added gene
```

---

## What This Means Biologically 🔬
Lists are used throughout bioinformatics for storing
and managing biological data such as:
- Gene expression values
- DNA and protein sequences
- Lists of cancer-related genes (e.g., TP53, BRCA1)
- Experimental results and sample identifiers

Tuples store fixed biological information like chromosomal
coordinates that should remain unchanged during analysis.

---

## Future Improvements 🚀
After learning loops, I plan to:
- Automate DNA complement generation
- Process longer DNA sequences
- Analyze multiple genes efficiently
- Build more realistic bioinformatics workflows
- Work with FASTA-style sequence data

---

## Learning Resources
- 📺 [Lecture 3 : List & Tuple in Python | Apna College](https://youtu.be/qVyvmzFxF_o?si=j2ri_fMYf-g-IBSU)
- 🌐 [FreeCodeCamp Python](https://www.freecodecamp.org/learn/python-v9/)

---

## Notes
[Lecture3_py.pdf](https://drive.google.com/file/d/1xGApxl-p67LLEWWv-QdlkwFREfWpRUMJ/view?usp=drive_link)

---

## Goal
Use Python data structures to store, organize, and
manipulate biological data such as gene lists, genomic
coordinates, and DNA sequences as preparation for
future bioinformatics projects. 🧬
