import unittest
import asyncio
from fastapi.testclient import TestClient

from main.core.sample_container import sample_container
from main.home_periscope import HomePeriscope

client = TestClient(HomePeriscope.create_app(sample_container))
loop = asyncio.get_event_loop()


class TestTemperature(unittest.TestCase):

    def test_heating_temperature(self) -> None:
        response = client.get("/api/heating_temperature")
        self.assertEqual(response.status_code, 200)
        self.assertEqual({
            'current': 30,
            'max_temperature': 60,
            'min_temperature': 20,
            'target_temperature': 40,
            'timestamp': 1234567891,
        }, response.json())

    def test_mixer_temperature(self) -> None:
        response = client.get("/api/mixer_temperature")
        self.assertEqual(response.status_code, 200)
        self.assertEqual({
            'current': 50,
            'max_temperature': 60,
            'min_temperature': 40,
            'target_temperature': 40,
            'timestamp': 1234567892,
        }, response.json())

    def test_water_heater_temperature(self) -> None:
        response = client.get("/api/water_heater_temperature")
        self.assertEqual(response.status_code, 200)
        self.assertEqual({
            'current': 56,
            'max_temperature': 60,
            'min_temperature': 40,
            'target_temperature': 50,
            'timestamp': 1234567893,
        }, response.json())