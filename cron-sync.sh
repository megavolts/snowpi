#!/bin/sh 

RSYNC=/usr/bin/rsync 
SSH=/usr/bin/ssh 
KEY=/home/megavolts/.ssh/id_rsa 
RUSER=sync
RHOST=66.230.87.226
RPORT=1507 
RPATH=SnowPi/data/
LPATH=/mnt/data/SnowPI/data/raw

TIMESTAMP=$(date +"%Y%m%d-%H_%M" -d @$(date +%s))


if [ -f $LPATH/log.txt ]
then
    mv $LPATH/log.txt $LPATH/log-$TIMESTAMP.txt
fi

if [ -f $LPATH/log.log ]
then
    mv $LPATH/log.log $LPATH/log-$TIMESTAMP.log
fi


$RSYNC -az -e "$SSH -i $KEY" $RUSER@$RHOST:$RPATH $LPATH --rsh='ssh -p'$RPORT  
