#!/bin/bash

TOTAL_COUNT=$(cat $1 | wc -c)

get_counts() {
	export LC_ALL=C
	COMPLEMENT=$(sed "s/$1//g" $2 | wc -c)
	echo $1 $((TOTAL_COUNT - COMPLEMENT))
}
get_counts A $1 &
get_counts C $1 &
get_counts T $1 &
get_counts G $1 &
wait
