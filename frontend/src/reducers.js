import { combineReducers } from 'redux'

import temperatureReducer from './features/temperature/temepratureSlice'
import stoveStateReducer from './features/stoveState/stoveStateSlice'
const rootReducer = combineReducers({
  temperature: temperatureReducer,
  stoveState: stoveStateReducer,
})

export default rootReducer