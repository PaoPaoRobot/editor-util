#!/bin/sh
for i in `seq -f"%04g.pdf" 1 3139`;
do
python title.py $i --rename;
done
