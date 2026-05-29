# Day 3 - Linux File Inspection & Navigation 🐧

## Environment
- OS: Windows 11 + WSL2 (Ubuntu)
- Linux user: `ankan_bioinfo`
- Workspace: `/home/ankan_bioinfo/`

## Commands Learned

| Command | What it does |
|---------|-------------|
| `ls -l` | List files with detailed info (permissions, size, date) |
| `ls -1` | List files one per line |
| `man` | Open manual/help for any command |
| `history` | Show all previously used commands |
| `clear` | Clear the terminal screen |
| `cd ..` | Move up one directory level |
| `cd ~` | Go back to home directory |

## Practice Done
```bash
# Created gene project folder and file
mkdir gene_project
touch gene.txt

# Listed files one per line
ls -1

# Checked detailed file info
ls -l

# Read manual for ls command
man ls

# Navigated back to home
cd ~
pwd   # Output: /home/ankan_bioinfo

# Checked full command history
history
```

## Understanding ls -l Output 🔍
```bash
drwxr-xr-x 2 ankan_bioinfo ankan_bioinfo 4096 May 27 bioinformatics
-rw-r--r-- 1 ankan_bioinfo ankan_bioinfo    0 May 29 gene.txt
```
- `d` = directory, `-` = file
- `rwxr-xr-x` = read/write/execute permissions
- `4096` = size in bytes
- `May 27` = last modified date

## Bioinformatics Connection 🔬
These commands are essential in real bioinformatics:
- `ls -l` → check file sizes of large genome/FASTQ files
- `man` → understand complex bioinformatics tool flags
- `history` → review and reproduce analysis workflows, an important aspect of reproducible bioinformatics research
- `cd ~` → navigate back to home between projects

## Key Takeaway 💡
Today I learned how to inspect files, navigate directories efficiently, access Linux documentation, and review command history.

These skills form the foundation for working with biological datasets, sequencing files, and bioinformatics tools from the command line.

## Learning Resources
- 📺 [Linux Command Line Tutorial For Beginners | ProgrammingKnowledge](https://youtube.com/playlist?list=PLS1QulWo1RIb9WVQGJ_vh-RQusbZgO_As)

## Goal
Master Linux navigation and file inspection for
managing and analyzing biological data files. 🧬
