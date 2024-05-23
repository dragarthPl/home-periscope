import CardContent from '@mui/material/CardContent';
import Typography from "@mui/material/Typography";
import {useSelector} from "react-redux";

const FlameSize = () => {
    const flameSize = useSelector((state) => state.rootReducers.flameSize.flameSize)
    const loadingStatus = useSelector((state) => flameSize === undefined ? 'loading' : 'idle')

    if (loadingStatus === 'loading') {
        return (
          <div className="flame-size">
            <div className="loader" />
          </div>
        )
    }

    return (
      <CardContent>
        <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
            <strong>Wielkość płomienia: </strong> {flameSize}
        </Typography>
      </CardContent>
    )
}

export default FlameSize;