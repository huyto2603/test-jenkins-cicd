from fastapi.testclient import TestClient
import unittest

from notify_server import app


class test(unittest.TestCase):
    client = TestClient(app)

    def test(self):
        response = self.client.post(
            "/sendmsteams/ftg/expire/",
            json={
                "ip": "1.1.1.1",
                "subnet": "255.255.255.255",
                "host": "Foo Bar",
                "group": "The Foo Barters",
            },
        )
        assert response.status_code == 200
