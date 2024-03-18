from locust import HttpUser, TaskSet, SequentialTaskSet, between, task
import random
import logging


class UtilityHelp:

    @staticmethod
    def choice_item(data_list):
        return random.choice(data_list)

    @staticmethod
    def select_uuid():
        all_uuid = ["anonymous", "rms3aac1-hrnnhtnf-8s1acwnq-o4wjub0f"]
        uuid = UtilityHelp.choice_item(all_uuid)
        return uuid

    @staticmethod
    def all_strings():
        all_strings = {
            "index_page": ["/", "LEARN<br>ON YOUR OWN SCHEDULE",
                           "Delay in Response for index page, url: '/', Status Code: ",
                           "Failed to load index page, url: '/', Status Code: "]
        }
        return all_strings


class Functions(HttpUser):
    abstract = True

    # @staticmethod
    def view_page(self, url, keyword, res_fail_text, code_fail_text):
        with self.client.get(url, catch_response=True) as response:
            if response.status_code == 200:
                if keyword in response.text:
                    response.success()
                else:
                    logging.info("{}".format(res_fail_text) + str(response.status_code))
            else:
                logging.error("{}".format(code_fail_text) + str(response.status_code))


class HomeLandingPage(SequentialTaskSet, Functions):
    def on_start(self):
        self.all_strings = UtilityHelp.all_strings()

    @task
    def index_page(self):
        self.view_page(
                       self.all_strings["index_page"][0],
                       self.all_strings["index_page"][1],
                       self.all_strings["index_page"][2],
                       self.all_strings["index_page"][3]
                       )

    # @task
    # def index_page(self):
    #     with self.client.get(self.all_strings["index_page"][0], catch_response=True) as response:
    #         if response.status_code == 200:
    #             if "".format(self.all_strings["index_page"][1]) in response.text:
    #                 response.success()
    #             else:
    #                 logging.info("Delayed in Response Text, index page url: '/', "
    #                              "Status Code: " + str(response.status_code))
    #         else:
    #             logging.error("Failed to load index page, "
    #                           "Status Code: " + str(response.status_code))
    #
    #
