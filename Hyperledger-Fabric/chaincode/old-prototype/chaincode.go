package main

import (
	"encoding/json"
	"strconv"
	"time"

	"github.com/hyperledger/fabric/core/chaincode/shim"
	sc "github.com/hyperledger/fabric/protos/peer"
)

type Prescription struct {
	Id         int       `json:"id"`
	Date       time.Time `json:"date"`
	DoctorId   int       `json:"doctorId"`
	Medication string    `json:"medication"`
}

type Diagnostic struct {
	Id       int       `json:"id"`
	Date     time.Time `json:"date"`
	DoctorId int       `json:"doctorId"`
	Notes    string    `json:"notes"`
}

type Register struct {
	Id            int            `json:"id"`
	prescriptions []Prescription `json:"prescriptions"`
	diagnostics   []Diagnostic   `json:"diagnostics"`
}

func (reg *Register) Init(stub shim.ChaincodeStubInterface) sc.Response {
	return shim.Success(nil)
}

func (reg *Register) Invoke(stub shim.ChaincodeStubInterface) sc.Response {
	fcn, params := stub.GetFunctionAndParameters()

	switch fcn {
	case "register":
		return reg.register(stub, params)
	case "delete":
		return reg.delete(stub, params)
	case "get":
		return reg.get(stub, params)
	default:
		return shim.Error("Invalid function")
	}
}

func (reg *Register) register(stub shim.ChaincodeStubInterface, args []string) sc.Response {
	if len(args) != 3 {
		return shim.Error("Wrong number of arguments! Expected 3 but got " + strconv.Itoa(len(args)))
	}

	register, err := readAndValidateArgs(args)

	if err != nil {
		return shim.Error("Error validating data: " + err.Error())
	}

	registerBytes, err := json.Marshal(register)

	if err != nil {
		return shim.Error("Error converting data: " + err.Error())
	}

	err = stub.PutState(strconv.Itoa(register.Id), registerBytes)

	if err != nil {
		return shim.Error("Error saving register: " + err.Error())
	}

	return shim.Success(nil)
}

func (reg *Register) delete(stub shim.ChaincodeStubInterface, args []string) sc.Response {
	if len(args) != 1 {
		return shim.Error("Wrong number of arguments! Expected 1 but got " + strconv.Itoa(len(args)))
	}

	err := stub.DelState(args[0])

	if err != nil {
		return shim.Error("Error deleting register: " + err.Error())
	}

	return shim.Success(nil)
}

func (reg *Register) get(stub shim.ChaincodeStubInterface, args []string) sc.Response {
	if len(args) != 1 {
		return shim.Error("Wrong number of arguments! Expected 1 but got " + strconv.Itoa(len(args)))
	}

	registerBytes, err := stub.GetState(args[0])

	if err != nil {
		return shim.Error("Error getting state: " + err.Error())
	} else if registerBytes == nil {
		return shim.Error("Register not found")
	}

	return shim.Success(registerBytes)
}

func readAndValidateArgs(args []string) (*Register, error) {
	id, err := strconv.Atoi(args[0])

	var register Register

	register.Id = id

	if err != nil {
		return nil, err
	}

	err = json.Unmarshal([]byte(args[1]), register.prescriptions)

	if err != nil {
		return nil, err
	}

	err = json.Unmarshal([]byte(args[2]), register.diagnostics)

	if err != nil {
		return nil, err
	}

	return &register, nil
}
