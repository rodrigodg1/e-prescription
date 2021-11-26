use schemars::JsonSchema;
use serde::{Deserialize, Serialize};

use cosmwasm_std::Addr;
use cw_storage_plus::Item;

#[derive(Serialize, Deserialize, Clone, Debug, PartialEq, JsonSchema)]
pub struct State {
    pub doctor: Addr,
    pub patient: Addr,
    //pub owner: Addr, //owner = who creates a instance  = doctor
    pub personal_info:String,
    pub medication:String,
    pub diagnosis:String,
    pub count:i32, // count updates in contract (i.e., new prescription)
    pub last_access: Addr,
}

pub const STATE: Item<State> = Item::new("state");