#     @task
#     def accept_notification(self):
#         with self.client.post("/wp-admin/admin-ajax.php", name="accept notifications", data={
#             "action": "borlabs_cookie_handler",
#             "type": "log",
#             "language": "en",
#             "cookieData[consents][essential][]": "borlabs-cookie",
#             # "cookieData[consents][external - media][]": "facebook",
#             # "cookieData[consents][external - media][]": "googlemaps",
#             # "cookieData[consents][external - media][]": "instagram",
#             # "cookieData[consents][external - media][]": "openstreetmap",
#             # "cookieData[consents][external - media][]": "twitter",
#             # "cookieData[consents][external - media][]": "vimeo",
#             # "cookieData[consents][external - media][]": "youtube",
#             "cookieData[domainPath]": "edlymultisitestage.arbisoft.com/",
#             # "cookieData[expires]": "Wed, 26 Jun 2024 07:01:46 GMT",
#             # "cookieData[uid]": "rms3aac1-hrnnhtnf-8s1acwnq-o4wjub0f",
#             "cookieData[uid]": UtilityHelp.select_uuid(),
#             "cookieData[version]": "1",
#             "essentialStatistic": "true"
#         },
#                               catch_response=True) as response:
#             if response.status_code == 200:
#                 if '{"success":true}' in response.text:
#                     response.success()
#                 else:
#                     logging.info("Failed to accept notification, Status Code: " +
#                                  str(response.status_code))
#             else:
#                 logging.error("Failed to load notification popup, "
#                               "Status Code: " + str(response.status_code))
#
#     @task
#     def exit_task(self):
#         self.interrupt()
#
#
# class HomePageNavigation(TaskSet):
#     @task
#     def contact_page(self):
#         with self.client.get("/contact-us/", catch_response=True) as response:
#             if response.status_code == 200:
#                 # print(response.text)
#                 if "Contact Us | arbisoft" in response.text:
#                     response.success()
#                 else:
#                     logging.info("Failed to find string 'Contact Us | arbisoft', Status Code: " +
#                                  str(response.status_code))
#             else:
#                 logging.error("Failed to load contact page, "
#                               "Status Code: " + str(response.status_code))
#
#     @task
#     def subscriptions_page(self):
#         with self.client.get("/subscriptions/", catch_response=True) as response:
#             if response.status_code == 200:
#                 # print(response.text)
#                 if "Subscriptions | arbisoft" in response.text:
#                     response.success()
#                 else:
#                     logging.info("Failed to find string 'Subscriptions | arbisoft' , Status Code: " +
#                                  str(response.status_code))
#             else:
#                 logging.error("Failed to load subscriptions page, "
#                               "Status Code: " + str(response.status_code))
#
#     @task
#     def instructors_page(self):
#         with self.client.get("/instructors/", catch_response=True) as response:
#             if response.status_code == 200:
#                 # print(response.text)
#                 if "Instructors | arbisoft" in response.text:
#                     response.success()
#                 else:
#                     logging.info("Failed to find string 'Instructors | arbisoft' , Status Code: " +
#                                  str(response.status_code))
#             else:
#                 logging.error("Failed to instructors index page, "
#                               "Status Code: " + str(response.status_code))
#
#     @task
#     def aboutus_page(self):
#         with self.client.get("/about-us/", catch_response=True) as response:
#             if response.status_code == 200:
#                 # print(response.text)
#                 if "About Us | arbisoft" in response.text:
#                     response.success()
#                 else:
#                     logging.info("Failed to find string 'About Us | arbisoft' , Status Code: " +
#                                  str(response.status_code))
#             else:
#                 logging.error("Failed to load about-us page, "
#                               "Status Code: " + str(response.status_code))
#
#     @task
#     def exit_task(self):
#         self.interrupt()
#
#
# class NavigateCourses(SequentialTaskSet):
#
#     @task
#     def courses_main_page(self):
#         with self.client.get("/courses/", catch_response=True) as response:
#             if response.status_code == 200:
#                 # print(response.text)
#                 if "Courses | arbisoft" in response.text:
#                     response.success()
#                 else:
#                     logging.info("Failed to find string 'Courses | arbisoft' , Status Code: " +
#                                  str(response.status_code))
#             else:
#                 logging.error("Failed to load courses main page, "
#                               "Status Code: " + str(response.status_code))
#
#     @task
#     def filter_course_by_category(self):
#         with self.client.post("/wp-admin/admin-ajax.php", name="filter course", data={
#             "search_term": "",
#             "course_categories": "1e40717f-5cd9-4b02-baa3-adebe12239df",
#             "orderby": "newly-published",
#             "nonce": "e19c93076a",
#             "action": "edly_fetch_course_cards",
#             "page": "1"
#         }, catch_response=True) as response:
#             if response.status_code == 200:
#                 # print(response.text)
#                 if "Suleman Test Course1.1" in response.text:
#                     response.success()
#                 else:
#                     logging.info("Failed to find course name 'Suleman Test Course1.1' , Status Code: " +
#                                  str(response.status_code))
#             else:
#                 logging.error("Failed to load filtered course page page, "
#                               "Status Code: " + str(response.status_code))
#
#     @task
#     def search_course_by_search_term(self):
#         with self.client.post("/wp-admin/admin-ajax.php", name="search course", data={
#             "search_term": "test",
#             # "course_categories": "1e40717f-5cd9-4b02-baa3-adebe12239df",
#             "orderby": "newly-published",
#             "nonce": "e19c93076a",
#             "action": "edly_fetch_course_cards",
#             "page": "1"
#         }, catch_response=True) as response:
#             if response.status_code == 200:
#                 # print(response.text)
#                 if "21st April 2021" in response.text:
#                     response.success()
#                 else:
#                     logging.info("Failed to search course with string 'test' , Status Code: " +
#                                  str(response.status_code))
#             else:
#                 logging.error("Failed to load search course result page, "
#                               "Status Code: " + str(response.status_code))
#
#     @task
#     def course_detail_page(self):
#         with self.client.get("/course/21st-april-2021-2", catch_response=True) as response:
#             if response.status_code == 200:
#                 if "21st April 2021 | arbisoft" in response.text:
#                     response.success()
#                 else:
#                     logging.info("Failed to find string '21st April 2021 | arbisoft' , Status Code: " +
#                                  str(response.status_code))
#             else:
#                 logging.error("Failed to load course detail page, "
#                               "Status Code: " + str(response.status_code))
#
#     @task
#     def exit_task(self):
#         self.interrupt()
#
#
# class NavigatePrograms(SequentialTaskSet):
#
#     @task
#     def programs_main_page(self):
#         with self.client.get("/programs/", catch_response=True) as response:
#             if response.status_code == 200:
#                 # print(response.text)
#                 if "Programs | arbisoft" in response.text:
#                     response.success()
#                 else:
#                     logging.info("Failed to find string 'Programs | arbisoft' , Status Code: " +
#                                  str(response.status_code))
#             else:
#                 logging.error("Failed to load programs main page, "
#                               "Status Code: " + str(response.status_code))
#
#     @task
#     def sort_programs(self):
#         with self.client.post("/wp-admin/admin-ajax.php", name="sort program", data={
#             # "search_term":
#             # "course_categories": "1e40717f-5cd9-4b02-baa3-adebe12239df",
#             "orderby": "alphabetical",
#             "nonce": "e19c93076a",
#             "action": "edly_fetch_course_cards",
#             "page": "1"
#         }, catch_response=True) as response:
#             if response.status_code == 200:
#                 # print(response.text)
#                 if "21st April 2021" in response.text:
#                     response.success()
#                 else:
#                     logging.info("Failed to sort program, Status Code: " +
#                                  str(response.status_code))
#             else:
#                 logging.error("Failed to load sort program result page, "
#                               "Status Code: " + str(response.status_code))
#
#     @task
#     def search_program_search_term(self):
#         with self.client.post("/wp-admin/admin-ajax.php", name="search program", data={
#             "search_term": "test",
#             # "course_categories": "1e40717f-5cd9-4b02-baa3-adebe12239df",
#             "orderby": "newly-published",
#             "nonce": "a43ef34729",
#             "action": "edly_fetch_programs_cards",
#             "page": "1"
#         }, catch_response=True) as response:
#             if response.status_code == 200:
#                 # print(response.text)
#                 if "testing program" in response.text:
#                     response.success()
#                 else:
#                     logging.info("Failed to search program with string 'test' , Status Code: " +
#                                  str(response.status_code))
#             else:
#                 logging.error("Failed to load search program result page, "
#                               "Status Code: " + str(response.status_code))
#
#     @task
#     def program_detail_page(self):
#         with self.client.get("/program/koa-stage-144-program/", catch_response=True) as response:
#             if response.status_code == 200:
#                 if "Pursue the Program" in response.text:
#                     response.success()
#                 else:
#                     logging.info("Failed to navigate program detail page, Status Code: " +
#                                  str(response.status_code))
#             else:
#                 logging.error("Failed to load program detail page, "
#                               "Status Code: " + str(response.status_code))
#
#     @task
#     def exit_task(self):
#         self.interrupt()


class StartUser(Functions):
    host = "https://edlymultisitestage.arbisoft.com"
    Functions.tasks = [HomeLandingPage]
    # tasks = {
    #     HomeLandingPage: 2,
    #     HomePageNavigation: 1,
    #     NavigateCourses: 4,
    #     NavigatePrograms: 3
    # }
    wait_time = between(1, 2)
