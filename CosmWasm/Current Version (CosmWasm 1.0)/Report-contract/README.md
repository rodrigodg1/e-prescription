# Report Contract
Contract for sending report transactions in case of illegal medication sales performed by pharmacy.

***Run these commands inside contract directory***

### COMPILE CONTRACT
```console
cargo wasm
```
#### OPTIMIZE COMPILATION
```console
RUSTFLAGS='-C link-arg=-s' cargo wasm
```

#### ENVIRONMENT VARIABLES (TERMINAL)
```console
source <(curl -sSL https://raw.githubusercontent.com/CosmWasm/testnets/master/sandynet-1/defaults.env)

export NODE="--node $RPC"
export TXFLAG="${NODE} --chain-id ${CHAIN_ID} --gas-prices 0.025ubay --gas auto --gas-adjustment 1.3"


```


#### FACEUT
> Wallet 1
```console
JSON=$(jq -n --arg addr $(wasmd keys show -a wallet) '{"denom":"ubay","address":$addr}') && curl -X POST --header "Content-Type: application/json" --data "$JSON" https://faucet.sandynet.cosmwasm.com/credit
```
> Wallet 2
```console
JSON=$(jq -n --arg addr $(wasmd keys show -a wallet2) '{"denom":"ubay","address":$addr}') && curl -X POST --header "Content-Type: application/json" --data "$JSON" https://faucet.sandynet.cosmwasm.com/credit

```



#### SHOW CONTRACTS ON THE NETWORK
```console
wasmd query wasm list-code $NODE
```



#### CONTRACT UPLOAD
```console
RES=$(wasmd tx wasm store report_contract.wasm --from wallet $TXFLAG -y --output json)
```

#### CONTRACT CODE_ID
```console
CODE_ID=4
```

#### FOR INSTANCE CREATION
```console
SENDER=$(wasmd keys show -a wallet)
RECEIVER=$(wasmd keys show -a wallet2)

INIT='{
    "origin":"'$SENDER'",
    "regulator":"'$RECEIVER'",
    "data":"first report data ...",
    "count":1
 }'


wasmd tx wasm instantiate $CODE_ID "$INIT" --from wallet --label "report contract" $TXFLAG -y
```

#### CHECK THE CONTRACT INSTANCES
```console
wasmd query wasm list-contract-by-code $CODE_ID $NODE --output json
```

#### CONSULT THE SMART CONTRACT ADDRESS FOR SENDING TRANSACTIONS
```console
CONTRACT=$(wasmd query wasm list-contract-by-code $CODE_ID $NODE --output json | jq -r '.contracts[-1]')
echo $CONTRACT
#export CONTRACT=wasm1ghd753shjuwexxywmgs4xz7x2q732vcnxnzzjq
```

#### CREATE A TRANSACATION BASED ON CONTRACT METHOD/EVENT/MESSAGE
```console
TRANSACTION='{"report":{"data":"test report data in transaction"}}'
```


#### SEND A TRANSACTION TO THE NETWORK
```console
wasmd tx wasm execute $CONTRACT "$TRANSACTION" --amount 100ubay --from wallet $TXFLAG -y
```

#### QUERY THE SMART CONTRACT CURRENT STATE
```console
wasmd query wasm contract-state all $CONTRACT $NODE --output "json" | jq -r '.models[1].value' | base64 -d | python3 -m json.tool
```



#### METHOD DEFINED TO RETURN THE LAST SMART CONTRACT ADDRESS
```console
QUERY='{"get_status": {}}'

wasmd query wasm contract-state smart $CONTRACT "$QUERY" $NODE --output json | python3 -m json.tool
```
