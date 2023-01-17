ACOUNT=$(sed '1~4d;3~4d;4~4d' $1 | sed s/./\&~/g | tr "~" "\n" | grep "A" | wc -l)  
 CCOUNT=$(sed '1~4d;3~4d;4~4d' $1 | sed s/./\&~/g | tr "~" "\n" | grep "C" | wc -l)  
 GCOUNT=$(sed '1~4d;3~4d;4~4d' $1 | sed s/./\&~/g | tr "~" "\n" | grep "G" | wc -l)  
 TCOUNT=$(sed '1~4d;3~4d;4~4d' $1 | sed s/./\&~/g | tr "~" "\n" | grep "T" | wc -l)  
   
 # Adds up all the individual bases   
 TOTALBASES=$(($ACOUNT + $CCOUNT + $GCOUNT + $TCOUNT))  
   
 # Prints out both the number of hits for each base, and the percentage of that each base's contribution to the whole  
 echo "\n"  
 echo A bases: "\n"$ACOUNT "\n"Percentage A:  
 echo "scale=2;$ACOUNT/$TOTALBASES"*100 | bc  
 echo "\n"  
 echo C bases: "\n"$CCOUNT "\n"Percentage C:   
 echo "scale=2;$CCOUNT/$TOTALBASES"*100 | bc  
 echo "\n"  
 echo G bases: "\n"$GCOUNT "\n"Percentage G:   
 echo "scale=2;$GCOUNT/$TOTALBASES"*100 | bc  
 echo "\n"  
 echo T bases: "\n"$TCOUNT "\n"Percentage T:   
 echo "scale=2;$(($CCOUNT + $GCOUNT))/$TOTALBASES"*100 | bc  
