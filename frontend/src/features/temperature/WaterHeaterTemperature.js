import {useDispatch, useSelector} from 'react-redux'
import TemperatureSlider from "../../components/TemperatureSlider";
import {blue} from "@mui/material/colors";
import {setWaterHeaterTemperature} from "./temepratureSlice";

const WaterHeaterTemperature = () => {
  const waterHeaterTemperature = useSelector((state) => state.rootReducers.temperature.waterHeaterTemperature)
  const loadingStatus = useSelector((state) => waterHeaterTemperature.current === undefined ? 'loading' : 'idle')

  const dispatch = useDispatch()

  if (loadingStatus === 'loading') {
    return (
      <div className="water-heating-temperature">
        <div className="loader" />
      </div>
    )
  }

  const onWaterHeaterTemperatureChange = async (event, newValue) => {
      try {
        await dispatch(setWaterHeaterTemperature(newValue))
      } catch (err) {
        console.error('Failed to save water heating temperature: ', err)
      } finally {
        console.info('Finally')
      }
  }

  return <TemperatureSlider
      key='waterHeatingTemperature'
      title={'Temperatura wody ciepłej (C.W.U.): '}
      minTemperature={waterHeaterTemperature.minTemperature}
      maxTemperature={waterHeaterTemperature.maxTemperature}
      targetTemperature={waterHeaterTemperature.targetTemperature}
      current={waterHeaterTemperature.current}
      color={blue[600]}
      onChangeCommitted={onWaterHeaterTemperatureChange}
  />
}

export default WaterHeaterTemperature
