import { createSlice,
  createSelector,
  createAsyncThunk,
  createEntityAdapter,
} from '@reduxjs/toolkit'
import { client } from '../../api/client'

const initialState = {
  heatingTemperature: {
    minTemperature: undefined,
    maxTemperature: undefined,
    targetTemperature: undefined,
    current: undefined,
  },
  waterHeaterTemperature: {
    minTemperature: undefined,
    maxTemperature: undefined,
    targetTemperature: undefined,
    current: undefined,
  },
  mixerTemperature: {
    minTemperature: undefined,
    maxTemperature: undefined,
    targetTemperature: undefined,
    current: undefined,
  }
}

const temperatureAdapter = createEntityAdapter()

// const initialState = temperatureAdapter.getInitialState({
//   status: 'idle'
// })


export const fetchHeatingTemperature = createAsyncThunk('temperature/fetchHeatingTemperature', async () => {
  const response = await client.get('/api/heating_temperature')
  return response
})

const todosSlice = createSlice({
  name: 'temperature',
  initialState,
  reducers: {
    updateHeatingTemperature(state, action) {
      // ✅ This "mutating" code is okay inside of createSlice!
      const newTemperature = action.payload
      if (newTemperature !== undefined) {
        state.entities.heatingTemperature = {
          minTemperature: newTemperature.min_temperature,
          maxTemperature: newTemperature.max_temperature,
          targetTemperature: newTemperature.target_temperature,
          current: newTemperature.current,
        }
      }

    }
  },
  extraReducers: builder => {
    builder
      .addCase(fetchHeatingTemperature.pending, (state, action) => {
        state.status = 'loading'
      })
      .addCase(fetchHeatingTemperature.fulfilled, (state, action) => {
        const heatingTemperature = {}
        heatingTemperature.minTemperature = action.payload.min_temperature
        heatingTemperature.maxTemperature = action.payload.max_temperature
        heatingTemperature.targetTemperature = action.payload.target_temperature
        heatingTemperature.current = action.payload.current
        state.heatingTemperature = heatingTemperature
        state.status = 'idle'
      })
  }
})

export const { updateHeatingTemperature } = todosSlice.actions

export default todosSlice.reducer

export const {
  selectAll: selectTemperatures,
} = temperatureAdapter.getSelectors((state) => state.heatingTemperature)

export const selectHeatingTemperature = createSelector(
  // Pass our other memoized selector as an input
  selectTemperatures,
  // And derive data in the output selector
  (temperatures) => temperatures => temperatures
)