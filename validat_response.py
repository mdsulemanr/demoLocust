from locust import HttpUser, task, constant, SequentialTaskSet

class ValidatResponse(SequentialTaskSet):

    @task
    def get_response(self):
        result = self.client.get("/xml", name="XML")
        print(result)

    @task
    def get_json(self):
        expected_result = "Wake up to WonderWidgets!"

        with self.client.get("/json", catch_response=True, name="JSON") as response:
            result = True if expected_result in response.text else False
            print(self.get_json.__name__, result)
            response.success()  # Marking this as success

    @task
    def get_robots(self):
        expected_result = "*"
        result = "Fail"

        with self.client.get("/robots.txt", catch_response=True, name="Robots") as response:
            if expected_result in response.text:
                result = "Success"
                response.failure("Not a failure")
        print(self.get_robots.__name__, result)

    @task
    def get_failure(self):
        expected_result = 404
        with self.client.get("/status/404", catch_response=True, name="Status 404") as response:
            if response.status_code == expected_result:
                response.failure("Got 404")
            else:
                response.success()
        print(self.get_failure.__name__, )

class MyUser(HttpUser):
    host = "https://httpbin.org"
    wait_time = constant(1)
    tasks = [ValidatResponse]
