from faker import Faker
from locust import HttpUser, between, task


class E2eTests(HttpUser):
    wait_time = between(0.5, 3)

    @task(10)
    def index(self):
        self.client.get("http://localhost:8000")

    @task(10)
    def submit_form(self):
        fake = Faker()
        self.client.post("http://localhost:8000", data={"url": fake.url()})

    @task(10)
    def short_url(self):
        url_hash = "88943cbd43bb688296fe77112152574a"
        self.client.get(f"http://localhost:8000/{url_hash}")
