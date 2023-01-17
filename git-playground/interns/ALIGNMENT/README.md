<!-- This is readme.md for Alignment -->
# Prerequisites
To install EMBOSS suite and clustal Omega in MacOS:
```
brew install emboss
brew install clustalo
```
To install in EMBOSS suite in linux:
```
apt-get install emboss
apt-get install clustalo
```

# How it works 
## - To run pairwise_alignment.sh :
### 1. Arguments required:
- Input sequence 1 (fasta file)
- Input sequence 2 (fasta file)
- Needle file 
- Water file
- Output file (csv file)
### 2. Run the following command
```
./pairwise_alignment.sh input.fasta target.fasta output.needle output.water output.csv
```

## - To run msa.sh
### 1. Arguments required:
- Input file containing the multiple sequences 1 (fasta file)
- Output aligned sequences file name (fasta file)
- Output distance matrix file (csv file)
### 2. Run the following command
```
./msa.sh input.fasta output.fasta output.csv
```

## - To run dotmat.sh
### 1. Arguments required:
- Input sequence 1 (fasta file)
- Input sequence 2 (fasta file)
- Window size (integer)
- Threshold (integer)
### 2. Run the following command
```
./dotmat.sh input.fasta target.fasta 10 23
```

