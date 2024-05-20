import {createAsyncThunk, createSlice} from "@reduxjs/toolkit";
import {client} from "../../api/client";

const initialState = {
  stoveState: undefined,
}

export const fetchStoveState = createAsyncThunk('temperature/fetchStoveState', async () => {
  const response = await client.get('/api/stove_state')
  return response
})

const stoveStateSlice = createSlice({
  name: 'stoveState',
  initialState,
  reducers: {

  },
  extraReducers: builder => {
    builder
        .addCase(fetchStoveState.pending, (state, action) => {
          state.status = 'loading'
        })
        .addCase(fetchStoveState.fulfilled, (state, action) => {
          const stoveState = {}
          stoveState.stoveState = action.payload.stove_state
          state.stoveState = stoveState
          state.status = 'idle'
        })
  }
});

export default stoveStateSlice.reducer


