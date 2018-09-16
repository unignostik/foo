INVSECS=( "BEGIN:VCALENDAR" METHOD:REQUEST VERSION:2.0 BEGIN:VEVENT DTSTART: LOCATION: 'ORGANIZER;' "SUBJECT:Population Care View Training" PRIORITY:3 ) #vcalendar components

#generate html description
INVBODYTEMP="/Users/ct/Desktop/invBodyTemp.html"
INVBODY="/Users/ct/Desktop/invBody.html"
SKYPEURL="https:HOLDERwww.google.com"
NUM1URL="https:HOLDERwww.google.com"
NUM1="https:HOLDERwww.google.com"
LOCNUMURL="https:HOLDERwww.google.com"
PCODE="235512"
HELPURL="https:HOLDERwww.google.com"
sed "s/SKYPEURL/$SKYPEURL/g; s/NUM1URL/$NUM1URL/g; s/NUM1/$NUM1/g; s/LOCALNUMURL/$LOCNUMURL/g; s/PCODE/$PCODE/g; s/HELPURL/$HELPURL/g" "$INVBODYTEMP" > $INVBODY
sed "s;HOLDER;\/\/;g" "$INVBODY" > inv.html
DESC=$( echo -n "X-ALT-DESC;FMTTYPE=text/html:"; cat inv.html)

#generate organizer info
EMAIL="cwtillar@arkbluecross.com"
NAME="Chase Tillar"
NM=$( echo $NAME | sed 's/ /\:/g' )
MI=$( echo $EMAIL | cut -c 2-2 | tr "[a-z]" "[A-Z]" )
FIRST=$( echo $NM | cut -d: -f1 )
LAST=$( echo $NM | cut -d: -f2)
ORGNZR="ORGANIZER;CN=\"${LAST}, ${MI} ${FIRST}\":mailto:${EMAIL}" 

rm invBody.html
rm inv.html

#add vcalendar components to file
IFS=""
for SEC in ${INVSECS[*]}; do
  echo "${SEC}" >> inv.ics
done

echo $DESC >> inv.ics #add html component
echo $ORGNZR >> inv.ics #add organizer component

#end file
echo END:VEVENT >> inv.ics
echo END:VCALENDAR >> inv.ics
