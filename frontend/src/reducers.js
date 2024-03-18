import { combineReducers } from 'redux'

import temperatureReducer from './features/temperature/temepratureSlice'

const rootReducer = combineReducers({
  temperature: temperatureReducer,
})

export default rootReducer