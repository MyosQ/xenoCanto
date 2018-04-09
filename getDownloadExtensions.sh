#!/bin/bash

# Given the birds first and secondName, this script echos
# the url's to stdout and adds the specifications of each
# recording to the database

birdFirstName=$1 #Firstname
birdSecondName=$2 #Secondname


#filename="$birdFirstName"_"$birdSecondName.txt"

# get number of pages
numOfPages=`curl http://www.xeno-canto.org/species/$birdFirstName-$birdSecondName | grep "href=\"?pg" |\
 tail -2 | head -1 | sed 's/.*<li>\([^-]*\)<\/a><\/li>.*/\1/' | sed 's/.*>\([^-]*\)/\1/'`

echo $numOfPages

# loop through each page and get the download-extension
baseName="www.xeno-canto.org"
for page in `seq 1 $numOfPages`;
do
   extensions=`curl http://www.xeno-canto.org/species/$birdFirstName-$birdSecondName?pg=$page \
   | grep download=* | cut -f 3 -d '<' | cut -f 3 -d '=' | cut -c 2- | rev | cut -c 3- | rev`
   extensions=(${extensions[@]})

   for i in `seq 0 ${#extensions[@]}`;
   do
      echo $baseName"${extensions[i]}"
   done
   unset extensions
done



# This loop runs the python script scraping_birds for each page.
# scraping_birds adds the recording specifications to the database
for page in `seq 1 $numOfPages`;
do
   url="http://www.xeno-canto.org/species/$birdFirstName-$birdSecondName?pg=$page"
   python scraping_birds.py $birdFirstName $birdSecondName $url
done
