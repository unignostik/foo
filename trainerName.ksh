EMAIL="cwtillar@arkbluecross.com"
NAME="Chase Tillar"
NM=$( echo $NAME | sed 's/ /\:/g' )

MI=$( echo $EMAIL | cut -c 2-2 | tr "[a-z]" "[A-Z]" )
FIRST=$( echo $NM | cut -d: -f1 )
LAST=$( echo $NM | cut -d: -f2)
ORGNZR="ORGANIZER;CN=\"${LAST}, ${MI} ${FIRST}\":mailto:${EMAIL}" 
echo $ORGNZR


