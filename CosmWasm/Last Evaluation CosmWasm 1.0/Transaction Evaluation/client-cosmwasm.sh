#!/bin/bash

MAX=99

CHAIN_ID="cliffnet-1"
TESTNET_NAME="cliffnet-1"
FEE_DENOM="upebble"
STAKE_DENOM="urock"
BECH32_HRP="wasm"
WASMD_VERSION="v0.23.0"
CONFIG_DIR=".wasmd"
BINARY="wasmd"

COSMJS_VERSION="v0.27.1"
GENESIS_URL="https://raw.githubusercontent.com/CosmWasm/testnets/master/cliffnet-1/config/genesis.json"

RPC="https://rpc.cliffnet.cosmwasm.com:443"
LCD="https://lcd.cliffnet.cosmwasm.com"
FAUCET="https://faucet.cliffnet.cosmwasm.com"

COSMOVISOR_VERSION="v0.42.10"
COSMOVISOR_HOME=/root/.wasmd
COSMOVISOR_NAME=wasmd


NODE="--node $RPC"
TXFLAG="${NODE} --chain-id ${CHAIN_ID} --gas-prices 0.025upebble --gas auto --gas-adjustment 1.3 "


echo $NODE
echo $TXFLAG
CONTRACT=wasm1xuu35m0p42vpkvqe6qsmklrwg2xmk0pjdddn6fvjg5qcvu3ycspql7gqc2
echo $CONTRACT



#transaction data
personal_info="jzkfpmdvrupofsyvtmdfyjnnvnrggdhmaxjlwmcofatkzxebfninrxckgshcxbnrclpsdnzjxjwuxoucnzcpnwuutwyhignesllqgvqxfbqnzshlcrfasuvarjdevlafmzzqkanrrjdddafwnyicqrpmfrudnticvpbeuirjigkevefaaozrezmrtnpzpqhggsgrshtdkxspfzjjepzwyuondpukjhvmzmhgptcqhvsnfpkwykkynhtpnfmydqwuaqaqewrbneeprmdsnimhrxpmzcqqsqocgfjqlzbomiakuzgeqafddnajqedjaayabfknqvperxvrbgdbdzvncumrn"
medication="nendehalijqyqhlnccfqwxtpqlylhfzlblfyrusvcuwjqcidnbgbzuxqieoknnbxolqfvizwyvepqxoaujnxunoyolejvmrqrvqphgknhrxtcbsomckgvjffgtzankfmypaqgrjflp"
diagnosis="zylmbcflspstiaiuqyiduscgqbemodanhgkhcseycoemxfnktxmasbjsdmafgajqkbplstqbehrllnfkthyudriktrfbsxphyzwqogvqnhwvewkbuvjgsfubtdsbytmibzochhgihwupvlkvdgokmlnxjlqhksfyryneelzymgwjreimctcizbvebviidhlvpofowuikcjcfmlkxvnuyudnxintqoqzownvtgypybnqmnnyugpbpgnianptzabdsbfvinksvefeblgtussquokymontwfhdruwvacgflryexkxxsomzscoekkmotybwacrgzycuwgdvifyyoxwcjkeprtggxzczntiyqshkqtezarslbyvqjktayknfooeturhiluzygmfpuytnambynbhsqdxgqebxmgfqeojhaixowdunbweskklthbnvoijqvlbrrwutwztlmkpndkjkgrupmzvgmdwubnnpyiouqbcmcslwvwerrohppcwwsadxouadogufzehfrjaqwfcisbwcqwscvf"

#transaction 
TRANSACTION='{"create_prescription":{"personal_info":"'$personal_info'","medication":"'$medication'","diagnosis":"'$diagnosis'"}}'

echo $TRANSACTION



#loop for sending transactions
for i in {0..2000}
do

    #echo "Prescription $i"

    TIMEFORMAT=%R


    #echo "Transaction Number: $i of $MAX " >> results_transaction.txt
    


    { time wasmd tx wasm execute $CONTRACT "$TRANSACTION" --amount 1upebble --from wallet $TXFLAG -y ; } 2>> results_transaction.txt
    
    sleep 2
    block_query=$(wasmd query block $NODE)

    echo $block_query | jq '.block.header.height' >> block_time.txt
    echo $block_query | jq '.block.header.time' >> block_time.txt
    #echo $block_query | jq '.block.data.txs[0]' >> block_time.txt

    echo " " >> block_time.txt




done
