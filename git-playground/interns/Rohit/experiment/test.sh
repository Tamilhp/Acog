#!/bin/bash

export LC_ALL=C
get_base_count () {
	echo $1  $(grep -o -F $1 $2 | wc -l)
}

get_base_count A $1 &
get_base_count T $1 & 
get_base_count C $1 & 
get_base_count G $1 &
wait

