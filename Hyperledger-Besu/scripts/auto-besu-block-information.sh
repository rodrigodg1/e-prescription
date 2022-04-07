#!/bin/bash

TIMEFORMAT=%R


for i in {1..2000}
do
      #query and salve block timestamp information in a file
      node prescription_tx.js >> report/besu-block-time.txt 
      sleep 4

done
echo "End !"

exit