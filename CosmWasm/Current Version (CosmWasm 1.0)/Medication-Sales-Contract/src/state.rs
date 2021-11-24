use schemars::JsonSchema;
use serde::{Deserialize, Serialize};

use cosmwasm_std::Addr;
use cw_storage_plus::Item;

#[derive(Serialize, Deserialize, Clone, Debug, PartialEq, JsonSchema)]
pub struct State {
    pub pharmacy: Addr,
    pub patient: Addr,
    pub source: Addr,
    pub medication : String,// medication name
    pub dosage : String, //ml or g 
    pub price : i32,
    pub count: i32,  // count medication sold to patient
    
}

pub const STATE: Item<State> = Item::new("state");
