pragma solidity ^0.5.11;


contract Reward {
    
    address regulator;


    modifier onlyOwner() {
        require(msg.sender == regulator, "Only regulator can call this method");
        _;
    }

    constructor() public{
        regulator = msg.sender;
    }

    function sendBal(address payable receiver) payable external onlyOwner {
        uint256 amount = msg.value;
        receiver.transfer(amount);  
    }
}
