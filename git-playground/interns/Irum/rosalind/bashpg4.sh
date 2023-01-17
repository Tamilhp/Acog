#! /bin/bash
 
function parse(){
	local seqno=-1
	local line
        file='rosalind_gc.txt'
	while read line 
	do
		if [ ${line:0:1}=">" ]
		then
			((seqno++))
		        seqidentifier{$seqno}=${line:1}
		else
		        seqData[$seqno]+=$line
		fi
	done<$file


}
declare -a seqidentifier
declare -a seqData
parse 

