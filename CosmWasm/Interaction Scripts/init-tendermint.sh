#!/bin/sh



echo "o wasmd deverá estar no diretório /home"
echo "iniciando..."

sleep 3

cd

cd wasmd/~

wasmd start --home ./.wasmd
