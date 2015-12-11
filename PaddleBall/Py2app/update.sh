#!/bin/sh
python setup.py py2app
rm -rf PaddleBall.app/
mv dist/PaddleBall.app/ .
rm -rf build dist
