#! /bin/bash

outDir=$1
orgFiles=`ls *.org`

for f in $orgFiles
do
    filename=${f%.*}
    filenameOut=${filename##*/}
    pandoc -f org -t rst -o $outDir/${filenameOut}.rst ${filename}.org
done
