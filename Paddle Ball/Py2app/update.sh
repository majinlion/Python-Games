#!/bin/sh
python setup.py py2app
zip -r PaddleBall.zip dist/PaddleBall.app/
mv PaddleBall.zip ../../Downloads/
rm -rf build dist
