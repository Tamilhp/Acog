#!/bin/bash

set -e

# Variables
sleep_var=1
default_col_var="6 qseqid sseqid qstart qend sstart send evalue score pident"
output_var="6"



#######################################
echo "######################################################################################################"
echo "######################################################################################################"
echo "                                "
echo "                                "
echo "######################################################################################################"
echo "########################################### BLAST DB #################################################"
echo "######################################################################################################"
echo "                                "
echo "                                "
echo "######################################################################################################"
echo "######################################################################################################"
#######################################



echo "                                "
echo "                                "
echo "######################################################################################################"
echo "                                                      "
echo "Select a Local BLAST DB to search a query sequence:"
echo "                                                      "
echo "1. Hemoglobin Alpha Subunit Protein"
echo "2. Hemoglobin Beta Subunit Protein"
echo "3. Mazie Transcription Factors Protein - ZMTF PEP"
echo "4. Mazie Transcription Factors Nucleotides - ZMTF CDS"
echo "                                                      "
read -p "Local BLAST DB ==> " seq_var
echo "                                                      "
echo "######################################################################################################"
echo "                                "
echo "                                "


# Selecting specific BLAST DB to fire the qurey seq's
if [[ $seq_var -eq 1 ]]
then db="Hemoglobin Alpha Subunit Protein BLAST DB"
     blast_db="/home/acog/BLAST_Testing/hemoglobin_alpha_subunit"
elif [[ $seq_var -eq 2 ]]
then db="Hemoglobin Beta Subunit Protein BLAST DB"
     blast_db="/home/acog/BLAST_Testing/hemoglobin_beta_subunit/reference"
elif [[ $seq_var -eq 3 ]]
then db="Mazie Transcription Factors Protein BLAST DB"
     blast_db="/home/acog/BLAST_Testing/mazie_transcription_factors/ref_pep/ref"
elif [[ $seq_var -eq 4 ]]
then db="Mazie Transcription Factors Nucleotides BLAST DB"
     blast_db="/home/acog/BLAST_Testing/mazie_transcription_factors/ref_cds/ref"
else
     db="Invalid BLAST DB"
     blast_db="Path is void"
fi



echo "                                "
echo "                                "
echo "######################################################################################################"
echo "                                                      "
echo "DB selected is $db and it is in path: $blast_db"
echo "                                                      "
echo "######################################################################################################"
echo "                                "
echo "                                "



echo "                                "
echo "                                "
echo "######################################################################################################"
echo "                                                      "
echo "Check and input all the fields needed in the report:"
echo "                                                      "
echo "These are some of the supported format specifiers, "
echo "if need be please check further by using < blastp -help >"
echo "                                                      "

echo "   	    qseqid means Query Seq-id"
echo "  	       qgi means Query GI"
echo "   	      qacc means Query accesion"
echo "   	      qlen means Query sequence length"
echo "   	    sseqid means Subject Seq-id"
echo "   	      slen means Subject sequence length"
echo "   	    qstart means Start of alignment in query"
echo "   	      qend means End of alignment in query"
echo "   	    sstart means Start of alignment in subject"
echo "   	      send means End of alignment in subject"
echo "   	      qseq means Aligned part of query sequence"
echo "   	      sseq means Aligned part of subject sequence"
echo "  	    evalue means Expect value"
echo "   	     score means Raw score"
echo "   	    length means Alignment length"
echo "   	    pident means Percentage of identical matches"
echo "   	      gaps means Total number of gaps"
echo "   	      ppos means Percentage of positive-scoring matches"


echo "                                                      "
echo "Here are the default input fields, you can hit ENTER to proceed ==> 'qseqid sseqid qstart qend sstart send evalue score pident'"
echo "  OR"
echo "You may change it manually for specific format specifiers separated with a space ..."
sleep $sleep_var
echo "                                                      "



read -p "Please enter the columns in the output csv ==> " col_var
temp_var=`echo $col_var | wc -c`
echo "                                                      "
echo "                                                      "
echo "######################################################################################################"



echo "                                                      "
read -p "Provide the fasta sequence location(.fa file) or a query sequence to search against the BLAST DB ==> " query_sequence
echo "                                "
read -p "Enter the threshold of the query-subject sequence match percentage to filter the data ==> " threshold
echo "                                "
echo "######################################################################################################"



if [[ $seq_var -eq 4 ]]
then
       if [[ temp_var -gt 2  ]]
	then
		echo "                                "
		echo "                                "
		echo "######################################################################################################"
        	echo "                                                      "
		echo "Running the query >>> blastn -db $blast_db -query $query_sequence -outfmt $default_col_var > $HOME/results.csv"
        	blastp -db $blast_db -query $query_sequence -outfmt "$output_var $col_var"  > $HOME/results.csv
		echo "                                                      "
                echo "######################################################################################################"
		echo "                                "
		echo "                                "
	else
		echo "                                "
		echo "                                "
                echo "######################################################################################################"
		echo "                                                      "
                echo "Running the query >>> blastn -db $blast_db -query $query_sequence -outfmt $default_col_var > $HOME/results.csv"
        	blastn -db $blast_db -query $query_sequence -outfmt "6 qseqid sseqid qstart qend sstart send evalue score pident" > $HOME/results.csv
		echo "                                                      "
		echo "######################################################################################################"
                echo "                                "
		echo "                                "
	fi

else
       if [[ temp_var -gt 2  ]]
	then
		# default_col_var="${output_var}${col_var}"
		default_col_var= echo "'`$output_var $col_var`'"
		echo "                                "
		echo "                                "
                echo "######################################################################################################"
		echo "                                                      "
		echo "Running the query >>> blastp -db $blast_db -query $query_sequence -outfmt '$output_var $col_var' > $HOME/results.csv"
		blastp -db $blast_db -query $query_sequence -outfmt "$output_var $col_var"  > $HOME/results.csv
		# blastp -db $blast_db -query $query_sequence -outfmt $default_col_var > $HOME/results.csv
		echo "                                                      "
		echo "######################################################################################################"
                echo "                                "
		echo "                                "
	else
		echo "                                "
		echo "                                "
                echo "######################################################################################################"
		echo "                                                      "
                echo "Running the query >>> blastn -db $blast_db -query $query_sequence -outfmt $default_col_var > $HOME/results.csv"
		blastp -db $blast_db -query $query_sequence -outfmt "6 qseqid sseqid qstart qend sstart send evalue score pident" > $HOME/results.csv
		echo "                                                      "
		echo "######################################################################################################"
                echo "                                "
		echo "                                "
	fi
fi

echo "                                "
#echo "Running the query ### blastp -db $blast_db -query $query_sequence -outfmt $default_col_var > $HOME/results.csv"
#blastp -db $blast_db -query $query_sequence -outfmt $default_col_var > $HOME/results.csv
#echo "                                "
#echo "                                "
# echo "Here is the path of the results generated as part of Local BLAST search ==> `pwd`"
echo "                                "
echo "                                "
echo "######################################################################################################"
echo "############################################# RESULTS ################################################"
echo "######################################################################################################"
echo "                                "
echo "                                                      "
chmod 700 $HOME/results.csv
echo "There are around `less $HOME/results.csv | wc -l` sequence matches"
echo "                                                      "
echo "Here are the results generated for the query sequence $query_sequence against"
echo "the Local BLAST DB: $db are here==> $HOME/results.csv"
echo "                                                      "
echo "                                "
echo "######################################################################################################"
echo "                                "
echo "                                "


less $HOME/results.csv

exit