# default home is ~/.wasmd
APP_HOME="~/.wasmd"
CLI_HOME="~/.wasmcli"
RPC="http://localhost:26657"


# initialize wasmd configuration files
wasmd init localnet --chain-id localnet --home ${APP_HOME}

# add minimum gas prices config to app configuration file
# define some configs about network in ~/wasmd/~/.wasmd/config/app.toml
sed -i -r 's/minimum-gas-prices = ""/minimum-gas-prices = "0.025ucosm"/' ${APP_HOME}/config/app.toml


#create keys
wasmcli keys add doctor 

wasmcli keys add patient 


# add your wallet addresses to genesis
wasmd add-genesis-account $(wasmcli keys show -a doctor) 10000000000ucosm,10000000000stake --home ${APP_HOME}
wasmd add-genesis-account $(wasmcli keys show -a patient) 10000000000ucosm,10000000000stake --home ${APP_HOME}

# add doctor's address as validator's address
wasmd gentx --name doctor --home ${APP_HOME}

# collect gentxs to genesis
wasmd collect-gentxs --home ${APP_HOME}

# validate the genesis file
wasmd validate-genesis --home ${APP_HOME}

# run the node
wasmd start --home ${APP_HOME}



# other terminal 



# see how many contract codes we have now
wasmcli query wasm list-code

#upload contract file
#you must be in the contract file directory
RES=$(wasmcli tx wasm store cw_medical_pharmacy.wasm --chain-id="localnet" --from doctor --gas-prices="0.025ucosm" --gas="auto" --gas-adjustment="1.2" -y)

# code for instantiating the contract
#CODE_ID=$(echo $RES | jq -r '.logs[0].events[0].attributes[-1].value')

#if error, make manually, se the last code with:
wasmcli query wasm list-code
#and then, store in CODE_ID
CODE_ID=1

echo $CODE_ID





#instantiating the contract

# instantiate contract and verify
INIT=$(jq -n --arg doctor $(wasmcli keys show -a doctor) --arg patient $(wasmcli keys show -a patient) '{"arbiter":$doctor,"recipient":$patient}') 

wasmcli tx wasm instantiate $CODE_ID "$INIT" --from doctor --amount=50000ucosm --chain-id="localnet" --label "Medical-Contract" --gas-prices="0.025ucosm" --gas="auto" --gas-adjustment="1.2" -y


# check the contract state 
wasmcli query wasm list-contract-by-code $CODE_ID

#store contract address
CONTRACT=$(wasmcli query wasm list-contract-by-code $CODE_ID | jq -r '.[0].address')

echo $CONTRACT

# ways to query contract
wasmcli query wasm contract $CONTRACT
wasmcli query account $CONTRACT
# you can dump entire contract state
wasmcli query wasm contract-state all $CONTRACT
# you can also query one key directly
wasmcli query wasm contract-state raw $CONTRACT 0006636f6e666967 --hex


# Note that keys are hex encoded, and val is base64 encoded.
# To view the returned data (assuming it is ascii), try something like:
wasmcli query wasm contract-state all $CONTRACT | jq -r '.[0].key' | xxd -r -ps
wasmcli query wasm contract-state all $CONTRACT | jq -r '.[0].val' | base64 -d




#Interacting 



#create transaction/prescription with medications and diagnosis
#with 1 token for the transaction
APPROVE='{"approve":{"quantity":[{"amount":"1","denom":"ucosm","medicines":"Vicodin (hydrocodone/acetaminophen) and Simvastatin (Generic for Zocor)","diagnosis":"Anxiety: Lucys sudden confinement in hospital, diminished ability to perform daily activities, and concerns about her family and health, predispose her to experiencing anxiety, a potential trigger of depression"}]}}'

wasmcli tx wasm execute $CONTRACT "$APPROVE" --from doctor --chain-id="localnet" --gas-prices="0.025ucosm" --gas="auto" --gas-adjustment="1.2" -y



#consult doctor account information
wasmcli query account $(wasmcli keys show doctor -a)

#consult patient account information
wasmcli query account $(wasmcli keys show patient -a)


#information about contract account
wasmcli query account $CONTRACT




