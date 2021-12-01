use schemars::JsonSchema;
use serde::{Deserialize, Serialize};

use cosmwasm_std::Addr;
use cw_storage_plus::Item;

#[derive(Serialize, Deserialize, Clone, Debug, PartialEq, JsonSchema)]

pub struct State {
    pub request_origin_name: String, // request name (e.g., pharmacy, doctor ...)
    pub request_origin_addr: Addr, // create the request
    pub patient_addr: Addr, // receives the request 
    pub patient_consent: String, //  Only updated by patient (Authorized or not authorized), 
    pub description: String, // Description about consent status
    pub count_requests:i32, // count requests in contract (i.e., new request)
    pub last_update_addr: Addr, //stores who last updated the contract
}



pub const STATE: Item<State> = Item::new("state");
