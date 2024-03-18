import random

from locust import HttpUser, between, SequentialTaskSet, task
from locust.exception import StopUser
import re


class UserLogin(SequentialTaskSet):
    csrftoken = ""

    def get_base_header(self):
        base_header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Sec-Ch-Ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"macOS"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            # 'X-CSRFToken': token,
            'Origin': 'https://apps.tndy.academy',
            'Referer': 'https://apps.tndy.academy/',
            'Upgrade-Insecure-AutoQuote': '1'
            # 'Content-Type': 'application/x-www-form-urlencoded',
            # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
        }
        return base_header

    def get_base_header_with_token(self):
        base_header = self.get_base_header()
        base_header['X-Csrftoken'] = self.csrftoken
        return base_header

    def set_csrf_token_before_login(self):
        resp = self.client.get("/api/user/v2/account/login_session/")  # https://learn.sdaia.academy/csrf/api/v1/token
        if resp.status_code == 200 and resp.cookies['csrftoken']:
            # print(resp.cookies['csrftoken'])
            self.csrftoken = resp.cookies['csrftoken']

    def on_start(self):
        self.set_csrf_token_before_login()
        headers = self.get_base_header_with_token()

        data = {
            'email_or_username': 'test1_learner', 'password': 'pfDB3MNShF5Tq7m'
            # ,'next': '/dashboard'
        }

        with self.client.post("/api/user/v2/account/login_session/", data, headers=headers,
                              catch_response=True) as response:
            if response.status_code == 200 and '"success": true' in response.text:
                self.csrftoken = response.cookies['csrftoken']
                print("login successful with " + "test1_learner")
                # print(response.cookies)
                # print(response.cookies['edx-jwt-cookie-header-payload'])
                # print(response.cookies['edx-jwt-cookie-signature'])
                # print(response.cookies['edx-user-info'])
                # print(response.cookies['edxloggedin'])
                # print(response.cookies['sessionid'])
                # print(response.cookies['csrftoken'])
                # re.findall("Email or password is incorrect.",response.text)
            else:
                response.failure('login Failed with status code: ' + str(response.status_code))
                print('login Failed with status code: ' + str(response.status_code))
                raise StopUser()

    @task
    def navigate_to_dashboard(self):
        with self.client.get("/dashboard",
                             catch_response=True) as response:
            if response.status_code == 200:
                # print(response.text)
                if "Dashboard" in response.text:
                    response.success()
                else:
                    response.failure("Dashboard string not found" + str(response.status_code))

    @task  # Enroll api course 1 [هندسة البيانات]
    def Enroll_course1(self):
        with self.client.get(
                "/register?course_id=course-v1:University+CN32+CR45&enrollment_action=enroll",
                data={"course_id": "course-v1:University+CN32+CR45", "enrollment_action": "enroll"},
                headers=self.get_base_header_with_token(), catch_response=True) as response:
            # print(response.text)
            if response.status_code == 200:
                # if response.cookies:
                if "Dashboard" or "Please Wait" in response.text:
                    response.success()
                else:
                    response.failure("Failed to navigate to Enroll user, Status Code: " +
                                     str(response.status_code))
    #
    # @task  # Enroll api course 1 [هندسة البيانات]
    # def Enroll_course1_baskets(self):
    #     with self.client.post(
    #             "/api/commerce/v0/baskets/", data={"course_id": "course-v1:SDAIA.ACADEMY+CM024+2023_T1"},
    #             headers=self.get_base_header_with_token(), catch_response=True) as response:
    #         if response.status_code in [200, 409]:
    #             # if response.cookies:
    #             if "Dashboard" or "Please Wait" in response.text:
    #                 response.success()
    #             else:
    #                 response.failure("Failed to navigate to Enroll user, Status Code: " +
    #                                  str(response.status_code))
    #
    # @task  # Un-enroll popup course 1 [هندسة البيانات]
    # def unenroll_course1(self):
    #     with self.client.get(
    #             "/course_run/course-v1:SDAIA.ACADEMY+CM024+2023_T1/refund_status",
    #             headers=self.get_base_header_with_token(), catch_response=True) as response:
    #         if response.status_code == 200:
    #             # if response.cookies:
    #             if "course_refundable_status" in response.text:
    #                 response.success()
    #             else:
    #                 response.failure("Failed to open un-enroll popup, Status Code: " +
    #                                  str(response.status_code), LogType.INFO)
    #
    # @task  # Un-enroll api course 1 [هندسة البيانات]
    # def unenroll_course1_baskets(self):
    #     with self.client.post(
    #             "/change_enrollment", data={"course_id": "course-v1:SDAIA.ACADEMY+CM024+2023_T1",
    #                                         "enrollment_action": "unenroll"},
    #             headers=self.get_base_header_with_token(), catch_response=True) as response:
    #         if response.status_code == 200:
    #             print(response.text)
    #             # if response.cookies:
    #             # if "Dashboard" or "Please Wait" in response.text:
    #             response.success()
    #
    # @task
    # def navigate_to_programs(self):
    #     with self.client.get("/dashboard/programs/",
    #                          catch_response=True) as response:
    #         if response.status_code == 200:
    #             if "Programs | SDAIA" in response.text:
    #                 # print(response.cookies['csrftoken'])
    #                 # self.csrftoken = response.cookies['csrftoken']
    #                 response.success()
    #             else:
    #                 response.failure("Dashboard string not found" + str(response.status_code))
    #
    # @task  # view course1 of program 2 [Internal Demo 1]
    # def view_course1_program2(self):
    #     with self.client.get(
    #             "https://apps.tndy.academy/learning/course/course-v1:Arbisoft+AR-201+2023_AR/home",
    #             catch_response=True) as response:
    #         if response.status_code == 200:
    #             if "Course" in response.text:
    #                 response.success()
    #             else:
    #                 response.failure("String 'Course' not found, "
    #                                  "url: /course_modes/choose/course-v1:Arbisoft+AR-201+2023_AR"
    #                                  "Status Code: " +
    #                                  str(response.status_code))
    #
    # @task  # enroll course of program 2 [Internal Demo 1]
    # def enroll_course1_program2(self):
    #     with self.client.post(
    #             "/api/commerce/v0/baskets/", data={
    #                 "course_id": "course-v1:Arbisoft+AR-201+2023_AR", "optIn": False
    #             }
    #             # , headers={'X-Csrftoken': self.csrftoken, 'Referer': 'https://apps.tndy.academy/'}
    #             , headers=self.get_base_header_with_token()
    #             , catch_response=True) as response:
    #         # print("enroll_course1_program2" + response.text)
    #         if response.status_code in [200, 409]:
    #             response.success()
    #
    # @task  # start course1 of program 2 [Internal Demo 1]
    # def start_course1_program2(self):
    #     with self.client.post(
    #             "/event", data={
    #                 "event_type": "edx.course.home.resume_course.clicked",
    #                 "event": {"org_key": "Arbisoft", "courserun_key": "course-v1:Arbisoft+AR-201+2023_AR",
    #                           "event_type": "start",
    #                           "url": "https://learn.tndy.academy/courses/course-v1:Arbisoft+AR-201+2023_AR/jump_to/block-v1:Arbisoft+AR-201+2023_AR+type@problem+block@5e9af529a01645d7865e92546e68b841"},
    #                 "page": "https://apps.tndy.academy/learning/course/course-v1:Arbisoft+AR-201+2023_AR/home"
    #             },
    #             headers=self.get_base_header_with_token(),
    #             catch_response=True) as response:
    #         print(response.text)
    #         if response.status_code == 200:
    #             response.success()
    #
    # @task
    # def navigate_to_profile(self):
    #     all_learners = ["test1_learner", "test2_learner", "test3_learner", "test4_learner", "test5_learner",
    #                     "test6_learner", "test7_learner", "test8_learner", "test9_learner", "test10_learner"]
    #     profile = "https://apps.tndy.academy/profile/u/" + random.choice(all_learners)
    #     with self.client.get(profile, name="/profile",
    #                          catch_response=True) as response:
    #         if response.status_code == 200:
    #             if "Learner Profile" in response.text:  # Search for string "Learner Profile"
    #                 response.success()
    #             else:
    #                 response.failure("String 'Learner Profile' not found, Status Code: " +
    #                                  str(response.status_code))

    def on_stop(self):
        # TODO: Logout user from server when load test ends
        pass


class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = 'https://learn.tndy.academy'
    tasks = [UserLogin]
