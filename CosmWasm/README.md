


## Requirements

 1. [Go](https://golang.org/dl/) `v1.14` 
 2. [Rust](https://rustup.rs/)
 3. [wasmd](https://github.com/CosmWasm/wasmd.git)
	 1. use `git checkout v0.11.1`  
	 2.  `make install`
	 3.  `make build`
	 4.  move the binaries `wasmd` and `wasmcli` from `build/` to `/usr/local/go/bin/`

the steps for installation on page: [Getting Started/Installation](https://docs.cosmwasm.com/)

## Usage
1.  In terminal, compile the project with
	* `rustup default stable` and 
	* `RUSTFLAGS='-C link-arg=-s' cargo wasm` (optimizer)
2. unit-test
	* `cargo unit-test`

the contract file is at `target/wasm32-unknown-unknown/release/`

## Uploading and Interacting

### Local
For configuration of keys, network, node and account, see the next steps in the script at:
-  [Scripts/local-node-script.sh](https://github.com/rodrigodg1/e-prescription/blob/master/CosmWasm/Scripts/local-node-script.sh)

for **local** transactions script:
-  [Scripts/transactions-script-local.sh](https://github.com/rodrigodg1/e-prescription/blob/master/CosmWasm/Scripts/transactions-script-local.sh)

### Testnet

for **testnet** transactions script:
-  [Scripts/transactions-script-testnet-8-validators-CoralTestnet.sh](https://github.com/rodrigodg1/e-prescription/blob/master/CosmWasm/Scripts/transactions-script-testnet-8-validators-CoralTestnet.sh)
-  [Scripts/transactions-script-testnet-12-validators-MusselTestnet.sh](https://github.com/rodrigodg1/e-prescription/blob/master/CosmWasm/Scripts/transactions-script-testnet-12-validators-MusselTestnet.sh) use wasmd v0.14.0 and Go v1.15


