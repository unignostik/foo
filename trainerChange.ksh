TEMPHEAD="$3 trainees have been reassigned to $2"
TEMP="/Users/ct/Desktop/tnrChangeTemp.html"
sed "s/head/$TEMPHEAD/g;" "$TEMP" > inv.html
open /Users/ct/Desktop/inv.html
