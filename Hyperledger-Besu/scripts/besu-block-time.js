const path = require('path');
const fs = require('fs-extra');
const Tx = require('ethereumjs-tx');
const Web3 = require('web3');

 

// member1 details
const { tessera, besu } = require("./keys.js");
const host = besu.ethsignerProxy.url;
const accountAddress = besu.ethsignerProxy.accountAddress;



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


  var result = block_number_string + ":" + count_txs + ":" + formattedTime_string

  console.log(result);




  }).catch(err => {
    console.log(err);
  })
  
}


async function main(){

    await latest_block()
    
}

if (require.main === module) {
  main();
}

module.exports = exports = main