import asyncio
import unittest

from starlette.testclient import TestClient

from main.core.sample_container import sample_container
from main.home_periscope import HomePeriscope

client = TestClient(HomePeriscope.create_app(sample_container))
loop = asyncio.get_event_loop()


class TestFlameSize(unittest.TestCase):
    def test_flame_size(self) -> None:
        response = client.get("/api/flame_size")
        self.assertEqual(response.status_code, 200)
        self.assertEqual({'flame_size': '30%'}, response.json())