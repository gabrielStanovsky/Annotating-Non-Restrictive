#!/bin/bash


if [ -z "$1" ]; then 
	echo "Usage: generateCorpora.sh <path to CoNLL 2009 train file>"; 
	exit 1;
fi

paste -d'\0'  ${1} ./diffs/CoNLL2009-ST-English-train-with-restrictiveness.paste ./diffs/train.paste  | grep '@@TRAIN@@' | rev | cut -f2- | rev > ./corpus/train
paste -d'\0'  ${1} ./diffs/CoNLL2009-ST-English-train-with-restrictiveness.paste ./diffs/dev.paste  | grep '@@DEV@@' | rev | cut -f2- | rev > ./corpus/dev
paste -d'\0'  ${1} ./diffs/CoNLL2009-ST-English-train-with-restrictiveness.paste ./diffs/test.paste  | grep '@@TEST@@' | rev | cut -f2- | rev > ./corpus/test
