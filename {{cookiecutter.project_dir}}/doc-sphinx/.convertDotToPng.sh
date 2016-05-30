#! /bin/bash

SOURCE_DIR=$1
DEST_DIR=$2

FILES=`ls ${SOURCE_DIR}`

for f in $FILES; do
    dot -Tpng ${SOURCE_DIR}/$f -o ${DEST_DIR}/${f}.png
done


