import asyncio
import unittest

from starlette.testclient import TestClient

from main.core.sample_container import sample_container
from main.home_periscope import HomePeriscope

client = TestClient(HomePeriscope.create_app(sample_container))
loop = asyncio.get_event_loop()


class TestStoveState(unittest.TestCase):

    def test_heating_temperature(self) -> None:
        response = client.get("/api/stove_state")
        self.assertEqual(response.status_code, 200)
        self.assertEqual({'stove_state': 'Stabilizacja'}, response.json())