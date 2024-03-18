from locust import HttpUser, task, between, SequentialTaskSet, TaskSet, constant
from locust.exception import StopUser


class QuickstartUser(SequentialTaskSet):

    def on_start(self):
        with self.client.post("/", {
            'emailOrUsername': 'ahmed_learner', 'password': 'pfDB3MNShF5Tq7m'
        }, headers={'Content-Type': 'text/html; charset=utf-8'}
                              # 'Content-Type': 'text/html; charset=utf-8',
                              # 'Connection': 'keep-alive'}
                , catch_response=True) as response:
            if response.status_code == 200:
                print("login Successful")
                response.success()
            else:
                print("login FAILED")
                response.failure("Failed to login" + str(response.status_code))
                raise StopUser()

    def on_stop(self):
        pass

    @task
    def enroll_user(self):
        self.client.get("/register?course_id=course-v1:openedx+test123+2014_T4&enrollment_action=enroll")

    @task
    def go_to_dashboard(self):
        self.client.get("/dashboard")

    @task
    def open_course(self):
        self.client.get("/course_modes/choose/course-v1:openedx+test123+2014_T4/")

    @task
    def start_course(self):
        self.client.get("/courses/course-v1:openedx+test123+2014_T4/jump_to/block-v1:openedx+test123+2014_T4+type@video+block@75df141313014099932f949406193152")


class NavigateCategory(HttpUser):
    host = "https://learn.sdaia.academy"
    wait_time = between(1, 2)
    tasks = [QuickstartUser]
