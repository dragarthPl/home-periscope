import unittest
import asyncio
from fastapi.testclient import TestClient

from main.home_periscope import HomePeriscope

client = TestClient(HomePeriscope().create_app())
loop = asyncio.get_event_loop()


class TestApp(unittest.TestCase):

    def test_dashboard(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"You need to enable JavaScript to run this app.", response.content)
