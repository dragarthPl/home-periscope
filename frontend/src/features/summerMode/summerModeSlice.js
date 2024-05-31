import {createAsyncThunk, createSlice} from "@reduxjs/toolkit";
import {client} from "../../api/client";

const initialState = {
    summerMode: undefined,
}

export const fetchSummerMode = createAsyncThunk('summerMode/fetchSummerMode', async () => {
    const response = await client.get('/api/summer_mode')
    return response
})

const summerModeSlice = createSlice({
    name: 'summerMode',
    initialState,
    reducers: {

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
    }
});

export default summerModeSlice.reducer