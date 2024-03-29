from main.temperature.mixer_temperature_repository import IMixerTemperatureRepository
from main.temperature.temperature import Temperature


class MixerTemperatureSampleRepository(IMixerTemperatureRepository):
    async def get_temperature(self) -> Temperature:
        return Temperature.from_dict({
            'current': 50,
            'max_temperature': 60,
            'min_temperature': 40,
        })