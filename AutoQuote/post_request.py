from locust import HttpUser, TaskSet, task, constant, SequentialTaskSet
from locust.exception import StopUser


class Login(SequentialTaskSet):

    @task
    def get_login(self):
        resp1 = self.client.get('/test/newtours/index.php'
        )
        print("get request successful")
        print(resp1.status_code)
        print(resp1.cookies)
        print(resp1.text)

    @task
    def post_login(self):
        resp2 = self.client.post('/test/newtours/index.php', data={
            'action': 'process',
            'userName': 'admin',
            'password': 'admin',
            'submit': 'Submit'
        })
        print("login successful")
        print(resp2.status_code)
        print(resp2.cookies)
        print(resp2.text)


class MyUser(HttpUser):
    host = 'https://demo.guru99.com'
    wait_time = constant(1)
    tasks = [Login]
