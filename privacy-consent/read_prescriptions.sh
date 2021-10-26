#!/bin/bash

MAX=1005
#loop for prescriptions files
for i in {1..$MAX}
do
    filename="encrypted-prescription-files/enc_prescription$i"
    value=$(<$filename)

    #echo "$value"

    export APPROVE='{"approve":{"quantity":[{"amount":"1"."denom":"umayo".'$value' }]}}'

    echo $APPROVE
    echo $CONTRACT
    echo ""
    echo ""


    TIMEFORMAT=%R



    #count max transaction for the script
    

    #interator for sending transactions to the contract
    #and saving the results on the results_transactions file
    for (( i=1; i<=$MAX; i++ ))
    do

    sleep 3

    echo ""
    echo ""
    echo "Transaction Number: $i of $MAX " >> results_transaction_oysternet.txt
    echo ""

    { time wasmd tx wasm execute $CONTRACT "$APPROVE" --from doctor $TXFLAG -y ; } 2>> results_transaction_oysternet.txt
    echo "" >> results_transaction_oysternet.txt


    done

done
