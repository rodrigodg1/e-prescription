# Medication Control Contract
Contract to count the drugs supplied by the regulator with the drugs sold by the pharmacy.

**Run the commands inside the contract directory**
### COMPILE CONTRACT
```console
cargo wasm
```
### OPTIMIZE COMPILATION
```console
RUSTFLAGS='-C link-arg=-s' cargo wasm
```

### ENVIRONMENT VARIABLES (TERMINAL)
```console
source <(curl -sSL https://raw.githubusercontent.com/CosmWasm/testnets/master/sandynet-1/defaults.env)

export NODE="--node $RPC"
export TXFLAG="${NODE} --chain-id ${CHAIN_ID} --gas-prices 0.025ubay --gas auto --gas-adjustment 1.3"


```


### FACEUT
> Wallet 1
```console
JSON=$(jq -n --arg addr $(wasmd keys show -a wallet) '{"denom":"ubay","address":$addr}') && curl -X POST --header "Content-Type: application/json" --data "$JSON" https://faucet.sandynet.cosmwasm.com/credit
```
> Wallet 2
```console
JSON=$(jq -n --arg addr $(wasmd keys show -a wallet2) '{"denom":"ubay","address":$addr}') && curl -X POST --header "Content-Type: application/json" --data "$JSON" https://faucet.sandynet.cosmwasm.com/credit

```



### SHOW CONTRACTS ON THE NETWORK
```console
wasmd query wasm list-code $NODE
```

### CONTRACT UPLOAD
```console
RES=$(wasmd tx wasm store medication_control_contract.wasm --from wallet $TXFLAG -y --output json)
```

### CONTRACT CODE_ID
```console
CODE_ID=1
```

### TO CREATE AN INSTANCE
```console
SENDER=$(wasmd keys show -a wallet)
RECEIVER=$(wasmd keys show -a wallet2)

INIT='{
    "regulator":"'$SENDER'",
    "pharmacy":"'$RECEIVER'",
    "amount_medication_supplied":100,
    "amount_medication_sold":0
 }'


wasmd tx wasm instantiate $CODE_ID "$INIT" --from wallet --label "medication control contract" $TXFLAG -y
```

### VERIFY THE CONTRACT INSTANCES
```console
wasmd query wasm list-contract-by-code $CODE_ID $NODE --output json
```

### CONSULT THE CONTRACT ADDRESS FOR SENDING TRANSACTIONS
```console
CONTRACT=$(wasmd query wasm list-contract-by-code $CODE_ID $NODE --output json | jq -r '.contracts[-1]')
echo $CONTRACT
#export CONTRACT=wasm1w27ekqvvtzfanfxnkw4jx2f8gdfeqwd3k7k3zk
```


### CREATE A TRANSACTION BASED ON THE METHOD OF CONTRACT EXECUTION
> for the pharmacy to report a sale:
```console
TRANSACTION='{"update_medication":{"amount_sold":10}}'
```
> for the regulator to update the amount of drugs supplied:
```console
TRANSACTION='{"supply":{"amount":10}}'
```

### SEND THE TRANSACTION TO THE NETWORK TO VALIDATE
wallet = regulator

wallet2 = pharmacy

> error, only the pharmacy can send sales notification and update the contract state
```console
wasmd tx wasm execute $CONTRACT "$TRANSACTION" --amount 100ubay --from wallet $TXFLAG -y
```
> the pharmacy that sends the sales notification with amount of medication
```console
wasmd tx wasm execute $CONTRACT "$TRANSACTION" --amount 100ubay --from wallet2 $TXFLAG -y
```

### QUERY THE CONTRACT STATE
```console
wasmd query wasm contract-state all $CONTRACT $NODE --output "json" | jq -r '.models[1].value' | base64 -d | python3 -m json.tool
```


### METHOD DEFINED IN THE CONTRACT TO RETURN THE LAST STATE OF RECORDS
```console
QUERY='{"get_count": {}}'

wasmd query wasm contract-state smart $CONTRACT "$QUERY" $NODE --output json | python3 -m json.tool
```
