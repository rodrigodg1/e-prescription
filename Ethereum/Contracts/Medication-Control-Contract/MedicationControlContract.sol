pragma solidity ^0.5.11;


contract MedicationControl{
    address regulatorAddr; //instance owner
    address pharmacyAddr;
    uint256 amount_medication_supplied=0;
    uint256 amount_medication_sold=0;
    uint256 amount_available_medication=0;
    address last_update_addr;


    //medication contract constructor (relation with regulator and pharmacy)
    constructor(address _pharmacy) public {
        regulatorAddr = msg.sender;
        last_update_addr = msg.sender;
        pharmacyAddr = _pharmacy;
    }

    //only the instance owner can create supply transactions
    function setSupply(uint256  _amount) public {
        if (msg.sender == regulatorAddr){
            amount_medication_supplied = amount_medication_supplied + _amount;
            amount_available_medication = amount_available_medication + _amount;
            last_update_addr = msg.sender;

        }else{
            require(msg.sender == regulatorAddr,"Sender not authorized.");
        }
    
    }
    //only pharmacy can create sales transactions
    function setSell(uint256  _amount_sold) public {
        if (msg.sender == pharmacyAddr){

            if(amount_available_medication > 0 && amount_available_medication >= _amount_sold){

                amount_medication_sold = amount_medication_sold + _amount_sold;
                amount_available_medication = amount_available_medication - _amount_sold;

                last_update_addr = msg.sender;
                
            }else{
                revert("No medication available to sell");
            }
        }else{
            require(msg.sender == pharmacyAddr,"Sender not authorized.");
        }
    
    }


    //return regulator addres and report data
    function get_control_info() public view returns (address,address, uint256, uint256, uint256,address){
        return (regulatorAddr,pharmacyAddr, amount_medication_supplied,amount_medication_sold,amount_available_medication,last_update_addr);
    }


}