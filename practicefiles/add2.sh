function add {
[[ $# -ge 2 ]] && echo $(($1+$2)) 
[[ $# -eq 1 ]] && echo $1 
[[ $# -eq 0 ]] && echo 0 
}
add $@
