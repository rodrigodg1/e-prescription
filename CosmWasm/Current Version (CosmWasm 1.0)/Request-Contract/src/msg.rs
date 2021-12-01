
use cosmwasm_std::{Addr};
use schemars::JsonSchema;
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, Clone, Debug, PartialEq, JsonSchema)]
pub struct InstantiateMsg {
    pub request_origin_name : String,
    pub request_origin_addr: String, //pharmacy, regulator or analyst address
    pub patient: String, //patient address
    pub patient_consent: String,
    pub description: String,
    pub count_requests:i32, //request count
    //pub last_request_addr: String, //store last request
}

#[derive(Serialize, Deserialize, Clone, Debug, PartialEq, JsonSchema)]
#[serde(rename_all = "snake_case")]
pub enum ExecuteMsg {
    RequestAccess {},
    Consent{},
    
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
    pub request_origin_name: String,
    pub request_origin_addr: Addr,
    pub patient_addr: Addr,
    pub patient_consent: String,
    pub description: String,
    pub count_requests:i32,
    pub last_update_addr:Addr,
}
