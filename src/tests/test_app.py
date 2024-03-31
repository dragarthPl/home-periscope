import unittest
import asyncio
from fastapi.testclient import TestClient

from main.core.sample_container import sample_container
from main.home_periscope import HomePeriscope

client = TestClient(HomePeriscope.create_app(sample_container))
loop = asyncio.get_event_loop()


class TestApp(unittest.TestCase):

    def test_dashboard(self) -> None:
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"You need to enable JavaScript to run this app.", response.content)
