# Day 1 - Linux Basics 🐧

## Environment Setup
- OS: Windows 11 + WSL2 (Ubuntu)
- Linux user: `ankan_bioinfo`
- Workspace: `/home/ankan_bioinfo/bioinformatics`

## Commands Learned

| Command | What it does |
|---------|-------------|
| `pwd` | Print current directory path |
| `ls` | List files in directory |
| `mkdir` | Create a new directory |
| `cd` | Change directory |
| `touch` | Create an empty file |
| `echo` | Write text to a file |
| `cat` | Read and display file content |

## Practice Done
```bash
# Created a bioinformatics workspace
mkdir bioinformatics
cd bioinformatics

# Created and wrote a DNA sequence file
touch dna.txt
echo "ATGCGTACCGT" > dna.txt
cat dna.txt
```

## What This Means Biologically
`ATGCGTACCGT` is a DNA sequence — later I'll write
Python scripts to analyze GC content, find patterns,
and parse FASTA files from this foundation.

## Goal
Master Linux for bioinformatics workflows — file handling,
sequence processing, and pipeline automation.
