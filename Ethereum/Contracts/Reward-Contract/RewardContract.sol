pragma solidity ^0.5.11;

// contract for regulator to send ether to patient in case of proof of fraud.

contract Reward {

    address regulator;


    modifier onlyOwner() {
        require(msg.sender == regulator, "Only regulator can call this method");
        _;
    }

    constructor() public{
        regulator = msg.sender;
    }

    function send_reward(address payable receiver) payable external onlyOwner {
        uint256 amount = msg.value;
        receiver.transfer(amount);  
    }
}
