
import { useSelector } from 'react-redux'
import TemperatureSlider from "../../components/TemperatureSlider";
import {red} from "@mui/material/colors";

const WaterHeaterTemperature = () => {
  const waterHeaterTemperature = useSelector((state) => state.rootReducers.temperature.waterHeaterTemperature)
  const loadingStatus = useSelector((state) => waterHeaterTemperature.current === undefined ? 'loading' : 'idle')

  if (loadingStatus === 'loading') {
    return (
      <div className="water-heating-temperature">
        <div className="loader" />
      </div>
    )
  }

  return <TemperatureSlider
      key='heatingTemperature'
      minTemperature={heatingTemperature.minTemperature}
      maxTemperature={heatingTemperature.maxTemperature}
      targetTemperature={heatingTemperature.targetTemperature}
      current={heatingTemperature.current}
      color={red[600]}
  />
}

export default WaterHeaterTemperature
