#CREATE INSIDE wasmd DIRECTORY


APP_HOME="~/.wasmd"
CLI_HOME="~/.wasmcli"

# initialize wasmd configuration files
wasmd init localnet --chain-id localnet --home ${APP_HOME}



#define some configs about network in ~/wasmd/~/.wasmd/config/app.toml
sed -i -r 's/minimum-gas-prices = ""/minimum-gas-prices = "0.025ucosm"/' ${APP_HOME}/config/app.toml


#create keys
wasmcli keys add fred 

wasmcli keys add bob 



#init config
wasmcli config chain-id localnet --home ${CLI_HOME}
wasmcli config trust-node true --home ${CLI_HOME}
wasmcli config node http://localhost:26657 --home ${CLI_HOME}
wasmcli config output json --home ${CLI_HOME}

wasmcli config broadcast-mode block



#add account tokens
wasmd add-genesis-account $(wasmcli keys show -a fred) 10000000000ucosm,10000000000stake --home ${APP_HOME}
wasmd add-genesis-account $(wasmcli keys show -a bob) 10000000000ucosm,10000000000stake --home ${APP_HOME}





# add fred's address as validator's address
wasmd gentx --name fred --home ${APP_HOME}

# collect gentxs to genesis
wasmd collect-gentxs --home ${APP_HOME}

# validate the genesis file
wasmd validate-genesis --home ${APP_HOME}

# run the node
wasmd start --home ${APP_HOME}




#other terminal



#upload contract, inside contract folder
RES=$(wasmcli tx wasm store cw_escrow.wasm --from fred --chain-id="localnet" --gas-prices="0.025ucosm" --gas="auto" --gas-adjustment="1.2" -y)

CODE_ID=$(echo $RES | jq -r '.logs[0].events[0].attributes[-1].value')

#if CODE_ID error, make it manually!



# instantiate contract
INIT=$(jq -n --arg fred $(wasmcli keys show -a fred) --arg bob $(wasmcli keys show -a bob) '{"arbiter":$fred,"recipient":$bob}')

wasmcli tx wasm instantiate $CODE_ID "$INIT" --from fred --amount=50000ucosm  --chain-id="localnet" --label "escrow 1" --gas-prices="0.025ucosm" --gas="auto" --gas-adjustment="1.2" -y
# must be returned information abount contract




#view contract
wasmcli query wasm list-contract-by-code $CODE_ID

#store the contract address
CONTRACT=$(wasmcli query wasm list-contract-by-code $CODE_ID | jq -r '.[0].address')
echo $CONTRACT




# consult contract information
# we should see this contract with 50000ucosm
wasmcli query wasm contract $CONTRACT
wasmcli query account $CONTRACT
wasmcli query wasm contract-state all $CONTRACT



#create transaction
APPROVE='{"approve":{"quantity":[{"amount":"1","denom":"ucosm","medicines":"medicine1 for example", "diagnosis":"diagnosis1 for example"}]}}'


#send transaction to network
wasmcli tx wasm execute $CONTRACT "$APPROVE" --from fred --chain-id="localnet" --gas-prices="0.025ucosm" --gas="auto" --gas-adjustment="1.2" -y


#consult account information
wasmcli query account $(wasmcli keys show fred -a)

#consult private key account
wasmcli query account $(wasmcli keys show bob -a)


#information about contract account
wasmcli query account $CONTRACT




