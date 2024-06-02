import {useSelector} from "react-redux";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";
import WbSunnyIcon from '@mui/icons-material/WbSunny';
import AcUnitIcon from '@mui/icons-material/AcUnit';
import {yellow} from "@mui/material/colors";
import {blue} from "@mui/material/colors";


const SummerMode = () => {
    const summerMode = useSelector((state) => state.rootReducers.summerMode.summerMode)
    const loadingStatus = useSelector((state) => summerMode === undefined ? 'loading' : 'idle')

    if (loadingStatus === 'loading') {
        return (
          <div className="summer-size">
            <div className="loader" />
          </div>
        )
    }

    return (
      <CardContent>
        <Typography sx={{ fontSize: 14, alignContent: 'center', display: 'flex' }} color="text.secondary" gutterBottom>
            <strong>Tryb: </strong>&nbsp; {summerMode ? <WbSunnyIcon sx={{color: yellow[600]}} /> : <AcUnitIcon sx={{color: blue[900]}} />}
        </Typography>
      </CardContent>
    )
}

export default SummerMode;