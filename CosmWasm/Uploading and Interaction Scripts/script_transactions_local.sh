#!/bin/bash


#prescription
APPROVE='{"approve":{"quantity":[{"amount":"1","denom":"ushell","medicines":"Vicodin (hydrocodone/acetaminophen) and Simvastatin (Generic for Zocor)","diagnosis":"Anxiety: Lucys sudden confinement in hospital, diminished ability to perform daily activities, and concerns about her family and health, predispose her to experiencing anxiety, a potential trigger of depression"}]}}'


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

echo "" > results_transactions_local.txt
echo "Prescription content transaction CORAL TESTNET" >> results_transactions_local.txt
echo "" >> results_transactions_local.txt
echo $APPROVE >> results_transactions_local.txt
echo "" >> results_transactions_local.txt
echo "" >> results_transactions_local.txt

else
   echo ""
   echo "# appending results #" >> results_transactions_local.txt
   echo ""	
fi




#interator for sendind transactions to the contract
#and saving the results on the results_transactions file
for (( i=1; i<=$MAX; i++ ))
do

sleep 3

echo ""
echo ""
echo "Transaction Number: $i of $MAX " >> results_transactions.txt
echo ""

{ time wasmcli tx wasm execute $CONTRACT "$APPROVE" --from doctor --chain-id="localnet" --gas-prices="0.025ucosm" --gas="auto" --gas-adjustment="1.2" -y ; } 2>> results_transactions.txt
echo "" >> results_transactions_local.txt


done







