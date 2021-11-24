use schemars::JsonSchema;
use serde::{Deserialize, Serialize};

use cosmwasm_std::Addr;
use cw_storage_plus::Item;

#[derive(Serialize, Deserialize, Clone, Debug, PartialEq, JsonSchema)]
pub struct State {
    pub regulator: Addr,
    pub pharmacy: Addr,
    pub owner: Addr, //instance owner
    pub amount_medication_supplied: i32, //supplied by regulator
    pub amount_medication_sold:i32, // notified by the pharmacy
    pub amount_available_medication:i32, // calculated by contract
    
}

pub const STATE: Item<State> = Item::new("state");
