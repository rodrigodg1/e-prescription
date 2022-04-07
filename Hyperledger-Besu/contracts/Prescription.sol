//SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;



contract Prescription {
  uint public storedData;
  string public personal_info; 
  string public medication;
  string public diagnosis;

  event stored(address _to, uint _amount);
  event stored_personal_info(address _to, string _personal_info);
  event stored_medication(address _to, string _medication);
  event stored_diagnosis(address _to, string _diagnosis);

  constructor(uint initVal) public {
    emit stored(msg.sender, initVal);
    storedData = initVal;
  }

  function set(uint x,string memory _personal_info,string memory _medication,string memory _diagnosis) public {
    emit stored(msg.sender, x);
    emit stored_personal_info(msg.sender, _personal_info);
    emit stored_medication(msg.sender, _medication);
    emit stored_diagnosis(msg.sender, _diagnosis);
    
    storedData = x;
    personal_info =_personal_info;
    medication = _medication;
    diagnosis = _diagnosis;

  }

  function get() view public returns (uint retVal,string memory personal_info,string memory medication,string memory diagnosis) {
    return (storedData,personal_info,medication,diagnosis);
  }
}