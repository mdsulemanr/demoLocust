from locust import HttpUser, task, constant, SequentialTaskSet, FastHttpUser


class PlaceOrder(SequentialTaskSet):

    @task
    def get_response(self):
        with self.client.get("/", catch_response=True) as response:
            if response.status_code == 200:
                print(response.cookies)


class MyUser(HttpUser):
    host = "https://courses.tndy.academy/"
    # wait_time = constant(1)
    tasks = [PlaceOrder]
