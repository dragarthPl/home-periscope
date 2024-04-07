from main.temperature.heating_temperature_repository import IHeatingTemperatureRepository
from main.temperature.temperature import Temperature


class HeatingTemperatureSampleRepository(IHeatingTemperatureRepository):
    async def get_temperature(self) -> Temperature:
        return Temperature.from_dict({
            'max_temperature': 60,
            'min_temperature': 20,
            'target_temperature': 40,
            'current': 30,
            'timestamp': 1234567891,
        })

    async def set_temperature(self, temperature: int) -> bool:
        return True
