#!/bin/bash

TIMEFORMAT=%R


for i in {1..1000}
do

      { time node rospten-client.js ; } 2>> report-ropsten.txt
      

done
echo "End !"

exit