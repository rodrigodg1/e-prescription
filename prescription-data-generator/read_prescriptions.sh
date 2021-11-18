#!/bin/bash

MAX=99
#loop for prescriptions files

#source <(curl -sSL https://raw.githubusercontent.com/CosmWasm/testnets/master/uni/defaults.env)
#export NODE="--node $RPC"
#export TXFLAG="${NODE} --chain-id ${CHAIN_ID} --gas-prices 0.025ujunox --gas auto --gas-adjustment 1.3"
#export CONTRACT=juno1muhpwhn3usuhp3qrqu2l2sxuh0xpu8rs5mck8kxzg00vzy7cq0kq0kapl5

 CHAIN_ID="uni"
 TESTNET_NAME="uni"
 DENOM="ujunox"
 BECH32_HRP="juno"
 WASMD_VERSION="v0.20.0"
 JUNOD_VERSION="v2.0.0-beta"
 CONFIG_DIR=".juno"
 BINARY="junod"

 COSMJS_VERSION="v0.26.0"
 GENESIS_URL="https://raw.githubusercontent.com/CosmosContracts/testnets/main/uni/genesis.json"
 PERSISTENT_PEERS_URL="https://raw.githubusercontent.com/CosmosContracts/testnets/main/uni/persistent_peers.txt"
 SEEDS_URL="https://raw.githubusercontent.com/CosmosContracts/testnets/main/uni/seeds.txt"

 RPC="https://rpc.uni.juno.deuslabs.fi:443"
 LCD="https://lcd.uni.juno.deuslabs.fi"
 FAUCET="https://faucet.uni.juno.deuslabs.fi"

 COSMOVISOR_VERSION="v0.1.0"
 COSMOVISOR_HOME=$HOME/.juno
 COSMOVISOR_NAME=junod


echo $RPC
NODE="--node $RPC"
TXFLAG="${NODE} --chain-id ${CHAIN_ID} --gas-prices 0.025ujunox --gas auto --gas-adjustment 1.3 "

echo $NODE


#echo $NODE
#echo $TXFLAG
CONTRACT=juno1muhpwhn3usuhp3qrqu2l2sxuh0xpu8rs5mck8kxzg00vzy7cq0kq0kapl5

echo $CONTRACT



for i in {0..99}
do
    #change these paths
    personal_info_filename="/home/vm/Desktop/e-prescription/prescription-data-generator/separate-prescription-data/personal_ID/patient_personal_id_of_precription$i"
    personal_info=$(<$personal_info_filename)

    medication_filename="/home/vm/Desktop/e-prescription/prescription-data-generator/separate-prescription-data/medication/medication_of_prescription$i"
    medication=$(<$medication_filename)

    diagnosis_filename="/home/vm/Desktop/e-prescription/prescription-data-generator/separate-prescription-data/diagnosis/diagnosis_of_prescription$i"
    diagnosis=$(<$diagnosis_filename)

    echo "Prescription $i"
    #echo "$personal_info"

    #echo "$medication"
    #echo "$diagnosis"
    #APPROVE='{"approve":{"quantity":[{"amount":"1","denom":"ushell","medicines":"Vicodin (hydrocodone/acetaminophen) and Simvastatin (Generic for Zocor)","diagnosis":"Anxiety: Lucys sudden confinement in hospital, diminished ability to perform daily activities, and concerns about her family and health, predispose her to experiencing anxiety, a potential trigger of depression"}]}}'


    #export APPROVE='{"approve":{"quantity":[{"amount":"1"."denom":"umayo".'$value' }]}}
    export TRANSACTION='{"prescription":{"personal_info":'$personal_info',"medication":'$medication',"diagnosis":'$diagnosis'}}'


    #TRANSACTION="'$TRANSACTION'"
    #echo $TRANSACTION
    #echo $CONTRACT



    TIMEFORMAT=%R



    #count max transaction for the script
    

    #interator for sending transactions to the contract
    #and saving the results on the results_transactions file

    echo "Transaction Number: $i of $MAX " >> results_transaction_juno.txt

    sleep 3


    { time junod tx wasm execute $CONTRACT "$TRANSACTION" --amount 1ujunox --from wallet $TXFLAG -y ; } 2>> results_transaction_juno.txt
    echo "" >> results_transaction_juno.txt


    sleep 5


done
