import homePeriscopeLogo from './home-periscope.png';
import './App.css';
import {blue, orange, red} from '@mui/material/colors';
import React, { useState, useEffect } from 'react';

import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import MenuIcon from '@mui/icons-material/Menu';
import IconButton from '@mui/material/IconButton';
import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Slider from '@mui/material/Slider';
import Typography from '@mui/material/Typography';
import DeviceThermostatIcon from "@mui/icons-material/DeviceThermostat";
import Container from "@mui/material/Container";
import Paper from "@mui/material/Paper";
import HeatingTemperature from './features/temperature/HeatingTemperature';

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
        <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar>
          {/*<IconButton*/}
          {/*  size="large"*/}
          {/*  edge="start"*/}
          {/*  color="inherit"*/}
          {/*  aria-label="menu"*/}
          {/*  sx={{ mr: 2 }}*/}
          {/*>*/}
          {/*  <MenuIcon />*/}
          {/*</IconButton>*/}
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            Home periscope
          </Typography>

        </Toolbar>
      </AppBar>
    </Box>

        <main className="Main">
          <Container maxWidth="lg" sx={{paddingTop: 4, paddingBottom: 4}}>
            <Grid container spacing={3}>


              <Grid item xs={12} md={3} lg={6}>
                <HeatingTemperature />
                <Paper sx={{padding: 4, display: "flex", overflow: "auto", flexDirection: "column"}}>
                  <Typography component="h2" variant="h6" gutterBottom sx={{justifyContent: "flex-start",display: "flex", alignItems: "center",}}>
                    <DeviceThermostatIcon sx={{ color: orange[600], fontSize: 30}} /> Temperatura mieszacza
                  </Typography>
                  <Slider
                      min={20}
                      max={85}
                      step={1}
                      marks={marks}
                      defaultValue={30}
                      valueLabelDisplay="auto"
                      aria-labelledby="input-slider"
                      sx={{color: orange[600]}}
                  />
                </Paper>
                <Paper sx={{padding: 4, display: "flex", overflow: "auto", flexDirection: "column"}}>
                  <Typography component="h2" variant="h6" gutterBottom sx={{justifyContent: "flex-start",display: "flex", alignItems: "center",}}>
                    <DeviceThermostatIcon sx={{ color: blue[600], fontSize: 30}} /> C.W.U.
                  </Typography>
                  <Slider
                      min={20}
                      max={85}
                      step={1}
                      marks={marks}
                      defaultValue={30}
                      valueLabelDisplay="auto"
                      aria-labelledby="input-slider"
                      sx={{color: blue[600]}}
                  />
                </Paper>
              </Grid>

              <Grid item xs={12} md={8} lg={4}>
                <Paper sx={{padding: 2, display: "flex", overflow: "auto", flexDirection: "column"}}>
                  <img src={homePeriscopeLogo} className="App-logo-periscope" alt="logo"/>
                </Paper>
              </Grid>

            </Grid>

          </Container>
        </main>
      </div>
);
}

export default App;
