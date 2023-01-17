#! /bin/bash
myString=" $(pwd)/rosalind_dna.txt"

myString="${myString,,}"
declare -A vowel=([a]=0 [c]=0 [g]=0 [t]=0 )
declare -l char

while IFS= read -r -d '' -n1 char; do 
    [[ -v "vowel[$char]" ]] && ((vowel[$char]++))
done < <(printf '%s' "$myString")

for char in "${!vowel[@]}"; do
    printf '%s\t%d\n' "$char" "${vowel[$char]}"
done | sort

