function rename_file {
for i in "$@"
do 
  mv ./$i ./$(echo $i | sed -e "s/' '/_/" | tr A-Z a-z)
done
}
rename_file $@
