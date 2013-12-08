#!/bin/bash
 
APP=/usr/bin/uvccapture
TIMESTAMP=$(date +%s)
$APP -B20 -C39 -S50 -v -x1600 -y1200 -otemp.jpg

TIMEH=$(date +"%Y-%m-%d-%H_%M" -d @$TIMESTAMP)

FILENAME=snow-$TIMEH.jpg
FILE=$FILENAME
cp temp.jpg current.jpg
mv temp.jpg ./pics/$FILE
 
echo -e "$FILENAME \t $TIMESTAMP \t jpg" > temp.txt
