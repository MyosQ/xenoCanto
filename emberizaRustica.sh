#!/bin/bash
birdFirstName="emberiza"
birdSecondName="rustica"
filename="$birdFirstName"_"$birdSecondName.txt"

curl http://www.xeno-canto.org/species/$birdFirstName-$birdSecondName > $filename

startline=`cat -n $filename | grep "<table class=\"results\">" | cut -f 1`
endline=`cat -n $filename | grep "<nav class=\"results-pages\">" | cut -f 1 | tail -1`

LINES=`wc -l $filename | cut -f 1 -d "e" | cut -c 5-`
let tailarg="-($LINES-$startline+2)"
let headarg="-($endline-$startline)"


cat $filename | tail $tailarg | head $headarg > temp.txt
cat temp.txt > $filename

let entry=0
let columnInEntry=0
while read LINE; do
   if [[ "$LINE" = *"<tr"* ]]; then
      let entry=entry+1
      let columnInEntry=0
   fi
   if [[ "$LINE" = *"<td"* ]]; then
      let columnInEntry=columnInEntry+1
   fi
   echo $entry  $columnInEntry $LINE


done < "$filename"
