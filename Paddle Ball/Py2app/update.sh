#!/bin/sh
rm -rf build dist
python setup.py py2app
zip -r PaddleBall.zip dist/PaddleBall.app/
mv PaddleBall.zip ../../Downloads/
