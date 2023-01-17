#! /bin/bash


#file= 'rosalind_dna.txt'
#echo $pwd
TEXT=" $(pwd)/rosalind_dna.txt"

declare -A arr=( ["A"]=0 ["C"]=0 ["G"]=0 ["T"]=0 )	
	

while read p ; do
	if (( p == "A"))
	then 
	    ((arr["A"]++))
        elif(( p == "C"))
        then 
            ((arr["C"]++)) 
        elif(( p == "G"))
        then
            ((arr["G"]++))
	elif(( p == "T"))
        then
            ((arr["T"]++))
        else 
	    continue
        fi	    

done < $TEXT
for val in "${arr[@]}"; do echo $val; done
