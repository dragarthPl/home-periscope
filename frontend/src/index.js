import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { store } from './store'
import { Provider } from 'react-redux'
import {fetchHeatingTemperature, fetchMixerTemperature, fetchWaterHeaterTemperature} from "./features/temperature/temepratureSlice";
import {fetchStoveState} from "./features/stoveState/stoveStateSlice";

const root = ReactDOM.createRoot(document.getElementById('root'));

store.dispatch(fetchHeatingTemperature());
store.dispatch(fetchMixerTemperature());
store.dispatch(fetchWaterHeaterTemperature());
store.dispatch(fetchStoveState());

root.render(
  <React.StrictMode>
    <Provider store={store}>
        <App />
    </Provider>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
