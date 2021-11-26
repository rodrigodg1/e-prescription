#[cfg(not(feature = "library"))]
use cosmwasm_std::entry_point;
use cosmwasm_std::{to_binary, Binary, Deps, DepsMut, Env, MessageInfo, Response, StdResult};
use cw2::set_contract_version;

use crate::error::ContractError;
use crate::msg::{CountResponse, ExecuteMsg, InstantiateMsg, QueryMsg};
use crate::state::{State, STATE};

// version info for migration info
const CONTRACT_NAME: &str = "crates.io:prescription-contract";
const CONTRACT_VERSION: &str = env!("CARGO_PKG_VERSION");

#[cfg_attr(not(feature = "library"), entry_point)]
pub fn instantiate(
    deps: DepsMut,
    _env: Env,
    info: MessageInfo,
    msg: InstantiateMsg,
) -> Result<Response, ContractError> {
    let state = State {
        doctor: deps.api.addr_validate(&msg.doctor)?,
        patient: deps.api.addr_validate(&msg.patient)?,
        //owner: info.sender,
        personal_info: msg.personal_info,
        medication : msg.medication,
        diagnosis : msg.diagnosis,
        count:msg.count,
        last_access: info.sender,
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
        ExecuteMsg::CreatePrescription{personal_info,medication,diagnosis} => try_create(deps,info,personal_info,medication,diagnosis),
        //for tracking
        ExecuteMsg::Tracking {} => try_tracking(deps, info),
    }
}

pub fn try_create(deps: DepsMut,info: MessageInfo,personal_info:String,medication:String,diagnosis:String) -> Result<Response, ContractError> {
    STATE.update(deps.storage, |mut state| -> Result<_, ContractError> {
        if info.sender != state.doctor {
            return Err(ContractError::Unauthorized {});
        }
        state.personal_info = personal_info;
        state.medication = medication;
        state.diagnosis = diagnosis;
        state.count += 1;
        //tracking
        state.last_access = info.sender;
        Ok(state)
    })?;

    Ok(Response::new().add_attribute("method", "try_create"))
}



pub fn try_tracking(deps: DepsMut,info: MessageInfo) -> Result<Response, ContractError> {
    STATE.update(deps.storage, |mut state| -> Result<_, ContractError> {
        //tracking = update contract state with only address
        state.last_access = info.sender;
        Ok(state)
    })?;

    Ok(Response::new().add_attribute("method", "try_tracking"))
}


#[cfg_attr(not(feature = "library"), entry_point)]
pub fn query(deps: Deps, _env: Env, msg: QueryMsg) -> StdResult<Binary> {
    match msg {
        QueryMsg::GetCount {} => to_binary(&query_count(deps)?),
    }
}




fn query_count(deps: Deps) -> StdResult<CountResponse> {

    let state = STATE.load(deps.storage)?;
    Ok(CountResponse { doctor:state.doctor, patient: state.patient,personal_info: state.personal_info, medication:state.medication, diagnosis:state.diagnosis,count:state.count,last_access:state.last_access})
}


