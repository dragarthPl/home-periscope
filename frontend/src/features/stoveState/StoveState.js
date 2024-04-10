import CardContent from '@mui/material/CardContent';
import Typography from "@mui/material/Typography";
import {useSelector} from "react-redux";
import {setHeatingTemperature} from "../temperature/temepratureSlice";

const StoveState = () => {
    const stoveState = useSelector((state) => state.rootReducers.stoveState.stoveState)
    const loadingStatus = useSelector((state) => stoveState === undefined ? 'loading' : 'idle')

    if (loadingStatus === 'loading') {
        return (
          <div className="stove-state">
            <div className="loader" />
          </div>
        )
    }

    return (
        <CardContent>
          <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
              Stan pieca: {stoveState.stoveState}
          </Typography>
          {/*<Typography variant="h5" component="div">*/}
          {/*  be nev o lent*/}
          {/*</Typography>*/}
          {/*<Typography sx={{ mb: 1.5 }} color="text.secondary">*/}
          {/*  adjective*/}
          {/*</Typography>*/}
          {/*<Typography variant="body2">*/}
          {/*  well meaning and kindly.*/}
          {/*  <br />*/}
          {/*  {'"a benevolent smile"'}*/}
          {/*</Typography>*/}
        </CardContent>
    )
}

export default StoveState;