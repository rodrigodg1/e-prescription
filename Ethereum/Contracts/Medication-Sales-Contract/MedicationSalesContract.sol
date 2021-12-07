pragma solidity ^0.5.11;


contract Sales{
    address pharmacyAddr; //instance owner
    address patientAddr;
    string medication;
    string dosage;
    uint256 amount=0;
    address last_update_addr;


    //sales contract constructor (relation with pharmacy and patient)
    constructor(address _patient) public {
        pharmacyAddr = msg.sender;
        last_update_addr = msg.sender;
        patientAddr = _patient;
    }

    //only the instance owner can create supply transactions
    function sell_medication(string memory _medication, string memory _dosage, uint256  _amount) public {
        if (msg.sender == pharmacyAddr){
            medication = _medication;
            dosage = _dosage;
            amount = _amount;
            last_update_addr = msg.sender;

        }else{
            require(msg.sender == pharmacyAddr,"Sender not authorized.");
        }
    
    }

    //return regulator addres and report data
    function get_sales_info() public view returns (address,address, string memory,string memory, uint256,address){
        return (pharmacyAddr,patientAddr, medication,dosage, amount,last_update_addr);
    }


}
