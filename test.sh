#!/bin/sh

clear


FILES=./test/*.py
for f in $FILES
do
    echo ""
    echo "----- TEST: $f -----"
    echo ""
    python py_sym.py eval "$f"

    echo ""
    read -p "--> Press enter to run next test" yn
done
