from locust import HttpUser, between, constant, TaskSet, SequentialTaskSet, User, events, task


class UtilityHelper:

    @staticmethod
    def base_headers():
        base_header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9"
        }
        return base_header


class MainClass(TaskSet):

    def on_start(self):
        self.headers = UtilityHelper.base_headers()

    @task(3)
    def home_page(self):
        with self.client.get("/InsuranceWebExtJS/index.jsf", headers=self.headers,
                             catch_response=True) as response:
            if response.status_code == 200:
                response.success()

    @task(2)
    class WebUser(TaskSet):

        def on_start(self):
            # self.headers = UtilityHelper.base_headers()
            print("Web user activities started")

        @task(2)  # الدورات
        def browse_courses(self):
            with self.client.get("/InsuranceWebExtJS/quote_auto.jsf", headers=self.headers,
                                 catch_response=True) as response:
                if response.status_code == 200:
                    response.success()
                    print("task2")

        @task(2)  # course 1
        def view_course1(self):
            self.client.get(
                "/intl/en_pk/ads/?subid=ww-ww-et-g-awa-a-g_hpafoot1_1!o2&utm_source=google.com&utm_medium=referral&utm_campaign=google_hpafooter&fg=1")
            print("task3")

        @task(1)
        def exit_task_execution(self):
            print("interupt1")
            self.interrupt()

    @task(1)
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
    host = "https://demo.borland.com"
    wait_time = constant(1)
    tasks = [MainClass]
