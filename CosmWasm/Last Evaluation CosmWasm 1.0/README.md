## Basic setup

 Ubuntu 20.04.3 LTS
 
 8GB - Intel Core i7-10510U @ 4x 2,304GHz
  

 Testnet used: [cliffnet](https://github.com/CosmWasm/testnets)
  

## Inside Prescription-Contract directory

```console
cd Prescription-Contract/
```
### COMPILE THE CONTRACT

```console
cargo wasm
```

### OPTIMIZE COMPILATION

```console
RUSTFLAGS='-C link-arg=-s' cargo wasm
```

### ENVIRONMENT VARIABLES (TERMINAL)

```console
source <(curl -sSL https://raw.githubusercontent.com/CosmWasm/testnets/master/cliffnet-1/defaults.env)

export NODE="--node $RPC"

export TXFLAG="${NODE} --chain-id ${CHAIN_ID} --gas-prices 0.025upebble --gas auto --gas-adjustment 1.3"

```

  
  

### CREATE WALLETS

```console
wasmd keys add wallet
wasmd keys add wallet2
```

### FACEUT

> Wallet 1

```console
JSON=$(jq -n --arg addr $(wasmd keys show -a wallet) '{"denom":"upebble","address":$addr}') && curl -X POST --header "Content-Type: application/json" --data "$JSON" https://faucet.cliffnet.cosmwasm.com/credit
```

> Wallet 2
```console
JSON=$(jq -n --arg addr $(wasmd keys show -a wallet2) '{"denom":"upebble","address":$addr}') && curl -X POST --header "Content-Type: application/json" --data "$JSON" https://faucet.cliffnet.cosmwasm.com/credit
```

### SHOW CONTRACTS IN NETWORK
```console
wasmd query wasm list-code $NODE
```

  
  

### CONTRACT UPLOAD (inside target/wasm32-unknown-unknown/release)

```console
cd target/wasm32-unknown-unknown/release/

RES=$(wasmd tx wasm store prescription_contract.wasm --from wallet $TXFLAG -y --output json)
```



### COUNT CODE_ID
```console
wasmd query wasm list-code --count-total $NODE
```

### CONTRACT CODE_ID 

```console
CODE_ID=$(echo $RES | jq -r '.logs[0].events[-1].attributes[0].value')
wasmd query wasm list-code --count-total $NODE

echo $CODE_ID
```

```console
CODE_ID=6
```

### CREATE A PRESCRIPTION CONTRACT INSTANCE

in this case doctor is wallet and patient wallet2

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
```
**Instantiate:**

    wasmd tx wasm instantiate $CODE_ID "$INIT" --from wallet --label "prescription contract" $TXFLAG --no-admin -y


### CHECK THE PRESCRIPTION CONTRACT INSTANCES

```console
wasmd query wasm list-contract-by-code $CODE_ID $NODE --output json
```


### QUERY THE PRESCRIPTION CONTRACT ADDRESS TO SEND TRANSACTIONS

```console
CONTRACT=$(wasmd query wasm list-contract-by-code $CODE_ID $NODE --output json | jq -r '.contracts[-1]')

echo $CONTRACT

#export CONTRACT=wasm153r9tg33had5c5s54sqzn879xww2q2egektyqnpj6nwxt8wls70qfhztaq
```

  

### CREATE A TRANSACTION FOLLOWING THE CONTRACT METHOD

```console
TRANSACTION='{"create_prescription":{"personal_info":"Personal Information","medication":"Medication x","diagnosis":"Diagnosis y"}}'
```

  
  

### SEND THE TRANSACTION TO NETWORK

```console
wasmd tx wasm execute $CONTRACT "$TRANSACTION" --amount 100upebble --from wallet $TXFLAG -y
```

  

### CREATE A QUERY TO CHECK THE CURRENT CONTRACT STATE

```console
TRANSACTION='{"tracking":{}}'
```

  

### PHARMACY SENDS A QUERY TO CHECK THE MEDICATION

```console
wasmd tx wasm execute $CONTRACT "$TRANSACTION" --amount 100ubay --from wallet3 $TXFLAG -y
```


### QUERY THE CONTRACT STATE

```console
wasmd query wasm contract-state all $CONTRACT $NODE --output "json" | jq -r '.models[1].value' | base64 -d | python3 -m json.tool
```

  
  
  
  

### METHOD DEFINED FOR QUERY CONTRACT STATE

```console
QUERY='{"get_count": {}}'

wasmd query wasm contract-state smart $CONTRACT "$QUERY" $NODE --output json | python3 -m json.tool
```

  
  

### Query account balances

```console
wasmd query bank balances wasm13tz5hdwdscflvklrng0v9vp8pamrha0w029ygz $NODE
```
