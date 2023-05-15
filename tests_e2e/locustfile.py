import random

from faker import Faker
from locust import HttpUser, between, task

fake = Faker()
Faker.seed(0)


class E2eTests(HttpUser):
    wait_time = between(0.5, 3)

    def __init__(self, *args, **kwargs):
        self.url_hashes = []
        super().__init__(*args, **kwargs)

    @task(10)
    def index(self):
        self.client.get("http://localhost:8000/")

    @task(10)
    def submit_form(self):
        response = self.client.post("http://localhost:8000/", json={"url": fake.url()})
        self.url_hashes.append(response.json()["url_hash"])

    @task(10)
    def short_url(self):
        url_hash = random.choice(self.url_hashes) or "88943cbd43bb688296fe77112152574a"
        with self.client.get(
            f"http://localhost:8000/{url_hash}", catch_response=True
        ) as response:
            response.success()
