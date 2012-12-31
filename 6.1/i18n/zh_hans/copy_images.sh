#!/bin/sh

SRC_IMAGE_DIR=source/features/images
DEST_IMAGE_NORMAL_DIR=build/html/images
DEST_IMAGE_SMALL_DIR=build/html/images_small

VERBOSE=0

echo 'copying images'

# create directory if it does not exists:
if [ ! -d $DEST_IMAGE_SMALL_DIR ]; then
  if [ $VERBOSE = 1 ]; then
    echo creating directory: $DEST_IMAGE_SMALL_DIR
  else
    echo .'\c'
  fi
  mkdir -p $DEST_IMAGE_SMALL_DIR || exit
fi

if [ ! -d $DEST_IMAGE_NORMAL_DIR ]; then
  if [ $VERBOSE = 1 ]; then
    echo creating directory: $DEST_IMAGE_NORMAL_DIR
  else
    echo .'\c'
  fi
  mkdir -p $DEST_IMAGE_NORMAL_DIR || exit
fi

for f in ${SRC_IMAGE_DIR}/*.png; do
  baseimage=$(basename $f)
  if [ $VERBOSE = 1 ]; then
    echo converting image $f in ${DEST_IMAGE_SMALL_DIR}/${baseimage}
  else
    echo .'\c'
  fi
  #convert -geometry 350x350 $f ${DEST_IMAGE_SMALL_DIR}/${baseimage} || exit
  if [ $VERBOSE = 1 ]; then
    echo copying image $f in ${DEST_IMAGE_NORMAL_DIR}
  else
    echo .'\c'
  fi
  cp -f $f $DEST_IMAGE_NORMAL_DIR || exit
done;

