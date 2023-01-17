tmpdir=mkdir $(mktemp ~/tmp/XXX)
function cleanup {
  echo "Cleaning $tmpdir"
  rm -rf $tmpdir
}

#creates a temp folder
#Starts creating temp files in that folder after every 10 seconds
#whenever we press <C-c> it gives SIGINT and cleanup is called
#The folder is cleaned up and it begins again


trap 'cleanup' TERM QUIT INT #whenever we press <C-c> it gives SIGINT and cleanup is called

echo "I am starting from beginning"
i=0

while true
do
  i=$(($i + 1))
  sleep 10; touch $tmpdir/$i
done
cleanup $@
