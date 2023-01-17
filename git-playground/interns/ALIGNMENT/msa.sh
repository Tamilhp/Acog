#!/bin/sh
#Authors - Ankeet Annapur, Irum Hussain

#This code performs multiple sequence alignment on an input file (input.fasta) that contains all the sequences that need to be aligned
#Checking parameters and showing usage
if [ "$#" -ne 3 ]; then
    echo "Illegal number of parameters"
    echo "Usage: ./msa.sh input.fasta output.fasta output.csv"
    exit 1
fi

#Calling the clustal omega command
# IMPORTANT: The distmat-out paramter is required to receive the distance matrix, and the --full flag is required to convey the distance matrix
clustalo -i $1 -o $2 -v --distmat-out=$3 --full --force
awk '{print $1}' $3 | tr "\n" "," > header.txt #Formatting the csv to make it more readable
sed -i '' '$ s/.$/\n/' header.txt
sed -i '' 's/ \{1,\}/,/g' $3
sed -i '' '1d' $3
cat $3 >> header.txt
mv header.txt $3

# Usage - ./msa.sh 7HBA.fasta distance_matrix_file.csv
