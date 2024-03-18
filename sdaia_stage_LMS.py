from locust import HttpUser, task, between, SequentialTaskSet, TaskSet


class QuickstartUser(TaskSet):

    @task(2)
    def browse_courses(self):
        self.client.get("/")

    @task(1)
    def view_course(self):
        self.client.get("/course/staging-course-fahad-2-course-v1-arbisoft-cs111-2023-t4/")
    #
    # @task(1)
    # def view_course(self):
    #     self.client.get("/course/introduction-to-computers-course-v1-umt-cs234-1233/")


class NavigateCategory(HttpUser):
    host = "https://stage.sdaia.academy"
    wait_time = between(4, 5)
    tasks = [QuickstartUser]
