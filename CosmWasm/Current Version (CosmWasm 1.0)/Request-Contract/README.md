# Consent Contract
Contract for request decryption rights to access the prescription item. Patient can authorize sending a encrypted delegation key from received public key.

***Run these commands inside contract directory***

#### COMPILE CONTRACT
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
RES=$(wasmd tx wasm store request_contract.wasm --from wallet $TXFLAG -y --output json)
```


#### CONTRACT CODE_ID
```console
CODE_ID=38
```

#### CONTRACT INSTANCE CREATION
```console
REQUEST_ORIGIN_ADDR=$(wasmd keys show -a wallet)
PATIENT=$(wasmd keys show -a wallet2)
CONSENT="NOT AUTHORIZED YET"
DESCRIPTION="Access to prescription data not yet authorized by the patient. Wait for authorization"

INIT='{
    "request_origin_name": "Pharmacy",
    "request_origin_addr":"'$REQUEST_ORIGIN_ADDR'",
    "patient":"'$PATIENT'",
    "patient_consent": "'$CONSENT'",
    "description": "'$DESCRIPTION'",
    "count_requests":1
 }'


wasmd tx wasm instantiate $CODE_ID "$INIT" --from wallet --label "request contract" $TXFLAG -y
```

#### CHECK CONTRACTS INSTANCE
```console
wasmd query wasm list-contract-by-code $CODE_ID $NODE --output json
```

#### CONSULT CONTRACT ADDRESS FOR SENDING TRANSACTIONS
```console
CONTRACT=$(wasmd query wasm list-contract-by-code $CODE_ID $NODE --output json | jq -r '.contracts[-1]')
echo $CONTRACT
#export CONTRACT=wasm1leqqmq0lpl6czfdd5tvkrahgy9jnf9du0e53yc
```

#### CREATE A TRANSACTION BASED ON CONTRACT METHOD/EVENT/MESSAGE
```console
TRANSACTION='{"request_access":{}}'
```

#### (REQUESTER) SEND THE TRANSACTION TO NETWORK
```console
wasmd tx wasm execute $CONTRACT "$TRANSACTION" --amount 100ubay --from wallet $TXFLAG -y
```

#### (ONLY PATIENT) CREATES A TRANSACTION TO AUTHORIZE (CONSENT) ACCESS TO PRESCRIPTION ITEM
```console
TRANSACTION='{"consent":{}}'
```
#### (ONLY PATIENT) SEND THE CONSENT TRANSACTION TO NETWORK
```console
wasmd tx wasm execute $CONTRACT "$TRANSACTION" --amount 100ubay --from wallet2 $TXFLAG -y
```




#### QUERY THE CONTRACT STATE
```console
wasmd query wasm contract-state all $CONTRACT $NODE --output "json" | jq -r '.models[1].value' | base64 -d | python3 -m json.tool
```



#### METHOD DEFINED INSIDE CONTRACT TO RETURN THE LAST CONTRACT STATE
```console
QUERY='{"get_count": {}}'

wasmd query wasm contract-state smart $CONTRACT "$QUERY" $NODE --output json | python3 -m json.tool
```
