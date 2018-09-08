WHEN="DTSTART:"$1"T"$2"Z"
LOC="LOCATION:"$3
SUM="SUMMARY:Invitation for Training with "$4
INVTEMP="/home/bpmadmin/bin/foo/invTemp.txt"
sed "s/DTSTART:/$WHEN/g; s/LOCATION:/$LOC/g; s/SUMMARY:/$SUM/g" "$INVTEMP" > inv.vcs
