import {useDispatch, useSelector} from 'react-redux'
import TemperatureSlider from "../../components/TemperatureSlider";
import {red} from "@mui/material/colors";
import {setHeatingTemperature} from "./temepratureSlice";

const HeatingTemperature = () => {
  const heatingTemperature = useSelector((state) => state.rootReducers.temperature.heatingTemperature)
  const loadingStatus = useSelector((state) => heatingTemperature.current === undefined ? 'loading' : 'idle')

  const dispatch = useDispatch()

  if (loadingStatus === 'loading') {
    return (
      <div className="heating-temperature">
        <div className="loader" />
      </div>
    )
  }
  const onHeatingTemperatureChange = async (event, newValue) => {
      try {
        await dispatch(setHeatingTemperature(newValue))
      } catch (err) {
        console.error('Failed to save heating temperature: ', err)
      } finally {
        console.info('Finally')
      }
  }

  return <TemperatureSlider
      key='heatingTemperature'
      title={'Temperatura kotła: '}
      minTemperature={heatingTemperature.minTemperature}
      maxTemperature={heatingTemperature.maxTemperature}
      targetTemperature={heatingTemperature.targetTemperature}
      current={heatingTemperature.current}
      color={red[600]}
      onChangeCommitted={onHeatingTemperatureChange}
  />
}

export default HeatingTemperature
