#[cfg(not(feature = "library"))]
use cosmwasm_std::entry_point;
use cosmwasm_std::{to_binary, Binary, Deps, DepsMut, Env, MessageInfo, Response, StdResult};
use cw2::set_contract_version;

use crate::error::ContractError;
use crate::msg::{ExecuteMsg, InstantiateMsg, QueryMsg, ReportResponse};
use crate::state::{State, STATE};

// version info for migration info
const CONTRACT_NAME: &str = "crates.io:report-contract";
const CONTRACT_VERSION: &str = env!("CARGO_PKG_VERSION");

#[cfg_attr(not(feature = "library"), entry_point)]
pub fn instantiate(
    deps: DepsMut,
    _env: Env,
    info: MessageInfo,
    msg: InstantiateMsg,
) -> Result<Response, ContractError> {
    let state = State {
        origin: deps.api.addr_validate(&msg.origin)?,
        regulator: deps.api.addr_validate(&msg.regulator)?,
        owner: info.sender,
        data:msg.data,
        count: msg.count,
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
        ExecuteMsg::Report {data} => try_report(deps, info,data),
        //ExecuteMsg::Reset { count } => try_reset(deps, info, count),
    }
}

pub fn try_report(
    deps: DepsMut,
    //env: Env,
    info: MessageInfo,
    data: String,

    ) -> Result<Response, ContractError> {
    STATE.update(deps.storage, |mut state| -> Result<_, ContractError> {
        if info.sender != state.owner {
            return Err(ContractError::Unauthorized {});
        }
   
        state.data = data;
        state.count += 1;

        Ok(state)

    })?;

    Ok(Response::new().add_attribute("method", "try_report"))
}

#[cfg_attr(not(feature = "library"), entry_point)]
pub fn query(deps: Deps, _env: Env, msg: QueryMsg) -> StdResult<Binary> {
    match msg {
        QueryMsg::GetStatus {} => to_binary(&query_report(deps)?),
    }
}

fn query_report(deps: Deps) -> StdResult<ReportResponse> {
    let state = STATE.load(deps.storage)?;
    Ok(ReportResponse { 
        origin:state.origin,
        regulator:state.regulator,
        owner:state.owner,
        data:state.data,
        count: state.count,
 })
}

