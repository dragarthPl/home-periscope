from main.temperature.temperature import Temperature
from main.temperature.water_heater_temperature_repository import IWaterHeaterTemperatureRepository


class WaterHeaterTemperatureSampleRepository(IWaterHeaterTemperatureRepository):
    async def get_temperature(self) -> Temperature:
        return Temperature.from_dict({
            'current': 56,
            'max_temperature': 60,
            'min_temperature': 40,
            'target_temperature': 50,
            'timestamp': 1234567893,
        })
