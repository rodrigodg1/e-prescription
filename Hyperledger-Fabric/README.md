# Healthcare-blockchain

Decentralized healthcare application using Hyperledger Fabric - done for educational purposes.

# Structure of the project

 - **chaincode** - Smart contracts
	 - **old-prototype** - Unused prototype of the application using a single smart contract
	 - **new** - All the recent smart contracts
		 - **doctor** - Contract used on medical appointments between a patient and the doctor/hospital;
		 - **pharmacy** - Contract used on pharmacy sales between the patient and the pharmacy application;
- **api** - TODO - API that will consume the application
- **network** - TODO - network configuration files for a test network

# Chaincode description
## Doctor
The doctor smart contract is used whenever the patient has a medical appointment that requires medication/diagnostic prescriptions. The doctor is responsible for using the patient address to generate a new entry on the ledger for the appointment, used to document the prescription.

## Pharmacy
The pharmacy smart contract is used on pharmacy sales, whether they are related to medical prescriptions or not. The pharmacy is responsible for registering the sale record on the ledger using the patient address for later queries.

# Sequence diagram

TODO

# License
[This code is available under the MIT license.](https://github.com/gabrielzut/healthcare-blockchain/blob/main/LICENSE)
