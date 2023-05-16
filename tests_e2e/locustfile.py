import random

from faker import Faker
from locust import HttpUser, between, task

fake = Faker()
Faker.seed(0)

TEST_URL = "http://localhost:8000/"  # "http://52.70.103.16/"


class E2eTests(HttpUser):
    wait_time = between(0.5, 3)

    def __init__(self, *args, **kwargs):
        self.url_hashes = []
        super().__init__(*args, **kwargs)

    @task(10)
    def index(self):
        self.client.get(TEST_URL)

    @task(10)
    def submit_form(self):
        response = self.client.post(TEST_URL, json={"url": fake.url()})
        self.url_hashes.append(response.json()["url_hash"])

    @task(10)
    def short_url(self):
        if not self.url_hashes:
            return

        url_hash = random.choice(self.url_hashes)
        with self.client.get(f"{TEST_URL}{url_hash}", catch_response=True) as response:
            response.success()
