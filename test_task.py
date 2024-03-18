from locust import between, task, TaskSet, HttpUser, User, constant, SequentialTaskSet, events


# class WebUser(SequentialTaskSet):
#
#     @task(3)
#     def task1(self):
#         print("task1")
#
#     @task(2)
#     def task2(self):
#         print("task2")
#
#     @task(1)
#     def task3(self):
#         print("task3")
#
#     @task
#     def exit_task_execution(self):
#         print("interupt1")
#         self.interrupt()
#
# class MobileUser(SequentialTaskSet):
#
#     @task(2)
#     def task4(self):
#         print("task4")
#
#     @task(1)
#     def task5(self):
#         print("task5")
#
#     @task
#     def exit_task_execution(self):
#         print("interupt2")
#         self.interrupt()
#
#
# class MyUser(User):
#     wait_time = between(1, 2)
#     tasks = {
#         WebUser: 5,
#         MobileUser: 1
#     }

@events.test_start.add_listener
def on_test_start(**kwargs):
    print("Connecting to DB")


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    print("Disconnecting to DB")


class WebUser(TaskSet):

    def on_start(self):
        print("Web user activities started")

    @task(1)
    def home_page(self):
        with self.client.get("/", catch_response=True) as response:
            if response.status_code == 200:
                print("task1")

    @task(2)  # الدورات
    def browse_courses(self):
        self.client.get("https://about.google/?utm_source=google-PK&utm_medium=referral&utm_campaign=hp-footer&fg=1")
        print("task2")

    @task(3)  # course 1
    def view_course1(self):
        self.client.get(
            "/intl/en_pk/ads/?subid=ww-ww-et-g-awa-a-g_hpafoot1_1!o2&utm_source=google.com&utm_medium=referral&utm_campaign=google_hpafooter&fg=1")
        print("task3")

    @task
    def exit_task_execution(self):
        print("interupt1")
        self.interrupt()


class MobileUser(TaskSet):

    def on_start(self):
        print("Mobile User tasks have been started")

    @task(1)
    def home_page(self):
        with self.client.get(
                "/services/?subid=ww-ww-et-g-awa-a-g_hpbfoot1_1!o2&utm_source=google.com&utm_medium=referral&utm_campaign=google_hpbfooter&fg=1",
                catch_response=True) as response:
            if response.status_code == 200:
                print("task4")

    @task(2)  # الدورات
    def browse_courses(self):
        self.client.get("/search/howsearchworks/?fg=1")
        print("task5")

    @task
    def exit_task_execution(self):
        print("interupt2")
        self.interrupt()


class NavigateCategory(HttpUser):
    host = "https://www.google.com"
    wait_time = between(1, 2)
    tasks = {
        WebUser: 4,
        MobileUser: 1
    }
