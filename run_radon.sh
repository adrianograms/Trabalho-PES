#!/bin/bash

echo "cyclomatic complexity"
cat src/*.py | radon cc -

wait

echo "raw metrics"
cat src/*.py | radon raw -

wait

echo "maintainability index"
cat src/*.py | radon mi -

wait

echo "halstead metrics"
cat src/*.py | radon hal -
