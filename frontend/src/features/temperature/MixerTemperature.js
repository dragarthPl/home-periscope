import {useDispatch, useSelector} from 'react-redux'
import TemperatureSlider from "../../components/TemperatureSlider";
import {orange} from "@mui/material/colors";
import {setMixerTemperature} from "./temepratureSlice";

const MixerTemperature = () => {
  const mixerTemperature = useSelector((state) => state.rootReducers.temperature.mixerTemperature)
  const loadingStatus = useSelector((state) => mixerTemperature.current === undefined ? 'loading' : 'idle')

  const dispatch = useDispatch()

  if (loadingStatus === 'loading') {
    return (
      <div className="mixer-temperature">
        <div className="loader" />
      </div>
    )
  }
  const onMixerTemperatureChange = async (event, newValue) => {
      try {
        await dispatch(setMixerTemperature(newValue))
      } catch (err) {
        console.error('Failed to save mixer temperature: ', err)
      } finally {
        console.info('Finally')
      }
  }

  return <TemperatureSlider
      key='mixerTemperature'
      title={'Temperatura mieszacza: '}
      minTemperature={mixerTemperature.minTemperature}
      maxTemperature={mixerTemperature.maxTemperature}
      targetTemperature={mixerTemperature.targetTemperature}
      current={mixerTemperature.current}
      color={orange[600]}
      onChangeCommitted={onMixerTemperatureChange}
  />
}

export default MixerTemperature
