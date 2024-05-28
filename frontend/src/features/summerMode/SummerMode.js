import {useSelector} from "react-redux";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";
import WbSunnyIcon from '@mui/icons-material/WbSunny';
import AcUnitIcon from '@mui/icons-material/AcUnit';


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
        <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
            <strong>Tryb: </strong> {summerMode ? <WbSunnyIcon /> : <AcUnitIcon />}
        </Typography>
      </CardContent>
    )
}

export default SummerMode;