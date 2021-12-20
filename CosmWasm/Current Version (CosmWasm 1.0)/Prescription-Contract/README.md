# Prescription Contract
Contract for sending medical records transactions such as prescriptions.

***Run these commands inside contract directory***

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
RES=$(wasmd tx wasm store prescription_contract.wasm --from wallet $TXFLAG -y --output json)
```


### CONTRACT CODE_ID
```console
CODE_ID=15
```



### FOR INSTANCE CREATION
```console
SENDER=$(wasmd keys show -a wallet)
RECEIVER=$(wasmd keys show -a wallet2)

INIT='{
    "doctor":"'$SENDER'",
    "patient":"'$RECEIVER'",
    "personal_info":"patient personal info 1",
    "medication":"patient medication 1",
    "diagnosis":"patient diagnosis 1",
    "count":1
 }'

 echo $INIT


wasmd tx wasm instantiate $CODE_ID "$INIT" --from wallet --label "prescription contract" $TXFLAG -y

```
### CHECK THE CONTRACT INSTANCES
```console
wasmd query wasm list-contract-by-code $CODE_ID $NODE --output json
```

### CHECK CONTRACT ADDRESS FOR SENDING TRANSACTIONS
```console
CONTRACT=$(wasmd query wasm list-contract-by-code $CODE_ID $NODE --output json | jq -r '.contracts[-1]')

echo $CONTRACT
#export CONTRACT=wasm1wastjc07zuuy46mzzl3egz4uzy6fs5975j2j4s
```

### CREATE A TRANSACTION BASED ON CONTRACT METHOD
```console
TRANSACTION='{"create_prescription":{"personal_info":"personal info patient 2","medication":"medication patient 2","diagnosis":"Diagnosis patient 2"}}'
```


### SEND TRANSACTION TO NETWORK
```console
wasmd tx wasm execute $CONTRACT "$TRANSACTION" --amount 100ubay --from wallet $TXFLAG -y
```

### CREATE A TRANSACTION TO UPDATE THE LAST ACCESS TRACKING
```console
TRANSACTION='{"tracking":{}}'
```

### SEND A TRANSACTION TO THE NETWORK (PHARMACY QUERY)
```console
wasmd tx wasm execute $CONTRACT "$TRANSACTION" --amount 100ubay --from wallet3 $TXFLAG -y
```



### QUERY SMART CONTRACT STATE
```console
wasmd query wasm contract-state all $CONTRACT $NODE --output "json" | jq -r '.models[1].value' | base64 -d | python3 -m json.tool
```




### METHOD FOR RETURN THE LAST SMART CONTRACT STATE
```console
QUERY='{"get_count": {}}'

wasmd query wasm contract-state smart $CONTRACT "$QUERY" $NODE --output json | python3 -m json.tool
```
