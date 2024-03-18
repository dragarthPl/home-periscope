
import { useSelector } from 'react-redux'
import TemperatureSlider from "../../components/TemperatureSlider";
import {red} from "@mui/material/colors";

const HeatingTemperature = () => {
  const heatingTemperature = useSelector((state) => state.rootReducers.temperature.heatingTemperature)
  const loadingStatus = useSelector((state) => heatingTemperature.current === undefined ? 'loading' : 'idle')

  if (loadingStatus === 'loading') {
    return (
      <div className="heating-temperature">
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

export default HeatingTemperature
