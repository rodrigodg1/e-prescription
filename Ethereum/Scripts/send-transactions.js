const Web3 = require('web3');
const Tx = require('ethereumjs-tx').Transaction;
/* 
bellow paste the http link with API code
we are using the ropsten testnet
remove < >
*/
const provider = new Web3.providers.HttpProvider("< https://ropsten.infura.io/v3/API >"); //RPC server Address
const web3 = new Web3(provider);


web3.eth.net.isListening()
   .then(() => console.log('web3 is connected'))
   .catch(e => console.log('Wow. Something went wrong'));



//your account, copy from metamask wallet  
const account1 = '< account address >'; // Your account address 1
web3.eth.defaultAccount = account1;




// export you private key from metamask wallet and paste bellow
const privateKey1 = Buffer.from('<your private key>', 'hex');

web3.eth.getBalance(account1, (err,bal)=>{
  console.log('account 1 balance:', web3.utils.fromWei(bal,'ether'));
})



/*
from smart contract compiled, paste below the abi
using remix = go in "Compilation details" and copy ABI
or if are using the quorum compiler, go to the contracts directory and copy the ABI in json file
*/
const abi = [
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "initVal",
        "type": "uint256"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": false,
        "internalType": "address",
        "name": "_to",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "_amount",
        "type": "uint256"
      }
    ],
    "name": "stored",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": false,
        "internalType": "address",
        "name": "_to",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "string",
        "name": "_derived_proof",
        "type": "string"
      }
    ],
    "name": "stored_derived_proof",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": false,
        "internalType": "address",
        "name": "_to",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "string",
        "name": "_selected_items",
        "type": "string"
      }
    ],
    "name": "stored_selected_items",
    "type": "event"
  },
  {
    "inputs": [],
    "name": "derived_proof",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "get",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "retVal",
        "type": "uint256"
      },
      {
        "internalType": "string",
        "name": "selected_items",
        "type": "string"
      },
      {
        "internalType": "string",
        "name": "derived_proof",
        "type": "string"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "selected_items",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "x",
        "type": "uint256"
      },
      {
        "internalType": "string",
        "name": "_selected_items",
        "type": "string"
      },
      {
        "internalType": "string",
        "name": "_derived_proof",
        "type": "string"
      }
    ],
    "name": "set",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "storedData",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
];



/*
paste the smart contract address bellow
*/
const contract_Address = "< smart contract address >";

const contract = new web3.eth.Contract(abi, contract_Address);

/*
set smart contract method with the parameters
*/
const myData = contract.methods.set(1,"Personal Info / Medication / Diagnosis","derived_proof").encodeABI();


web3.eth.getTransactionCount(account1, (err, txCount) => {
// transaction object
  const txObject = {
  nonce:    web3.utils.toHex(txCount),
  to:       contract_Address,
  value:    web3.utils.toHex(web3.utils.toWei('0', 'ether')),
  gasLimit: web3.utils.toHex(2100000),
  gasPrice: web3.utils.toHex(web3.utils.toWei('6', 'gwei')),
  data: myData  
}
  // Sign the transaction
  const tx = new Tx(txObject,{'chain':'ropsten'});
  tx.sign(privateKey1);

  const serializedTx = tx.serialize();
  const raw = '0x' + serializedTx.toString('hex');

  // Broadcast the transaction
  const transaction = web3.eth.sendSignedTransaction(raw, (err, tx) => {
      console.log('err:', err, 'txHash:',tx)
  });

}); 

