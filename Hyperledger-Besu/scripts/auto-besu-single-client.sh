#!/bin/bash

TIMEFORMAT=%R


for i in {1..1000}
do
        #time to include a transaction in a block    
      { time node prescription_tx.js ; } 2>> report/besu-time.txt 
      

done
echo "Fim !"

exit