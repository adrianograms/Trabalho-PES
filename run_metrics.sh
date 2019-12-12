#!/bin/bash

echo "----------------------------------------"
echo "Cyclomatic complexity:"
cat src/*.py | radon cc - -a -s -o LINES
echo "----------------------------------------"
echo ""

wait

echo "----------------------------------------"
echo "Raw metrics:"
cat src/*.py | radon raw - -s
echo "----------------------------------------"
echo ""

wait

echo "----------------------------------------"
echo "maintainability index"
cat src/*.py | radon mi - -s -m
echo "----------------------------------------"
echo ""

wait

echo "----------------------------------------"
echo "halstead metrics"
cat src/*.py | radon hal - -f
echo "----------------------------------------"
echo ""
