#!/bin/bash

birdFirstName="emberiza"
birdSecondName="rustica"
#filename="$birdFirstName"_"$birdSecondName.txt"

# get number of pages

# for page 1 to n do
curl http://www.xeno-canto.org/species/$birdFirstName-$birdSecondName \
| grep download=* | cut -f 3 -d '<' | cut -f 3 -d '=' | cut -c 2- | rev | cut -c 3- | rev
#end
