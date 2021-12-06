pragma solidity ^0.5.11;


contract Report{
    address originAddr;
    address regulatorAddr;
    string  data;
    uint256  count;


    //report contract constructor (relation with origin and regulator)
    constructor(address _regulator) public {
        originAddr = msg.sender;
        regulatorAddr = _regulator;
    }

    //only the instance owner can create report transactions
    function setReport(string memory _data) public {
        if (msg.sender == originAddr){
            data = _data;
            count = count + 1;
        }else{
            require(msg.sender == originAddr,"Sender not authorized.");
        }
    
    }



    //return regulator addres and report data
    function get_report_info() public view returns (address, string memory){
        return (regulatorAddr,data);
    }


}