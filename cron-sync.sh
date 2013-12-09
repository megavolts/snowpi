#!/bin/sh 

RSYNC=/usr/bin/rsync 
SSH=/usr/bin/ssh 
KEY=/home/megavolts/.ssh/id_rsa 
RUSER=sync
RHOST=66.230.87.226
RPORT=1507 
RPATH=SnowPi/data/
LPATH=/mnt/data/SnowPI/data/raw

$RSYNC -az -e "$SSH -i $KEY" $RUSER@$RHOST:$RPATH $LPATH --rsh='ssh -p'$RPORT  
