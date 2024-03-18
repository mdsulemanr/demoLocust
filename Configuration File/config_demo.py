from locust import HttpUser, between, task


class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = "https://httpbin.org/"

    def __int__(self, parent):
        super().__init__(self, parent)
        self.hostname = self.host

    @task
    def home_page(self):
        res = self.client.get("/", name=self.hostname)
        print(res.text)
