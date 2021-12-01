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
        request_origin_name: msg.request_origin_name,
        request_origin_addr: deps.api.addr_validate(&msg.request_origin_addr)?,
        patient_addr: deps.api.addr_validate(&msg.patient)?,
        patient_consent: msg.patient_consent,
        description: msg.description,
        count_requests:msg.count_requests,
        last_update_addr: info.sender,
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
        ExecuteMsg::RequestAccess{} => try_create(deps,info),
        
        ExecuteMsg::Consent {} => try_consent(deps, info),
        
    }
}

pub fn try_create(deps: DepsMut,info: MessageInfo) -> Result<Response, ContractError> {
    STATE.update(deps.storage, |mut state| -> Result<_, ContractError> {

        // only accepts transactions comming from instance creator
        if info.sender != state.request_origin_addr {
            return Err(ContractError::Unauthorized {});
        }
        let consent_=String::from("NOT AUTHORIZED YET");
        let description_=String::from("Access to prescription data not yet authorized by the patient. Wait for authorization");

        state.patient_consent = consent_;
        state.description = description_;
        state.count_requests += 1;
        //tracking
        
        state.last_update_addr = info.sender;
        Ok(state)
    })?;

    Ok(Response::new().add_attribute("method", "try_create"))
}



pub fn try_consent(deps: DepsMut,info: MessageInfo) -> Result<Response, ContractError> {
    STATE.update(deps.storage, |mut state| -> Result<_, ContractError> {

        // only accepts consent transaction comming from patient
        if info.sender != state.patient_addr {
            return Err(ContractError::Unauthorized {});
        }

        let consent_=String::from("AUTHORIZED");
        let description_=String::from("Access to prescription data was authorized by the patient");


        state.patient_consent = consent_;
        state.description = description_;
        
        //tracking
        state.last_update_addr = info.sender;
        Ok(state)
    })?;

    Ok(Response::new().add_attribute("method", "try_create"))
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
        request_origin_name:state.request_origin_name,
        request_origin_addr:state.request_origin_addr,
        patient_addr: state.patient_addr,
        patient_consent: state.patient_consent,
        description: state.description,
        count_requests:state.count_requests,
        last_update_addr:state.last_update_addr})
}


