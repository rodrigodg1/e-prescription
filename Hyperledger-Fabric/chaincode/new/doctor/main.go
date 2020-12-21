package main

import "github.com/hyperledger/fabric/core/chaincode/shim"

func main() {
	err := shim.Start(new(Contract))
	if err != nil {
		panic(err)
	}
}
