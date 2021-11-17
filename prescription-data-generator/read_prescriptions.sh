#!/bin/bash

MAX=2
#loop for prescriptions files

pwd 


for i in {0..4}
do
    #change these paths
    personal_info_filename="/Users/rodrigo/Desktop/e-prescription/prescription-data-generator/separate-prescription-data/personal_ID/patient_personal_id_of_precription$i"
    personal_info=$(<$personal_info_filename)

    medication_filename="/Users/rodrigo/Desktop/e-prescription/prescription-data-generator/separate-prescription-data/medication/medication_of_prescription$i"
    medication=$(<$medication_filename)

    diagnosis_filename="/Users/rodrigo/Desktop/e-prescription/prescription-data-generator/separate-prescription-data/diagnosis/diagnosis_of_prescription$i"
    diagnosis=$(<$diagnosis_filename)

    echo "Prescription $i"
    echo "$personal_info"
    echo "$medication"
    echo "$diagnosis"


    #export APPROVE='{"approve":{"quantity":[{"amount":"1"."denom":"umayo".'$value' }]}}'

    #echo $APPROVE
    #echo $CONTRACT



    TIMEFORMAT=%R



    #count max transaction for the script
    

    #interator for sending transactions to the contract
    #and saving the results on the results_transactions file
    for (( i=0; i<=4; i++ ))
    do

    #sleep 3

    echo "Transaction Number: $i of $MAX " >> results_transaction.txt


    ##{ time wasmd tx wasm execute $CONTRACT "$APPROVE" --from doctor $TXFLAG -y ; } 2>> results_transaction_oysternet.txt
    #echo "" >> results_transaction_oysternet.txt


    done

done
