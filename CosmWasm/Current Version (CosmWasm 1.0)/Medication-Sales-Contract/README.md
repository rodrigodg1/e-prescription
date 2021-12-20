# Medication Sales Contract

Smart Contract for medication sales

***Run the commands inside contract directory***

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
$ JSON=$(jq -n --arg addr $(wasmd keys show -a wallet) '{"denom":"ubay","address":$addr}') && curl -X POST --header "Content-Type: application/json" --data "$JSON" https://faucet.sandynet.cosmwasm.com/credit
```
> Wallet 2
```console
$ JSON=$(jq -n --arg addr $(wasmd keys show -a wallet2) '{"denom":"ubay","address":$addr}') && curl -X POST --header "Content-Type: application/json" --data "$JSON" https://faucet.sandynet.cosmwasm.com/credit

```



### SHOW CONTRACTS ON THE NETWORK
```console
wasmd query wasm list-code $NODE
```

### CONTRACT UPLOAD
 RES=$(wasmd tx wasm store medication_sales_contract.wasm --from wallet $TXFLAG -y --output json)

### CONTRACT CODE_ID
```console
$ CODE_ID=1
```

### PARA CRIAR UMA INSTANCIA
```console
$ SENDER=$(wasmd keys show -a wallet)
$ RECEIVER=$(wasmd keys show -a wallet2)

$ INIT='{
    "pharmacy":"'$SENDER'",
    "patient":"'$RECEIVER'",
    "medication":"medicationx",
    "dosage":"dosagex",
    "price":23,
    "cents":50,
    "count":1
 }'


$ wasmd tx wasm instantiate $CODE_ID "$INIT" --from wallet --label "medication sales contract" $TXFLAG -y

```

### CHECK THE CONTRACT INSTANCES
```console
$ wasmd query wasm list-contract-by-code $CODE_ID $NODE --output json
```

### CONSULT THE CONTRACT ADDRESS FOR SENDING TRANSACTIONS
```console
$ CONTRACT=$(wasmd query wasm list-contract-by-code $CODE_ID $NODE --output json | jq -r '.contracssts[-1]')
echo $CONTRACT
#export CONTRACT=wasm1nc5tatafv6eyq7llkr2gv50ff9e22mnfhap4vz
```

### CREATE A TRANSACTION BASED ON THE METHOD OF CONTRACT EXECUTION
```console
$ TRANSACTION='{"sell":{"medication":"test 3 medication name","dosage":"89g","price":77}}'

```

### SEND THE TRANSACTION TO THE NETWORK TO VALIDATE
```console
$ wasmd tx wasm execute $CONTRACT "$TRANSACTION" --amount 100ubay --from wallet $TXFLAG -y
```

### QUERY THE CONTRACT STATE
```console
$ wasmd query wasm contract-state all $CONTRACT $NODE --output "json" | jq -r '.models[1].value' | base64 -d | python3 -m json.tool
```

### METHOD DEFINED IN THE CONTRACT TO RETURN THE LAST RECORD STATE
```console
$ QUERY='{"get_status": {}}'

$ wasmd query wasm contract-state smart $CONTRACT "$QUERY" $NODE --output json | python3 -m json.tool
```
