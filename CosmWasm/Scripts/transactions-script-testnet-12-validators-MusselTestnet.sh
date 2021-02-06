#!/bin/bash



export APPROVE='{"approve":{"quantity":[{"amount":"1","denom":"umayo","medicines":"Vicodin (hydrocodone/acetaminophen) and Simvastatin (Generic for Zocor)","diagnosis":"Anxiety: Lucys sudden confinement in hospital, diminished ability to perform daily activities, and concerns about her family and health, predispose her to experiencing anxiety, a potential trigger of depression"}]}}'


echo $APPROVE
echo $CONTRACT
echo ""
echo ""


TIMEFORMAT=%R



#count max transaction for the script
MAX=100




echo "clear results file ? y/n"
read op



#clear the file content 
if [[ "$op" = "y" ]]
then


echo "" > results_transaction_musselnet.txt
echo "Prescription content transaction Mussel TestNet" >> results_transaction_musselnet.txt
echo "" >> results_transaction_musselnet.txt
echo $APPROVE >> results_transaction_musselnet.txt
echo "" >> results_transaction_musselnet.txt
echo "" >> results_transaction_musselnet.txt


else
   echo ""
   echo "# appending results #" >> results_transaction_musselnet.txt
   echo ""	
fi



#interator for sending transactions to the contract
#and saving the results on the results_transactions file
for (( i=1; i<=$MAX; i++ ))
do

sleep 3

echo ""
echo ""
echo "Transaction Number: $i of $MAX " >> results_transaction_musselnet.txt
echo ""

{ time wasmd tx wasm execute $CONTRACT "$APPROVE" --from doctor $TXFLAG -y ; } 2>> results_transaction_musselnet.txt
echo "" >> results_transaction_musselnet.txt


done







