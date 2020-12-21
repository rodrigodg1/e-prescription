
## Requirements

 1. [Go](https://golang.org/dl/) `v1.14 +` 
 2. [Rust](https://rustup.rs/)
 3. [wasmd](https://github.com/CosmWasm/wasmd.git)
## Usage
1.  Compile this project with
	* `rustup default stable` and 
	* `RUSTFLAGS='-C link-arg=-s' cargo wasm` (optimizer)
2. unit-test
	* `cargo unit-test`

the contract file is at `target/wasm32-unknown-unknown/release`

## Uploading and Interacting

for configuration of keys, network, node and account, see the next steps in the directory :
-  **Interaction Scripts/local-node-script-doctor.sh**

and to send transactions: 
- **Interaction Scripts/script_transactions_local.sh** 



