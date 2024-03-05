import homePeriscopeLogo from './home-periscope.png';
import './App.css';
import { red } from '@mui/material/colors';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Slider from '@mui/material/Slider';
import Typography from '@mui/material/Typography';
import DeviceThermostatIcon from "@mui/icons-material/DeviceThermostat";

const marks = [
  {
    value: 20,
    label: '20°C',
  },
  {
    value: 30,
    label: '30°C',
  },
  {
    value: 40,
    label: '40°C',
  },
    {
    value: 40,
    label: '40°C',
  },
    {
    value: 50,
    label: '50°C',
  },
    {
    value: 60,
    label: '60°C',
  },
  {
    value: 70,
    label: '70°C',
  },
    {
    value: 80,
    label: '80°C',
  },
    {
    value: 85,
    label: '90°C',
  },
];

function App() {
  return (
    <div className="App">
      <Box sx={{ flexDirection: 'row' }}>
        <img src={homePeriscopeLogo} className="App-logo-periscope" alt="logo"/>
        <Typography id="input-slider" gutterBottom>
            Home periscope
        </Typography>
      </Box>
      <Box sx={{ width: 450 }}>
        <Typography id="input-slider" gutterBottom>
            Temperatura kotła
        </Typography>
        <Grid container spacing={2} alignItems="center">
          <Grid item>
            <DeviceThermostatIcon sx={{ color: red[600], fontSize: 30}} />
          </Grid>
          <Grid item xs>
            <Slider
                min={20}
                max={85}
                step={1}
                marks={marks}
                defaultValue={30}
                valueLabelDisplay="auto"
                aria-labelledby="input-slider"
                sx={{ color: red[600]}}
            />
            </Grid>
        </Grid>
      </Box>
    </div>
  );
}

export default App;
