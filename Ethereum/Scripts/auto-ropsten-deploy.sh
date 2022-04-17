#!/bin/bash

TIMEFORMAT=%R


for i in {1..1000}
do

      { time node rospten-deploy.js ; } 2>> rospten-deploy.txt
      

done
echo "End !"

exit