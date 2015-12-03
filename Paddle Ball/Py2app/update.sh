#!/bin/sh
python setup.py py2app
zip -r PaddleBall-Mac.zip dist/PaddleBall.app/
mv PaddleBall-Mac.zip ../../Downloads/
rm -rf build dist
