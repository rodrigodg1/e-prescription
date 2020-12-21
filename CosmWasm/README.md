
## Requirements

 1. [Go](https://golang.org/dl/) `v1.14 +` 
 2. [Rust](https://rustup.rs/)
 3. [wasmd](https://github.com/CosmWasm/wasmd.git)

the steps for installation on page: [CosmWasm Installation](https://docs.cosmwasm.com/getting-started/installation.html)

## Usage
1.  In terminal, compile the project with
	* `rustup default stable` and 
	* `RUSTFLAGS='-C link-arg=-s' cargo wasm` (optimizer)a
2. unit-test
	* `cargo unit-test`

the contract file is at `target/wasm32-unknown-unknown/release/`

## Uploading and Interacting

for configuration of keys, network, node and account, see the next steps in the script at:
-  **Uploading and Interaction Scripts/local-node-script-doctor.sh**

and to send transactions: 
- **Uploading and Interaction Scripts/script_transactions_local.sh** 



