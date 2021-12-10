pragma solidity ^0.5.11;


contract Prescription{
    address doctorAddr;
    address patientAddr;
    string  personal_id;
    string  medication;
    string  diagnosis;
    uint256 count=0;
    address last_update_addr;


    //prescription contract constructor (relation with doctor and patient)
    constructor(address _patientAddr) public {
        doctorAddr = msg.sender;
        patientAddr = _patientAddr;
        last_update_addr = msg.sender; //tracking who made changes in contract state
    }

    //only doctor can create prescriptions transactions
    function create_prescription(string memory _personal_id, string memory _medication, string memory _diagnosis) public {
        if (msg.sender == doctorAddr){
            personal_id = _personal_id;
            medication = _medication;
            diagnosis = _diagnosis;
            count = count + 1;
            last_update_addr = msg.sender;
        }else{
            require(msg.sender == doctorAddr,"Sender not authorized.");
        }
    
    }



    //for patient and doctor
    function get_prescription_info() public view returns (address,address, string memory ,string memory ,string memory ){
        return (doctorAddr,patientAddr,personal_id,medication,diagnosis);
    }

    // for pharmacy
    function get_medication_info() public view returns (address,address, string memory){
        return (doctorAddr,patientAddr,medication);
    }










}
