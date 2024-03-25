import homePeriscopeLogo from './home-periscope.png';
import './App.css';
import React from 'react';

import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Container from "@mui/material/Container";
import Paper from "@mui/material/Paper";
import HeatingTemperature from './features/temperature/HeatingTemperature';
import MixerTemperature from "./features/temperature/MixerTemperature";
import WaterHeaterTemperature from './features/temperature/WaterHeaterTemperature';


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
                <MixerTemperature />
                <WaterHeaterTemperature />
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
