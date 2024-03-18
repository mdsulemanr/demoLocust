from locust import HttpUser, task, constant, SequentialTaskSet


class PlaceOrder(SequentialTaskSet):

    @task
    def get_response(self):
        result = self.client.post("/post")
        print(result)

    @task
    def post_data(self):
        data = {
    "comments": "testing purpose",
    "custemail": "testuser@example.com",
    "custname": "test user",
    "custtel": "923219876543",
    "delivery": "",
    "size": "small",
    "topping": "bacon"
        }
        with self.client.post("/post", data, catch_response=True) as response:
            if response.status_code != 200:
                response.failure(str(response.status_code))
            else:
                response.success()
                print(response.status_code)
                print(response.cookies)
                print(response.headers)


class MyUser(HttpUser):
    host = "https://httpbin.org"
    wait_time = constant(1)
    tasks = [PlaceOrder]
