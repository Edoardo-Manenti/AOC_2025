#!/bin/bash

case "$1" in
    test)
        python -m unittest aoc
        ;;
    -h|--help)
        echo "Usage: $0 [test]"
        exit 1
        ;;
    *)
        python -m aoc
        ;;
esac

