import unittest
from flask import render_template

from src.app import app


class TestLocationApi(unittest.TestCase):

    def setUp(self) -> None:
        self.client = app.test_client()

    def test_index_GET_wout_code_returns_main_page(self):
        response = self.client.get("/")
        assert response.status_code == 200

    def test_index_POST_returns_index_rendered_with_url(self):
        TEST_URL = "https://some.long.url/"
        response = self.client.post("/", data={"url": TEST_URL})
        assert response.status_code == 200
        assert TEST_URL in response.text
