## Basic setup

 Ubuntu 20.04.3 LTS
 
 8GB - Intel Core i7-10510U @ 4x 2,304GHz
  
  
**Installation**

 to execute smart contracts methods in Hyperledger Besu network:

    npm install

**Client Code**

    cd scripts/

Edit: `prescription_tx.js`

1. Insert the RPC (*check your testnet address*);

2. Insert the private key (*if you are using metamask, export the private key and paste in client code*);

3. Insert your account address;
4. Insert you smart-contract address;

  

To automate transactions, run the scripts (inside scripts directory):

**Execution permission:**

  
**Single Client Bash:**

    chmod +x ./auto-besu-single-client.sh


**Run:**

    ./auto-besu-single-client.sh

or

    ./auto-besu-block-information.sh


It is possible to run the client directly:

    node prescription_tx.js

