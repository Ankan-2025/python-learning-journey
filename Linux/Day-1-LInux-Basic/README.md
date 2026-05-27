# Day 1 - Linux Basics 🐧

## Environment Setup
- OS: Windows 11 + WSL2 (Ubuntu)
- Linux user: `ankan_bioinfo`
- Workspace: `/home/ankan_bioinfo/bioinformatics`

## Installation Reference
- 📺 [How to Install Ubuntu on Windows 11 (WSL2 Setup)](https://youtu.be/wjbbl0TTMeo?si=jiOeU1SjZCOOgWPp)

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

## Error & Fix
```bash
$ mkdir
mkdir: missing operand  ← forgot to add folder name

$ mkdir bioinformatics  ← fixed!
```

## What This Means Biologically
`ATGCGTACCGT` is a DNA sequence — later I'll write
Python scripts to analyze GC content, find patterns,
and parse FASTA files from this foundation.

## Installation Reference
- 📺 [How to Install Ubuntu on Windows 11 (WSL2 Setup)](https://youtu.be/wjbbl0TTMeo?si=jiOeU1SjZCOOgWPp)

## Learning Resources
- 📺 [Linux Command Line Tutorial For Beginners 1 - Introduction](https://youtu.be/YHFzr-akOas?si=1dkunwdq5El-9jtB)
- 📺 [Linux Command Line Tutorial For Beginners 2 - ls command](https://youtu.be/dQ8JgDUS8DA?si=NxWP1XwDBsPvz1aG)
- 📺 [Linux Command Line Tutorial For Beginners 3 - cd command](https://youtu.be/FTTr2bjI2UM?si=kwIUXcY2idVTHj9u)
- 📺 [Linux Command Line Tutorial For Beginners 4 - cat command](https://youtu.be/E01hskdRmUg?si=_Wkgh_T2oxixpR7A)
- 📺 [Linux Command Line Tutorial For Beginners 6 - mkdir command](https://youtu.be/qixSaXSUs-U?si=x9eQn8A2WAXV6TFY)
- 📺 [Linux Command Line Tutorial For Beginners 16 - echo command](https://youtu.be/tYmFsyH7VJY?si=orssWebOvj80aphT)

## Goal
Master Linux for bioinformatics workflows — file handling,
sequence processing, and pipeline automation.
