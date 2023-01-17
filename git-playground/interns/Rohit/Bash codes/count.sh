#! /bin/bash

echo "count of A: "
grep -o "A" <<< "$seq" | wc -l
echo "count of C: "
grep -o "C" <<< "$seq" | wc -l
echo "count of G: "
grep -o "G" <<< "$seq" | wc -l
echo "count of T: "
grep -o "T" <<< "$seq" | wc -l


echo "Implementing with method 2: "

echo "Count of A by method 2: "
char="A"
awk -F"${char}" '{print NF-1}' <<< "${seq}"

echo "Count of C by method 2: "
char="C"
awk -F"${char}" '{print NF-1}' <<< "${seq}"

echo "Count of G by method 2: "
char="G"
awk -F"${char}" '{print NF-1}' <<< "${seq}"

echo "Count of T by method 2: "
char="T"
awk -F"${char}" '{print NF-1}' <<< "${seq}"