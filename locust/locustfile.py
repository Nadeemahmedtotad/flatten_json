from locust import HttpUser, task, between

# class FastAPIUser(HttpUser):
#     wait_time = between(1, 3)

#     @task(2)
#     def login(self):
#         self.client.post(
#             "/login",
#             json={
#                 "username": "nadeem",
#                 "password": "password"
#             }
#         )

#     @task(3)
#     def flatten_json(self):
#         payload = {
#             "name": {
#                 "fn": "Nadeem",
#                 "ln": "Totad"
#             },
#             "age": 25,
#             "address": {
#                 "permanent": {
#                     "line1": "abc",
#                     "line2": "xyz"
#                 }
#             }
#         }

#         self.client.post(
#             "/flatten",
#             json=payload,
#             headers={
#                 "Authorization": "Bearer dummy-token"
#             }
#         )

from locust import HttpUser, task, between


class FastAPIUser(HttpUser):
    """
    Simulates realistic traffic:
    - Successful login
    - Successful flatten requests (200)
    - Unauthorized flatten requests (401 / 403 -> 4xx)
    - Bad payload flatten requests (400 / 422 -> 4xx)
    - Forced server errors (500 -> 5xx)
    """

    wait_time = between(1, 3)

    # -------- NORMAL TRAFFIC --------

    @task(3)
    def login(self):
        """Valid login request (200)"""
        self.client.post(
            "/login",
            json={
                "username": "nadeem",
                "password": "password"
            }
        )

    @task(4)
    def flatten_valid(self):
        """Valid flatten request (200)"""
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

    # -------- 4xx ERROR SCENARIOS --------

    @task(1)
    def flatten_unauthorized(self):
        """Missing auth header -> 401 / 403"""
        payload = {
            "test": {
                "a": 1
            }
        }

        self.client.post(
            "/flatten",
            json=payload
        )

    @task(1)
    def flatten_bad_request(self):
        """Invalid JSON -> 400 / 422"""
        self.client.post(
            "/flatten",
            data="this-is-not-json",
            headers={
                "Authorization": "Bearer dummy-token"
            }
        )

    # -------- 5xx ERROR SCENARIO --------

    @task(1)
    def trigger_server_error(self):
        """
        Forced server error (500).
        Requires a debug endpoint in FastAPI:
        POST /debug/error
        """
        self.client.post("/debug/error")
