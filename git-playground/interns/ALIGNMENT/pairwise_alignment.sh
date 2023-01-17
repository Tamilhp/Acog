#!/bin/sh

#Authors - Ankeet Annapur, Irum Hussain

#This code performs the pairwise alignment of 2 sequences using both the Needleman-Wunsch and Smith-Waterman algorithms and returns a CSV file

#Checking parameters and showing usage
if [ "$#" -ne 5 ]; then
    echo "Illegal number of parameters"
    echo "Usage: ./pairwise_alignment.sh input.fasta target.fasta output.needle output.water output.csv"
    exit 1
fi

#Range of input Gap Open Penalty Values
x=(1 10 20 30 40 50 60 70 80 90 100)
#Range of input Gap Extension Penalty Values
y=(0 1 2 3 4 5 6 7 8 9 10)

#Creating the first identifier row with relevant attributes along with required formatting
printf "Gap_Open_Penalty\tGap_Extension_Penalty\tGaps\tIdentity\tSimilarity\tScore" > $5
printf "\n" >> $5
printf "Needle Scores\n" >> $5
for i in ${!x[@]}; do
    #Wrapper for needle
    needle -asequence $1 -bsequence $2 -gapopen ${x[i]} -gapextend ${y[i]} -outfile $3
    #Using awk to parse the output needle file from command above and receiving the relevant scoring values
    awk 'BEGIN{FS=" "} NR==20 || NR==21 || NR==26 {printf "%s\t", $3}' $3 >> $5
    awk 'BEGIN{FS=" "} NR==24 || NR==25 {printf "%s\t", $4}' $3 | sed 's/(//g' | sed 's/)//g'>> $5
    awk 'BEGIN{FS=" "} NR==27 {printf "%s", $3}' $3 >> $5
    printf "\n" >> $5
done

printf "Water Scores\n" >> $5
for i in ${!x[@]}; do
    #Wrapper for water
    water -asequence $1 -bsequence $2 -gapopen ${x[i]} -gapextend ${y[i]} -outfile $4
    #Using awk to parse the output water file from command above and receiving the relevant scoring values
    awk 'BEGIN{FS=" "} NR==20 || NR==21 || NR==26 {printf "%s\t", $3}' $4 >> $5
    awk 'BEGIN{FS=" "} NR==24 || NR==25 {printf "%s\t", $4}' $4 | sed 's/(//g' | sed 's/)//g'>> $5
    awk 'BEGIN{FS=" "} NR==27 {printf "%s", $3}' $4 >> $5
    printf "\n" >> $5
done
