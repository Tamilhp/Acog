#gets the options entered and performs accordingly based on case statements
usage() {
cat <<_EOF_
  Usage: ${0} -h -v -o <outputfile>
_EOF_
}
OPTIND=1
verbose=0

while getopts "h?vo": opt
do
    case "$opt" in
        h|\?) 
             usage
             exit 0
             ;;
        v) verbose=1
             echo "Verbose On"
             ;;
        o) output_file=$OPTARG
             echo "Using $OPTARG as the output"
             ;;
        *)
             echo "Unknown option"
             usage
             exit 0
             ;;
     esac
done
echo $OPTIND
shift $((OPTIND-1))
echo $OPTIND

echo "I am doing important stuff with $@"
