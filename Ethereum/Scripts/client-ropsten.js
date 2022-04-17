const Web3 = require('web3');
// Please to HTTP Provider, create an API in infuria and paste below
const provider = new Web3.providers.HttpProvider("< https://ropsten.infura.io/v3/API >");
const web3 = new Web3(provider);
web3.eth.net.isListening()
   .then(() => console.log('web3 is connected'))
   .catch(e => console.log('Wow. Something went wrong'));