import CardContent from '@mui/material/CardContent';
import Typography from "@mui/material/Typography";
import {useSelector} from "react-redux";

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
              <strong>Stan pieca: </strong> {stoveState.stoveState}
          </Typography>
        </CardContent>
    )
}

export default StoveState;