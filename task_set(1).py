import random

from locust import TaskSet, constant, task, HttpUser


class GetStatus(TaskSet):

    @task
    def get_status(self):
        self.client.get("/200")
        print("200")

    @task
    def get_random_codes(self):
        all_codes = [418, 421, 422, 423, 424, 425, 426, 428, 429, 431, 451,
                     500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511]
        code = "/" + str(random.choice(all_codes))
        random_code = self.client.get(code)
        print("random code")


class MyUser(HttpUser):
    host = "https://http.cat/"
    wait_time = constant(1)
    tasks = [GetStatus]
