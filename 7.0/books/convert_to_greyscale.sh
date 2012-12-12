#!/bin/bash

shopt -s nullglob

TEXDIR=$1

if [ -f $TEXDIR/convert_started.txt ]; then
  echo
  echo -n "Images seems to be converted already,"
  if [ -f $TEXDIR/convert_ended.txt ]; then
    echo " and the conversion seems to be complete. I won't do it twice. Exiting."
    exit 0
  else
    echo " but it seems the convertion was not complete. I suggest you to execute the 'make clean' command"
  fi
  echo
fi

touch $TEXDIR/convert_started.txt

for img in $TEXDIR/*.png;
  do
    echo -n .
    cp $img ${img}.png.BAK
    convert $img -colorspace Gray ${img}.grey.png
    mv ${img}.grey.png $img
done
echo

for img in $TEXDIR/*.jpeg;
  do
    echo -n .
    cp $img ${img}.jpeg.BAK
    convert $img -colorspace Gray ${img}.grey.jpeg
    mv ${img}.grey.jpeg $img
done
echo


touch $TEXDIR/convert_ended.txt

