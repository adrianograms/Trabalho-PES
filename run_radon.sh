#!/bin/bash

echo "cyclomatic complexity"
cat src/*.py | radon cc -

echo "raw metrics"
cat src/*.py | radon raw -

echo "maintainability index"
cat src/*.py | radon mi -

echo "halstead metrics"
cat src/*.py | radon hal -
