DESC="X-ALT-DESC;FMTTYPE=text/html:CODE"
INVBODYTEMP="/Users/ct/Desktop/invBodyTemp.html"
INVBODY="/Users/ct/Desktop/invBody.html"
SKYPEURL="https:HOLDERwww.google.com"
NUM1URL="https:HOLDERwww.google.com"
NUM1="https:HOLDERwww.google.com"
LOCNUMURL="https:HOLDERwww.google.com"

PCODE="235512"
HELPURL="https:HOLDERwww.google.com"
sed "s/SKYPEURL/$SKYPEURL/g; s/NUM1URL/$NUM1URL/g; s/NUM1/$NUM1/g; s/LOCALNUMURL/$LOCNUMURL/g; s/PCODE/$PCODE/g; s/HELPURL/$HELPURL/g" "$INVBODYTEMP" > $INVBODY
sed 's;HOLDER;\//;g' "$INVBODY" > inv.html


