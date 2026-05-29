# Day 2 - Linux File Management 🐧

## Environment
- OS: Windows 11 + WSL2 (Ubuntu)
- Linux user: `ankan_bioinfo`
- Workspace: `/home/ankan_bioinfo/`

## Commands Learned

| Command | What it does |
|---------|-------------|
| `cp` | Copy a file to a new location |
| `mv` | Move or rename a file |
| `rm` | Delete a file |
| `rmdir` | Remove an empty directory |
| `head` | View first lines of a file |
| `tail` | View last lines of a file |

## Practice Done
```bash
# Created a DNA project folder
mkdir dna_project
cd dna_project

# Created and wrote DNA sequence
touch dna.txt
echo "ATGCGTACCGTA" > dna.txt

# Viewed file content
head dna.txt
tail dna.txt

# Copied file as backup
cp dna.txt dna_backup.txt

# Renamed original file
mv dna.txt original_sequence.txt

# Deleted backup
rm dna_backup.txt

# Cleaned up — deleted file and folder
rm dna_project/original_sequence.txt
rmdir dna_project
```

## Errors & Fixes 🔧
```bash
$ cd dna.project
# Error: No such file or directory
# Fix: cd dna_project  ← used _ not .

$ cp dna_txt dna_sequence_txt
# Error: cannot stat 'dna_txt'
# Fix: cp dna.txt dna_backup.txt  ← missing dots

$ rm dna.project/original_sequence.txt
# Error: No such file or directory
# Fix: rm dna_project/original_sequence.txt  ← used _ not .
```

## Bioinformatics Connection 🔬
These commands are used daily in real bioinformatics:
- `cp` → backup genome files before processing
- `mv` → organize sequencing output files
- `rm` → clean up large temporary files
- `head/tail` → quickly preview FASTQ/FASTA sequence files

## Learning Resources
- 📺 [Linux Command Line Tutorial For Beginners | ProgrammingKnowledge](https://youtube.com/playlist?list=PLS1QulWo1RIb9WVQGJ_vh-RQusbZgO_As)

## Goal
Master Linux file management for handling
biological sequence files and genomics data. 🧬
