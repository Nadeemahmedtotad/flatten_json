from locust import HttpUser, task, between

class FastAPIUser(HttpUser):
    wait_time = between(1, 3)

    @task(2)
    def login(self):
        self.client.post(
            "/login",
            json={
                "username": "nadeem",
                "password": "password"
            }
        )

    @task(3)
    def flatten_json(self):
        payload = {
            "name": {
                "fn": "Nadeem",
                "ln": "Totad"
            },
            "age": 25,
            "address": {
                "permanent": {
                    "line1": "abc",
                    "line2": "xyz"
                }
            }
        }

        self.client.post(
            "/flatten",
            json=payload,
            headers={
                "Authorization": "Bearer dummy-token"
            }
        )
