#! /bin/bash

#Authors : Ankeet Annapur , Irum Hussain
#check for arguments
if [ $# -ne 4 ]
  then
    echo "arguments not supplied "
    exit 1
fi
#Input for graph type
read -p " Select the graph type: " x

#Wrapper for dotmatcher
dotmatcher -asequence $1 -bsequence $2 -graph $x -windowsize $3 -threshold $4


