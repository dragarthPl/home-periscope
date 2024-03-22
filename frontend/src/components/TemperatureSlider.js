import React from 'react';
import Typography from "@mui/material/Typography";
import DeviceThermostatIcon from "@mui/icons-material/DeviceThermostat";
import Slider from "@mui/material/Slider";
import Paper from "@mui/material/Paper";

const prepareMarks = (min, max) => {
    const marks = [];
    const minTemperature = min % 5 === 0 ? min : min - min % 5;
    const maxTemperature = max % 5 === 0 ? max : max + 5 - max % 5;
    for (let i = minTemperature; i <= maxTemperature; i += 5) {
        marks.push({value: i, label: `${i}°C`})
    }
    return marks;
}

const TemperatureSlider = ({ minTemperature, maxTemperature, targetTemperature, current, color, onChangeCommitted }) => {
  const marks = prepareMarks(minTemperature, maxTemperature);

    return (
        <Paper sx={{padding: 4, display: "flex", overflow: "auto", flexDirection: "column"}}>
          <Typography component="h2" variant="h6" gutterBottom sx={{justifyContent: "flex-start",display: "flex", alignItems: "center",}}>
              <DeviceThermostatIcon sx={{ color: color, fontSize: 30}} />
              <Typography sx={{justifyContent: "flex-start",display: "flex", alignItems: "center", fontSize: 20}}>Temperatura kotła: </Typography>
              <Typography sx={{justifyContent: "flex-start",display: "flex", alignItems: "center", color: color, marginLeft: 1, fontSize: 20}} > {current}°C</Typography>
          </Typography>
          <Slider
              min={minTemperature}
              max={maxTemperature}
              step={1}
              marks={marks}
              defaultValue={targetTemperature}
              valueLabelDisplay="auto"
              aria-labelledby="input-slider"
              sx={{color: color}}
              onChangeCommitted={onChangeCommitted}
          />
        </Paper>
    )
}
export default TemperatureSlider;