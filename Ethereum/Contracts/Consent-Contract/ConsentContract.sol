pragma solidity ^0.5.11;


contract Consent{
    string request_origin_name; // requester name
    address request_origin_addr; // requester origin address
    address patient_addr; // patient address
    string patient_consent; // Authorized or Not
    string description; // description about patient consent status
    uint256 count_requests=0; // count number of requests
    address last_update_addr; // last state update address
    string delegation_key;


    //consent contract constructor (relation with requester and patient)
    constructor(address _patientAddr) public {
        request_origin_addr = msg.sender;
        patient_addr = _patientAddr;
        last_update_addr = msg.sender; //tracking who made changes in contract state
    }

    //only requester can create request transactions
    function create_consent(string memory _requester_name) public {
        if (msg.sender == request_origin_addr){
            string memory _consent = "NOT AUTHORIZED YET";
            string memory _description = "Access to prescription data not yet authorized by the patient. Wait for authorization";
            
            request_origin_name = _requester_name;
            count_requests = count_requests + 1;
            last_update_addr = msg.sender;
            patient_consent = _consent;
            description = _description;


        }else{
            require(msg.sender == request_origin_addr,"Sender not authorized.");
        }
    
    }
    function update_consent(string memory _delegation_key) public {
        if (msg.sender == patient_addr){
            string memory _consent = "AUTHORIZED";
            string memory _description = "Access to prescription data was authorized by the patient";
            
            last_update_addr = msg.sender;
            patient_consent = _consent;
            description = _description;

            delegation_key = _delegation_key;


        }else{
            require(msg.sender == patient_addr,"Sender not authorized.");
        }
    
    }




    //for patient and doctor
    function get_consent_info() public view returns (string memory,address,address, string memory ,string memory ,uint256,address,string memory ){
        return (request_origin_name,request_origin_addr,patient_addr,patient_consent,description,count_requests,last_update_addr,delegation_key);
    }






}
