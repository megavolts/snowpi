#!/bin/sh
#
# SnowPI
# Marc Oggier
# Simon Filhol
#
#
# source : http://troy.jdmz.net/rsync/index.html

case "$SSH_ORIGINAL_COMMAND" in
*\&*)
echo "Rejected"
;;
*\(*)
echo "Rejected"
;;
*\{*)
echo "Rejected"
;;
*\;*)
echo "Rejected"
;;
*\<*)
echo "Rejected"
;;
*\`*)
echo "Rejected"
;;
*\|*)
echo "Rejected"
;;
rsync\ --server*)
$SSH_ORIGINAL_COMMAND
;;
*)
echo "Rejected"
;;
esac
