import { combineReducers } from 'redux'

import temperatureReducer from './features/temperature/temepratureSlice'
import stoveStateReducer from './features/stoveState/stoveStateSlice'
import flameSizeReducer from './features/flameSize/flameSizeSlice'
const rootReducer = combineReducers({
  temperature: temperatureReducer,
  stoveState: stoveStateReducer,
  flameSize: flameSizeReducer,
})

export default rootReducer