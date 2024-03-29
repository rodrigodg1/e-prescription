use schemars::JsonSchema;
use serde::{Deserialize, Serialize};

use cosmwasm_std::Addr;
use cw_storage_plus::Item;

#[derive(Serialize, Deserialize, Clone, Debug, PartialEq, JsonSchema)]
pub struct State {
    pub origin: Addr,
    pub regulator: Addr,
    pub owner: Addr,
    pub data : String,// data report
    pub count: i32,  // count reports made by user
}

pub const STATE: Item<State> = Item::new("state");
