#!/bin/sh
python setup.py py2app
rm -rf StickStory.app/
mv dist/StickStory.app/ .
rm -rf build dist
cp ../*.gif StickStory.app/Contents/Resources/
tar -zcvf StickStory.tar.gz StickStory.app/
