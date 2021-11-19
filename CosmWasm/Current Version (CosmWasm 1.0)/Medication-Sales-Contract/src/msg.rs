use cosmwasm_std::{Addr};
use schemars::JsonSchema;
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, Clone, Debug, PartialEq, JsonSchema)]
pub struct InstantiateMsg {
    pub pharmacy: String, //pharmacy address
    pub patient : String, // patient address
    pub medication : String,// medication name
    pub dosage : String, //ml or g 
    pub price : f32,
    pub count: i32,  // count medication sold to patient
}

#[derive(Serialize, Deserialize, Clone, Debug, PartialEq, JsonSchema)]
#[serde(rename_all = "snake_case")]
pub enum ExecuteMsg {
    Sell {medication:String,dosage:String,price:f32,},
    //Reset { count: i32 },
}

#[derive(Serialize, Deserialize, Clone, Debug, PartialEq, JsonSchema)]
#[serde(rename_all = "snake_case")]
pub enum QueryMsg {
    // GetCount returns the current medication sold as a json-encoded number
    GetStatus {},
}

// We define a custom struct for each query response
#[derive(Serialize, Deserialize, Clone, Debug, PartialEq, JsonSchema)]

// CountResponse
pub struct SalesResponse {
    pub medication:String,
    pub dosage: String,
    pub price: f32,
    pub count: i32,
    pub pharmacy: Addr,
    pub patient: Addr,
}

