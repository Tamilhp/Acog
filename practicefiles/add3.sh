
function add3 { echo $(( ${1:-0} +  ${2:-0} )); }
add3 $@
