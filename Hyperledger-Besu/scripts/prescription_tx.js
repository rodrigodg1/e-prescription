const path = require('path');
const fs = require('fs-extra');
const Web3 = require('web3');

// member1 details
const { tessera, besu } = require("./keys.js");
//const host = besu.member1.url;
const host = "http://localhost:8545";
//console.log(host)
const accountAddress = besu.member1.accountAddress;

// abi and bytecode generated from simplestorage.sol:
// > solcjs --bin --abi simplestorage.sol
const contractJsonPath = path.resolve(__dirname, '../','contracts','Prescription.json');
const contractJson = JSON.parse(fs.readFileSync(contractJsonPath));
const contractAbi = contractJson.abi;
const contractBytecode = contractJson.evm.bytecode.object
// initialize the default constructor with a value `47 = 0x2F`; this value is appended to the bytecode
const contractConstructorInit = "000000000000000000000000000000000000000000000000000000000000002F";
const contractConstructorUpdate = "000000000000000000000000000000000000000000000000000000000000001F";


async function getValueAtAddress(host, deployedContractAbi, deployedContractAddress){
  const web3 = new Web3(host);
  const contractInstance = new web3.eth.Contract(deployedContractAbi, deployedContractAddress);
  const res = await contractInstance.methods.get().call();
  console.log("Obtained value at deployed contract is: "+ res);
  return res
}

async function getAllPastEvents(host, deployedContractAbi, deployedContractAddress){
    const web3 = new Web3(host);
    const contractInstance = new web3.eth.Contract(deployedContractAbi, deployedContractAddress);
    const res = await contractInstance.getPastEvents("allEvents", {
      fromBlock: 0,
      toBlock: 'latest'
    })
  
    const amounts = res.map(x => {
      return x.returnValues._amount
    });
  
    const personal_info = res.map(y => {
      return y.returnValues._personal_info
    });
    const medication = res.map(z => {
      return z.returnValues._medication
    });
    const diagnosis = res.map(k => {
      return k.returnValues._diagnosis
    });
  
  
  
  
    console.log("Obtained all value events from deployed contract : [" + amounts + "]");
    console.log("Obtained all medication events from deployed contract : [" + medication + "]");
    console.log("Obtained all diagnosis events from deployed contract : [" + diagnosis + "]");
  
  
    return res
  }

// You need to use the accountAddress details provided to Quorum to send/interact with contracts
async function setValueAtAddress(host, accountAddress, value,personal_info,medication, diagnosis, deployedContractAbi, deployedContractAddress){
  const web3 = new Web3(host);
  const account = web3.eth.accounts.create();
  // console.log(account);
  const contract = new web3.eth.Contract(deployedContractAbi,deployedContractAddress);

  // eslint-disable-next-line no-underscore-dangle
  const functionAbi = contract._jsonInterface.find(e => {
    return e.name === "set";
  });



  //data to be send to the set smart contract method
  const prescription_data = contract.methods.set(value,personal_info, medication, diagnosis).encodeABI(); 


  const functionParams = {
    to: deployedContractAddress,
    data: prescription_data,
    gas: "0x2CA51"  //max number of gas units the tx is allowed to use
  };
  const signedTx = await web3.eth.accounts.signTransaction(functionParams, account.privateKey);
   //console.log("sending the txn")
  const txReceipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
  //console.log("tx transactionHash: " + txReceipt.transactionHash);
  //console.log("tx contractAddress: " + txReceipt.contractAddress);
  return txReceipt
}

async function createContract(host) {
  const web3 = new Web3(host);
  // make an account and sign the transaction with the account's private key; you can alternatively use an exsiting account
  const account = web3.eth.accounts.create();
  console.log(account);

  const txn = {
    chainId: 1337,
    nonce: await web3.eth.getTransactionCount(account.address),       // 0x00 because this is a new account
    from: account.address,
    to: null,            //public tx
    value: "0x00",
    data: '0x'+contractBytecode+contractConstructorInit,
    gasPrice: "0x0",     //ETH per unit of gas
    gas: "0x3d0900"  //max number of gas units the tx is allowed to use
  };

  console.log("create and sign the txn")
  const signedTx = await web3.eth.accounts.signTransaction(txn, account.privateKey);
  console.log("sending the txn")
  const txReceipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
  console.log("tx transactionHash: " + txReceipt.transactionHash);
  console.log("tx contractAddress: " + txReceipt.contractAddress);
  return txReceipt;
};


//used to block time
async function latest_block(){
    const web3 = new Web3(host);
    //web3.eth.getBlock("latest").then(console.log);
    web3.eth.getBlock("latest").then(data => {
      var unix_timestamp = data["timestamp"]
      var block_number = data["number"]
      var count_txs = data["transactions"].length;
      //console.log(count_txs)
      //console.log(data)

    // Create a new JavaScript Date object based on the timestamp
    // multiplied by 1000 so that the argument is in milliseconds, not seconds.
    var date = new Date(unix_timestamp * 1000);
    // Hours part from the timestamp
    var hours = date.getHours();
    // Minutes part from the timestamp
    var minutes = "0" + date.getMinutes();
    // Seconds part from the timestamp
    var seconds = "0" + date.getSeconds();

  
    // Will display time in 10:30:23 format
    var formattedTime = hours + ':' + minutes.substr(-2) + ':' + seconds.substr(-2)
    var count_txs_string = String(count_txs)
    var formattedTime_string = String(formattedTime)
    var block_number_string = String(block_number)
  
    // block height : number of transactions : block timestamp
    var result = block_number_string + ":" + count_txs + ":" + formattedTime_string
  
    console.log(result);
  
  
  
  
    }).catch(err => {
      console.log(err);
    })
    
  }
  


async function main(){
  
    let newValue = 1;


    let personal_info = "Personal Information";
    let medication = "Medication 1";
    let diagnosis = "Diagnosis data";



    //first, the contract was uploaded via Remix IDE
    // and the contract address was paste here
    contract_addr = "0x05d91B9031A655d08E654177336d08543ac4B711";


    //console.log("Contract deployed at address: " + contract_addr);
    //console.log("Use the smart contracts 'get' function to read the contract's constructor initialized value .. " )
    //await getValueAtAddress(host, contractAbi, contract_addr);
    //console.log("Use the smart contracts 'set' function to update prescription state.. " );
    await setValueAtAddress(host, accountAddress, newValue,personal_info,medication, diagnosis, contractAbi, contract_addr);
    //console.log("Verify the updated value that was set .. " )
    //await getValueAtAddress(host, contractAbi, contract_addr);
    //await getAllPastEvents(host, contractAbi, contract_addr);
    await latest_block();
  
}

if (require.main === module) {
  main();
}

module.exports = exports = main

