//SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;



contract Disclosure {
  uint public storedData;
  string public selected_items; 
  string public derived_proof;


  event stored(address _to, uint _amount);
  event stored_selected_items(address _to, string _selected_items);
  event stored_derived_proof(address _to, string _derived_proof);


/*
  constructor(uint initVal) public {
    emit stored(msg.sender, initVal);
    storedData = initVal;
  }
  */

  function set(uint x,string memory _selected_items,string memory _derived_proof) public {
    emit stored(msg.sender, x);
    emit stored_selected_items(msg.sender, _selected_items);
    emit stored_derived_proof(msg.sender, _derived_proof);
    
    
    storedData = x;
    selected_items =_selected_items;
    derived_proof = _derived_proof;
    

  }

  function get() view public returns (uint retVal,string memory selected_items,string memory derived_proof) {
    return (storedData,selected_items,derived_proof);
  }
}