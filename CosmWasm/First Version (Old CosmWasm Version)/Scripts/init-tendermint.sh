#!/bin/sh



echo "wasmd must be in the directory/home "
echo "starting..."

sleep 3

cd

cd wasmd/~

wasmd start --home ./.wasmd
