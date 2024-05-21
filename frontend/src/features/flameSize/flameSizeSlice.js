import {createAsyncThunk, createSlice} from "@reduxjs/toolkit";
import {client} from "../../api/client";

const initialState = {
    flameSize: undefined,
}

export const fetchFlameSize = createAsyncThunk('flameSize/fetchFlameSize', async () => {
    const response = await client.get('/api/flame_size')
    return response
})

const flameSizeSlice = createSlice({
    name: 'flameSize',
    initialState,
    reducers: {

    },
    extraReducers: builder => {
        builder
            .addCase(fetchFlameSize.pending, (state, action) => {
                state.status = 'loading'
            })
            .addCase(fetchFlameSize.fulfilled, (state, action) => {
                state.flameSize = action.payload.flame_size
                state.status = 'idle'
            })
    }
});

export default flameSizeSlice.reducer