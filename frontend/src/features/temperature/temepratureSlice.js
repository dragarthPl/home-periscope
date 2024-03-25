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


export const fetchHeatingTemperature = createAsyncThunk('temperature/fetchHeatingTemperature', async () => {
  const response = await client.get('/api/heating_temperature')
  return response
})
export const fetchMixerTemperature = createAsyncThunk('temperature/fetchMixerTemperature', async () => {
  const response = await client.get('/api/mixer_temperature')
  return response
})

export const fetchWaterHeaterTemperature = createAsyncThunk('temperature/fetchWaterHeatingTemperature', async () => {
  const response = await client.get('/api/water_heater_temperature')
  return response
})

export const setHeatingTemperature = createAsyncThunk('temperature/setHeatingTemperature', async (temperature) => {
    const response = await client.post('/api/heating_temperature', {temperature: temperature})
    return response
})

export const setMixerTemperature = createAsyncThunk('temperature/setMixerTemperature', async (temperature) => {
    const response = await client.post('/api/mixer_temperature', {temperature: temperature})
    return response
})

export const setWaterHeaterTemperature = createAsyncThunk('temperature/setWaterHeatingTemperature', async (temperature) => {
    const response = await client.post('/api/water_heater_temperature', {temperature: temperature})
    return response
})

const todosSlice = createSlice({
  name: 'temperature',
  initialState,
  reducers: {
    updateHeatingTemperature(state, action) {
      const newTemperature = action.payload
      if (newTemperature !== undefined) {
        state.entities.heatingTemperature = {
          minTemperature: newTemperature.min_temperature,
          maxTemperature: newTemperature.max_temperature,
          targetTemperature: newTemperature.target_temperature,
          current: newTemperature.current,
        }
      }
    },
    updateMixerTemperature(state, action) {
      const newTemperature = action.payload
      if (newTemperature !== undefined) {
        state.entities.mixerTemperature = {
          minTemperature: newTemperature.min_temperature,
          maxTemperature: newTemperature.max_temperature,
          targetTemperature: newTemperature.target_temperature,
          current: newTemperature.current,
        }
      }
    },
    updateWaterHeaterTemperature(state, action) {
      const newTemperature = action.payload
      if (newTemperature !== undefined) {
        state.entities.waterHeaterTemperature = {
          minTemperature: newTemperature.min_temperature,
          maxTemperature: newTemperature.max_temperature,
          targetTemperature: newTemperature.target_temperature,
          current: newTemperature.current,
        }
      }
    },
    changeSliceHeatingTemperature(state, action) {
      state.heatingTemperature.targetTemperature = action.payload
    },
    changeSliceMixerTemperature(state, action) {
      state.mixerTemperature.targetTemperature = action.payload
    },
    changeSliceWaterHeaterTemperature(state, action) {
      state.waterHeaterTemperature.targetTemperature = action.payload
    },
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
      .addCase(setHeatingTemperature.pending, (state, action) => {
        state.status = 'loading'
      })
      .addCase(setHeatingTemperature.fulfilled, (state, action) => {
        const heatingTemperature = {}
        heatingTemperature.minTemperature = action.payload.min_temperature
        heatingTemperature.maxTemperature = action.payload.max_temperature
        heatingTemperature.targetTemperature = action.payload.target_temperature
        heatingTemperature.current = action.payload.current
        state.heatingTemperature = heatingTemperature
      })
      .addCase(fetchMixerTemperature.pending, (state, action) => {
        state.status = 'loading'
      })
      .addCase(fetchMixerTemperature.fulfilled, (state, action) => {
        const mixerTemperature = {}
        mixerTemperature.minTemperature = action.payload.min_temperature
        mixerTemperature.maxTemperature = action.payload.max_temperature
        mixerTemperature.targetTemperature = action.payload.target_temperature
        mixerTemperature.current = action.payload.current
        state.mixerTemperature = mixerTemperature
        state.status = 'idle'
      })
      .addCase(setMixerTemperature.pending, (state, action) => {
        state.status = 'loading'
      })
      .addCase(setMixerTemperature.fulfilled, (state, action) => {
        const mixerTemperature = {}
        mixerTemperature.minTemperature = action.payload.min_temperature
        mixerTemperature.maxTemperature = action.payload.max_temperature
        mixerTemperature.targetTemperature = action.payload.target_temperature
        mixerTemperature.current = action.payload.current
        state.mixerTemperature = mixerTemperature
      })
      .addCase(fetchWaterHeaterTemperature.pending, (state, action) => {
        state.status = 'loading'
      })
      .addCase(fetchWaterHeaterTemperature.fulfilled, (state, action) => {
        const waterHeaterTemperature = {}
        waterHeaterTemperature.minTemperature = action.payload.min_temperature
        waterHeaterTemperature.maxTemperature = action.payload.max_temperature
        waterHeaterTemperature.targetTemperature = action.payload.target_temperature
        waterHeaterTemperature.current = action.payload.current
        state.waterHeaterTemperature = waterHeaterTemperature
        state.status = 'idle'
      })
      .addCase(setWaterHeaterTemperature.pending, (state, action) => {
        state.status = 'loading'
      })
      .addCase(setWaterHeaterTemperature.fulfilled, (state, action) => {
        const waterHeaterTemperature = {}
        waterHeaterTemperature.minTemperature = action.payload.min_temperature
        waterHeaterTemperature.maxTemperature = action.payload.max_temperature
        waterHeaterTemperature.targetTemperature = action.payload.target_temperature
        waterHeaterTemperature.current = action.payload.current
        state.waterHeaterTemperature = waterHeaterTemperature
      })
  }
})

export const {
  updateHeatingTemperature,
  updateMixerTemperature,
  updateWaterHeaterTemperature,
  changeSliceHeatingTemperature,
  changeSliceMixerTemperature,
  changeSliceWaterHeaterTemperature,
} = todosSlice.actions

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