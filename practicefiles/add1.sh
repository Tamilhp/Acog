function add {
case "$#" in 
0) echo 0;;
1) echo $1;;
*) echo `expr $1 + $2`;;
esac
}
add $@
