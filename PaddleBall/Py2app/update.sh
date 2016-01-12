#!/bin/sh
python setup.py py2app
rm -rf PaddleBall.app/
mv dist/PaddleBall.app/ .
tar -zcvf PaddleBall.tar.gz PaddleBall.app/
rm -rf build dist
