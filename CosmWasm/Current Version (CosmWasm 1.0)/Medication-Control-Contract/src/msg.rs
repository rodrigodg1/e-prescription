use cosmwasm_std::{Addr};
use schemars::JsonSchema;
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, Clone, Debug, PartialEq, JsonSchema)]
pub struct InstantiateMsg {
    pub regulator: String,
    pub pharmacy: String,
    pub amount_medication_supplied: i32,
    pub amount_medication_sold:i32,

}

#[derive(Serialize, Deserialize, Clone, Debug, PartialEq, JsonSchema)]
#[serde(rename_all = "snake_case")]
pub enum ExecuteMsg {
    UpdateMedication{amount_sold:i32},
    Supply { amount: i32 },
}

#[derive(Serialize, Deserialize, Clone, Debug, PartialEq, JsonSchema)]
#[serde(rename_all = "snake_case")]
pub enum QueryMsg {
    // GetCount returns the current count as a json-encoded number
    GetCount {},
}

// We define a custom struct for each query response
#[derive(Serialize, Deserialize, Clone, Debug, PartialEq, JsonSchema)]
pub struct CountResponse {
    pub regulator: Addr,
    pub pharmacy: Addr,
    pub owner: Addr,
    pub amount_medication_supplied: i32,
    pub amount_medication_sold: i32,
    pub amount_available_medication : i32,

}
