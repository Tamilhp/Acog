function add {
           if [ $# -ge 2 ]
           then 
             echo $(($1 + $2));
           elif [ $# -ge 1 ]
           then
             echo $1;
           else
             echo 0;
           fi
          }
add $@
