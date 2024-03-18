from locust import HttpUser, task, between, SequentialTaskSet, TaskSet, constant


class QuickstartUser(TaskSet):

    def __init__(self, parent: "User"):
        super().__init__(parent)
        self.csrftoken = None

    def on_start(self):
        result = self.client.get("/", headers={
            'Content-Type': 'text/html; charset=utf-8',
            'Connection': 'keep-alive'
        })
        # print(result.status_code)
        # print(result.cookies)
        self.csrftoken = result.cookies['csrftoken']

    @task
    def user_login(self):
        with self.client.post("/", data={
            'emailOrUsername': 'suleman.rafi+stage02@arbisoft.com', 'password': 'oneacademy01'
        }, headers={
            'Content-Type': 'text/html; charset=utf-8',
            'Connection': 'keep-alive',
            'Referer': 'https://apps-stage.sdaia.academy/',
            'csrftoken': self.csrftoken
        }, catch_response=True) as response:
            print(response.status_code)
            print(response.cookies)
            print(response.text)

    # @task(1)
    # def view_course(self):
    #     self.client.get("/course/staging-course-fahad-2-course-v1-arbisoft-cs111-2023-t4/")


class NavigateCategory(HttpUser):
    host = "https://learn-stage.sdaia.academy"
    wait_time = between(4, 5)
    tasks = [QuickstartUser]
