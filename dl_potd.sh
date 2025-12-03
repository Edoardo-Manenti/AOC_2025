#!/bin/bash

year=$(date +"%Y")
day=$(date +"%d")

case "$1" in
    part-one)
	aoc-utils -y $year -d $day -b Template -s -i
        ;;
    part-two)
	aoc-utils -y $year -d $day -s 
        ;;
    -h|--help|*)
        echo "Usage: $0 [part-one|part-two]"
        exit 1
        ;;
esac

