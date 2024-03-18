from locust import HttpUser, between, SequentialTaskSet, task
from locust.exception import StopUser


class SearchProducts(SequentialTaskSet):

    @task
    def get_base_header(self):
        resp = self.client.get("/", allow_redirects=False)
        print(resp.status_code)
        print(resp.cookies)


class MyUser(HttpUser):
    wait_time = between(2, 3)
    host = 'https://learn.tndy.academy'
    tasks = [SearchProducts]
