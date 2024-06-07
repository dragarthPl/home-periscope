import {createAsyncThunk, createEntityAdapter, createSlice} from "@reduxjs/toolkit";
import {client} from "../../api/client";
import {setHeatingTemperature} from "../temperature/temepratureSlice";

const initialState = {
    summerMode: undefined,
}

const summerModeAdapter = createEntityAdapter()

export const fetchSummerMode = createAsyncThunk('summerMode/fetchSummerMode', async () => {
    const response = await client.get('/api/summer_mode')
    return response
})

export const setSummerMode = createAsyncThunk('summerMode/setSummerMode', async (summerMode) => {
    const response = await client.post('/api/summer_mode', {summerMode: summerMode})
    return response
})

const summerModeSlice = createSlice({
    name: 'summerMode',
    initialState,
    reducers: {
      updateSummerMode(state, action) {
        const newSummerMode = action.payload
        if (newSummerMode !== undefined) {
          state.entities.summerMode = newSummerMode
        }
      },
    },
    extraReducers: builder => {
        builder
            .addCase(fetchSummerMode.pending, (state, action) => {
                state.status = 'loading'
            })
            .addCase(fetchSummerMode.fulfilled, (state, action) => {
                const summerMode = {}
                summerMode.summerMode = action.payload.summer_mode
                state.summerMode = summerMode
                state.status = 'idle'
            })
            .addCase(setSummerMode.pending, (state, action) => {
                state.status = 'loading'
            })
            .addCase(setHeatingTemperature.fulfilled, (state, action) => {
                const summerMode = {}
                summerMode.summerMode = action.payload.summer_mode
                state.summerMode = summerMode
              })
    }
});

export default summerModeSlice.reducer