
use cosmwasm_std::{Addr};
use schemars::JsonSchema;
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, Clone, Debug, PartialEq, JsonSchema)]
pub struct InstantiateMsg {
    pub doctor: String, //doctor address
    pub patient : String, // patient address
    pub personal_info: String,
    pub medication:String,
    pub diagnosis:String,
    pub count:i32,
}

#[derive(Serialize, Deserialize, Clone, Debug, PartialEq, JsonSchema)]
#[serde(rename_all = "snake_case")]
pub enum ExecuteMsg {
    CreatePrescription {personal_info:String,medication:String,diagnosis:String}
    //Reset { count: i32 },
}

#[derive(Serialize, Deserialize, Clone, Debug, PartialEq, JsonSchema)]
#[serde(rename_all = "snake_case")]
pub enum QueryMsg {
    // GetCount returns the current prescription as a json-encoded number
    GetCount {},
}

// We define a custom struct for each query response
#[derive(Serialize, Deserialize, Clone, Debug, PartialEq, JsonSchema)]
pub struct CountResponse {
    pub doctor: Addr,
    pub patient: Addr,
    pub owner: Addr,
    pub personal_info: String,
    pub medication:String,
    pub diagnosis:String,
    pub count:i32,
}
