from locust import HttpUser, TaskSet, task, constant
from locust.exception import StopUser


class Login(TaskSet):

    def on_start(self):
        with self.client.post('/test/newtours/index.php', data={
            'action': 'process',
            'userName': 'admin',
            'password': 'admin',
            'submit': 'Submit'
        }, catch_response=True) as response:
            if response.status_code != 200 or "Enter your userName and password correct" in response.text:
                response.failure("Failed to login, status code: " + str(response.status_code))
                raise StopUser
            else:
                if "Welcome: Mercury Tours" in response.text:
                    print("login successful")
                    print(response.status_code)
                    print(response.cookies)
                    # print(response.text)
                    response.success()

    @task
    def go_to_home(self):
        with self.client.get("/test/newtours/index.php", catch_response=True) as response:
            if response.status_code == 200:
                print(response.status_code)
                print(response.cookies)
                response.success()


class MyUser(HttpUser):
    host = 'https://demo.guru99.com'
    wait_time = constant(1)
    tasks = [Login]
