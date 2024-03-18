from locust import HttpUser, task, between, SequentialTaskSet, TaskSet, constant


class WordPress(TaskSet):

    #     @task(1)
    #     def home_page(self):
    #         with self.client.get("/", catch_response=True) as response:
    #             if response.status_code in [0, 200]:
    #                 response.success()
    #
    #     @task(3)  # الدورات
    #     def browse_courses(self):
    #         with self.client.get("/courses/", catch_response=True) as response:
    #             if response.status_code in [0, 200]:
    #                 response.success()
    #
    #     @task(2)  # course 1
    #     def view_course1(self):
    #         with self.client.get("/course/mqdm-fy-jwd-lbynt-wtrq-qysh-course-v1-sdaia-academy-cm048-2023-t1/", catch_response=True) as response:
    #             if response.status_code in [0, 200]:
    #                 response.success()
    #
    #     @task(2)  # course 2
    #     def view_course2(self):
    #         with self.client.get("/course/mqdm-fy-lsyrt-dhty-lqyd-course-v1-sdaia-academy-cm073-2023-t1/", catch_response=True) as response:
    #             if response.status_code in [0, 200]:
    #                 response.success()
    #
    #     @task(2)  # course 3
    #     def view_course3(self):
    #         with self.client.get("/course/mqdm-fy-ltyrt-bdwn-tyr-drones-course-v1-sdaia-academy-cm071-2023-t1/", catch_response=True) as response:
    #             if response.status_code in [0, 200]:
    #                 response.success()
    #
    #     @task(2)  # course 4
    #     def view_course4(self):
    #         with self.client.get("/course/mqdm-fy-lm-lbynt-course-v1-sdaia-academy-cm077-2023-t1/", catch_response=True) as response:
    #             if response.status_code in [0, 200]:
    #                 response.success()
    #
    #     @task(2)  # course 5
    #     def view_course5(self):
    #         with self.client.get("/course/nmdhj-llg-ltby-y-course-v1-sdaia-academy-cm064-2023-t1/", catch_response=True) as response:
    #             if response.status_code in [0, 200]:
    #                 response.success()
    #
    #     @task(2)  # course 6
    #     def view_course6(self):
    #         with self.client.get("/course/mqdm-fy-m-lj-llgt-ltby-y-course-v1-sdaia-academy-cm053-2023-t1/", catch_response=True) as response:
    #             if response.status_code in [0, 200]:
    #                 response.success()
    #
    #     @task(1)  # course 7
    #     def view_course7(self):
    #         with self.client.get("/course/mqdm-fy-thlyl-lbynt-course-v1-sdaia-academy-cm076-2023-t1/", catch_response=True) as response:
    #             if response.status_code in [0, 200]:
    #                 response.success()
    #
    #     @task(1)  # course 8
    #     def view_course8(self):
    #         with self.client.get("/course/mqdm-fy-qw-d-lbynt-course-v1-sdaia-academy-cm057-2023-t1/", catch_response=True) as response:
    #             if response.status_code in [0, 200]:
    #                 response.success()
    #
    #     @task(1)  # course 9
    #     def view_course9(self):
    #         with self.client.get("/course/mqdm-fy-m-lj-llg-l-rby-course-v1-sdaia-academy-cm079-2023-t1/", catch_response=True) as response:
    #             if response.status_code in [0, 200]:
    #                 response.success()
    #
    #     @task(1)  # course 10
    #     def view_course10(self):
    #         with self.client.get("/course/mqdm-fy-t-lm-lal-ml-course-v1-sdaia-academy-cm058-2023-t1/", catch_response=True) as response:
    #             if response.status_code in [0, 200]:
    #                 response.success()
    #
    #     @task(1)  # course 11
    #     def view_course11(self):
    #         with self.client.get("/course/mqdm-fy-tmthyl-lbynt-introduction-to-data-visualization-course-v1-sdaia-academy-cm021-2023-t0/", catch_response=True) as response:
    #             if response.status_code in [0, 200]:
    #                 response.success()
    #
    #     @task(1)  # course 12
    #     def view_course12(self):
    #         with self.client.get("/course/khlqyt-ldhk-lstn-y-ethics-of-artificial-intelligence-course-v1-sdaia-academy-cm020-2023-t0/", catch_response=True) as response:
    #             if response.status_code in [0, 200]:
    #                 response.success()
    #
    #
    # class NavigateCategory(HttpUser):
    #     host = "https://courses.tndy.academy"
    #     wait_time = between(50, 60)
    #     tasks = [WordPress]
    @task(1)
    def home_page(self):
        with self.client.get("/", catch_response=True) as response:
            if response.status_code == 200:
                if "MAIN وجهتك نحو المستقبل" in response.text:
                    response.success()

    @task(3)  # الدورات
    def browse_courses(self):
        self.client.get("/courses/")

    @task(2)  # course 1
    def view_course1(self):
        self.client.get("/course/mqdm-fy-jwd-lbynt-wtrq-qysh-course-v1-sdaia-academy-cm048-2023-t1/")

    @task(2)  # course 2
    def view_course2(self):
        self.client.get("/course/mqdm-fy-lsyrt-dhty-lqyd-course-v1-sdaia-academy-cm073-2023-t1/")

    @task(2)  # course 3
    def view_course3(self):
        self.client.get("/course/mqdm-fy-ltyrt-bdwn-tyr-drones-course-v1-sdaia-academy-cm071-2023-t1/")

    @task(2)  # course 4
    def view_course4(self):
        self.client.get("/course/mqdm-fy-lm-lbynt-course-v1-sdaia-academy-cm077-2023-t1/")

    @task(2)  # course 5
    def view_course5(self):
        self.client.get("/course/nmdhj-llg-ltby-y-course-v1-sdaia-academy-cm064-2023-t1/")

    @task(2)  # course 6
    def view_course6(self):
        self.client.get("/course/mqdm-fy-m-lj-llgt-ltby-y-course-v1-sdaia-academy-cm053-2023-t1/")

    @task(1)  # course 7
    def view_course7(self):
        self.client.get("/course/mqdm-fy-thlyl-lbynt-course-v1-sdaia-academy-cm076-2023-t1/")

    @task(1)  # course 8
    def view_course8(self):
        self.client.get("/course/mqdm-fy-qw-d-lbynt-course-v1-sdaia-academy-cm057-2023-t1/")

    @task(1)  # course 9
    def view_course9(self):
        self.client.get("/course/mqdm-fy-m-lj-llg-l-rby-course-v1-sdaia-academy-cm079-2023-t1/")

    @task(1)  # course 10
    def view_course10(self):
        self.client.get("/course/mqdm-fy-t-lm-lal-ml-course-v1-sdaia-academy-cm058-2023-t1/")

    @task(1)  # course 11
    def view_course11(self):
        self.client.get(
            "/course/mqdm-fy-tmthyl-lbynt-introduction-to-data-visualization-course-v1-sdaia-academy-cm021-2023-t0/")

    @task(1)  # course 12
    def view_course12(self):
        self.client.get(
            "/course/khlqyt-ldhk-lstn-y-ethics-of-artificial-intelligence-course-v1-sdaia-academy-cm020-2023-t0/")


class NavigateCategory(HttpUser):
    host = "https://courses.tndy.academy"
    wait_time = between(50, 60)
    tasks = [WordPress]
