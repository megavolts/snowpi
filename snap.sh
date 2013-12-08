#!/bin/bash
#
# SnowPI
# 
# Marc Oggier
# Simon Filhol
#
# Updated December 9, 2013
# Version 2.1
#
## Man
# snap.sh [DIR]

APP=/usr/bin/uvccapture
TIMESTAMP=$(date +%s)
DIR=$1

$APP -B20 -C39 -S50 -v -x1600 -y1200 -otemp.jpg

TIMEH=$(date +"%Y-%m-%d-%H_%M" -d @$TIMESTAMP)

FILENAME=snow-$TIMEH.jpg
FILE=$FILENAME
cp temp.jpg current.jpg
mv temp.jpg $DIR/$FILE
 
echo -e "$FILENAME \t $TIMESTAMP \t jpg" > $DIR/temp.txt
