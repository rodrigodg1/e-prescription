package main

import (
	"bytes"
	"encoding/json"
	"strconv"

	"github.com/hyperledger/fabric/core/chaincode/shim"
	sc "github.com/hyperledger/fabric/protos/peer"
)

/*
	Contract model - token is unique for each appointment
*/
type Contract struct {
	Token          string `json:"token"`
	DoctorAddress  string `json:"doctorAddress"`
	PatientAddress string `json:"patientAddress"`
	Medications    string `json:"medications"`
	Diagnostics    string `json:"diagnostics"`
}

func (cn *Contract) Init(stub shim.ChaincodeStubInterface) sc.Response {
	return shim.Success(nil)
}

/*
	Method invoked on every transaction
*/
func (cn *Contract) Invoke(stub shim.ChaincodeStubInterface) sc.Response {
	fcn, params := stub.GetFunctionAndParameters()

	switch fcn {
	case "send":
		return cn.Send(stub, params)
	case "query":
		return cn.QueryByPatientAddress(stub, params)
	}

	return shim.Success(nil)
}

/*
	Function used to send a new Contract to the ledger, receives 4 args on this order:
	args[0]: string - Contract token
	args[1]: string - Patient Address
	args[2]: string - Doctor Address
	args[3]: string - Medications
	args[4]: string - Diagnostics
*/
func (cn *Contract) Send(stub shim.ChaincodeStubInterface, args []string) sc.Response {
	if len(args) != 5 {
		return shim.Error("Wrong number of arguments! Expected 5 but got " + strconv.Itoa(len(args)))
	}

	contract := &Contract{
		Token:          args[0],
		PatientAddress: args[1],
		DoctorAddress:  args[2],
		Medications:    args[3],
		Diagnostics:    args[4],
	}

	// Get the JSON encoding of the Contract
	contractBytes, err := json.Marshal(contract)

	if err != nil {
		return shim.Error("Error serializing data: " + err.Error())
	}

	// Tries to put it into the state (contract token is the key)
	err = stub.PutState(args[0], contractBytes)

	if err != nil {
		return shim.Error("Error putting contract on state: " + err.Error())
	}

	// Creates a composite key to separate the Contracts by Patient Address
	patientTokenKey, err := stub.CreateCompositeKey("patient~token", []string{contract.PatientAddress, contract.Token})

	if err != nil {
		return shim.Error("Error associating token to patient: " + err.Error())
	}

	// Puts an empty state with the composite key
	err = stub.PutState(patientTokenKey, []byte{0x00})

	if err != nil {
		return shim.Error("Error associating token to patient: " + err.Error())
	}

	return shim.Success(contractBytes)
}

/*
	Function used to query patient Contracts, receives one arg:
	arg[0]: string - Patient Address
*/
func (cn *Contract) QueryByPatientAddress(stub shim.ChaincodeStubInterface, args []string) sc.Response {
	if len(args) != 1 {
		return shim.Error("Wrong number of arguments! Expected 1 but got " + strconv.Itoa(len(args)))
	}

	indexName := "patient~token"

	// Seeks for the composite key on the ledger
	iterator, err := stub.GetStateByPartialCompositeKey(indexName, []string{args[0]})

	if err != nil {
		return shim.Error("Error getting state: " + err.Error())
	}

	// Initializes a buffer that will be the response JSON array
	var buffer bytes.Buffer
	buffer.WriteString("[")

	firstToken := true

	for iterator.HasNext() {
		compositeKey, err := iterator.Next()

		if err != nil {
			return shim.Error("Error getting state: " + err.Error())
		}

		// Splits the composite key to get the args (patient address and token)
		_, compositeKeyArgs, err := stub.SplitCompositeKey(compositeKey.Key)

		if err != nil {
			return shim.Error("Error getting state: " + err.Error())
		}

		tokenID := compositeKeyArgs[1]

		// Gets the contract based on the token of the composite key
		contractBytes, err := stub.GetState(tokenID)

		if err != nil {
			return shim.Error("Error getting state: " + err.Error())
		}

		// If the first item has already been written, writes a comma to separate the JSON objects
		if !firstToken {
			buffer.WriteString(",")
		}

		buffer.WriteString("{\"Token\":")
		buffer.WriteString("\"")
		buffer.WriteString(tokenID)
		buffer.WriteString("\"")

		buffer.WriteString(", \"Contract\":")
		buffer.WriteString(string(contractBytes))
		buffer.WriteString("}")

		firstToken = false
	}
	buffer.WriteString("]")

	iterator.Close()

	return shim.Success(buffer.Bytes())
}
