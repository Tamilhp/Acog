#!/bin/bash

tmpfile=$(mktemp ~/tmp/tamil-XXX)
find $PWD | grep .py$ > $tmpfile

function get_time {
  mod_time=$(stat $1)
  mod_secs=$(date "mod_time" + %s)
  echo mod_secs
}

function clean {
rm -rf $tmpfile
}

time_stamp=$(get_time "./a.py")
for i in `cat $tmpfile`
do
  [[ $(get_time $i) -gt $time_stamp ]] && echo $i
done

trap 'clean; exit 1' 1 2 3 6
clean; exit 0
