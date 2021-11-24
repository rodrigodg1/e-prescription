#[cfg(not(feature = "library"))]
use cosmwasm_std::entry_point;
use cosmwasm_std::{to_binary, Binary, Deps, DepsMut, Env, MessageInfo, Response, StdResult};
use cw2::set_contract_version;

use crate::error::ContractError;
use crate::msg::{CountResponse, ExecuteMsg, InstantiateMsg, QueryMsg};
use crate::state::{State, STATE};

// version info for migration info
const CONTRACT_NAME: &str = "crates.io:medication-control-contract";
const CONTRACT_VERSION: &str = env!("CARGO_PKG_VERSION");

#[cfg_attr(not(feature = "library"), entry_point)]
pub fn instantiate(
    deps: DepsMut,
    _env: Env,
    info: MessageInfo,
    msg: InstantiateMsg,
) -> Result<Response, ContractError> {
    let state = State {
        regulator: deps.api.addr_validate(&msg.regulator)?,
        pharmacy: deps.api.addr_validate(&msg.pharmacy)?,
        owner: info.sender, //instance owner
        amount_medication_supplied: msg.amount_medication_supplied,
        amount_medication_sold: msg.amount_medication_sold,
        amount_available_medication: msg.amount_medication_supplied,
    };
    set_contract_version(deps.storage, CONTRACT_NAME, CONTRACT_VERSION)?;
    STATE.save(deps.storage, &state)?;

    Ok(Response::default())
}

#[cfg_attr(not(feature = "library"), entry_point)]
pub fn execute(
    deps: DepsMut,
    _env: Env,
    info: MessageInfo,
    msg: ExecuteMsg,
) -> Result<Response, ContractError> {
    match msg {
        ExecuteMsg::UpdateMedication{amount_sold} => try_update(deps,info,amount_sold),
        ExecuteMsg::Supply { amount } => try_supply(deps, info, amount),
    }
}

pub fn try_update(deps: DepsMut,info:MessageInfo,amount_sold:i32) -> Result<Response, ContractError> {
    STATE.update(deps.storage, |mut state| -> Result<_, ContractError> {
        //only pharmacy can update medication sold
        if info.sender != state.pharmacy {
            return Err(ContractError::Unauthorized {});
        }
   
        state.amount_medication_sold += amount_sold;
        state.amount_available_medication = state.amount_available_medication - state.amount_medication_sold;

        Ok(state)
    })?;

    Ok(Response::new().add_attribute("method", "try_update"))
}

pub fn try_supply(deps: DepsMut, info: MessageInfo, amount: i32) -> Result<Response, ContractError> {
    STATE.update(deps.storage, |mut state| -> Result<_, ContractError> {
        if info.sender != state.owner {
            return Err(ContractError::Unauthorized {});
        }
        state.amount_medication_supplied += amount;
        state.amount_available_medication += amount;
        Ok(state)
    })?;
    Ok(Response::new().add_attribute("method", "supply"))
}



#[cfg_attr(not(feature = "library"), entry_point)]
pub fn query(deps: Deps, _env: Env, msg: QueryMsg) -> StdResult<Binary> {
    match msg {
        QueryMsg::GetCount {} => to_binary(&query_count(deps)?),
    }
}

fn query_count(deps: Deps) -> StdResult<CountResponse> {
    let state = STATE.load(deps.storage)?;
    Ok(CountResponse { 
        regulator:state.regulator,
        pharmacy:state.pharmacy,
        owner:state.owner,
        amount_medication_supplied:state.amount_medication_supplied,
        amount_medication_sold: state.amount_medication_sold,
        amount_available_medication: state.amount_available_medication
 })
}


