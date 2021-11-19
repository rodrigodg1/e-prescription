use cosmwasm_std::{Addr};
use schemars::JsonSchema;
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, Clone, Debug, PartialEq, JsonSchema)]
pub struct InstantiateMsg {
    pub owner: String, //who makes report address
    pub regulator : String, // regulator address
    pub data : String,// medication name
    pub count: i32,  // count medication sold to patient
}

#[derive(Serialize, Deserialize, Clone, Debug, PartialEq, JsonSchema)]
#[serde(rename_all = "snake_case")]
pub enum ExecuteMsg {
    Report {data:String},
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
pub struct ReportResponse {
    //pub medication:String,
    pub regulator: Addr,
    pub data: String,
    pub count: i32,
}

