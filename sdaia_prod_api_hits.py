from locust import HttpUser, between, SequentialTaskSet, task, constant
from locust.exception import StopUser


class SdaiaAPIs(SequentialTaskSet):

    @task
    def get_csrf_token(self):
        with self.client.get("/authn/login", catch_response=True) as response:
            if response.status_code == 200:
                response.success()

    # @task
    # def login_session_api(self):
    #     with self.client.get("/api/user/v2/account/login_session/", catch_response=True) as response:
    #         if response.status_code == 200:
    #             if "Cookie" in response.text:
    #                 response.success()
    #             print("/api/user/v2/account/login_session/: " + response.cookies['csrftoken'])
    #             response.success()
    #
    # @task
    # def token_api(self):
    #     with self.client.get("/csrf/api/v1/token: ", catch_response=True) as response:
    #         if response.status_code == 200:
    #             print("/csrf/api/v1/token" + response.cookies['csrftoken'])
    #             response.success()
    #
    # @task
    # def get_base_header(self):
    #     with self.client.get("/register?course_id=course-v1:SDAIA.ACADEMY+CM056+2023_T1&enrollment_action=enroll", catch_response=True) as response:
    #         if response.status_code == 200:
    #             response.success()
    #


class MyUser(HttpUser):
    wait_time = constant(1)
    host = 'https://learn.tndy.academy'
    tasks = [SdaiaAPIs]
