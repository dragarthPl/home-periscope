import { combineReducers } from 'redux'

import temperatureReducer from './features/temperature/temepratureSlice'
import stoveStateReducer from './features/stoveState/stoveStateSlice'
import flameSizeReducer from './features/flameSize/flameSizeSlice'
import summerModeReducer from './features/summerMode/summerModeSlice'
const rootReducer = combineReducers({
  temperature: temperatureReducer,
  stoveState: stoveStateReducer,
  flameSize: flameSizeReducer,
  summerMode: summerModeReducer,
})

export default rootReducer