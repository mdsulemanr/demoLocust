from locust import HttpUser, TaskSet, task, constant, SequentialTaskSet, between
from locust.exception import StopUser
import re
import os
import csv


class UserLoader:
    users = []
    file_path = os.getcwd() + "/AutoQuote/users.csv"

    @staticmethod
    def load_users():
        open_file = open(UserLoader.file_path)
        reader = csv.DictReader(open_file)
        for user_ele in reader:
            UserLoader.users.append(user_ele)

    @staticmethod
    def get_user():
        if len(UserLoader.users) < 1:
            UserLoader.load_users()
        user_obj = UserLoader.users.pop()
        return user_obj


class Login(SequentialTaskSet):

    def __init__(self, parent):
        super().__init__(parent)
        self.UserSessionFilter = ""
        self.JSESSIONID = ""
        self.ViewState = ""

    def set_cookie(self):
        resp = self.client.get("/InsuranceWebExtJS/index.jsf")
        if resp.status_code == 200:
            self.JSESSIONID = resp.cookies['JSESSIONID']
            #  j_id1:j_id2
            re1 = re.findall("j_id\d+:j_id\d+", resp.text)
            self.ViewState = re1[0]

    def on_start(self):

        self.set_cookie()  # get and store values of self.JSESSIONID & self.ViewState in init
        # user_obj = UserLoader.get_user()
        with self.client.post('/InsuranceWebExtJS/index.jsf', data={
            'login-form': 'login-form',
            'login-form:email': 'qamile1@gmail.com',
            'login-form:password': 'qamile',
            'login-form:login.x': '56',
            'login-form:login.y': '11',
            'javax.faces.ViewState': self.ViewState
        }, cookies={"JSESSIONID": self.JSESSIONID}, catch_response=True) as response:

            if response.status_code == 200 and "Logged in as" in response.text:
                print("login successful with " + 'qamile1@gmail.com')
                self.UserSessionFilter = response.cookies["UserSessionFilter.sessionId"]
                self.ViewState = re.findall("j_id\d+:j_id\d+", response.text)[0]
                response.success()
            else:
                response.failure("Failed to login, status code: " + str(response.status_code))
                raise StopUser

    @task
    def select_agent_lookup(self):
        with self.client.get("/InsuranceWebExtJS/agent_lookup.jsf",
                             cookies={"JSESSIONID": self.JSESSIONID,
                                      "UserSessionFilter.sessionId": self.UserSessionFilter
                                      }, catch_response=True) as response:
            if response.status_code == 200:
                if "Find an Insurance Co. Agent" not in response.text:
                    response.failure(
                        "Failed to navigate to Agent Lookup Page, status code: " + str(response.status_code))
                else:
                    if re.findall("j_id\d+:j_id\d+", response.text):
                        self.ViewState = re.findall("j_id\d+:j_id\d+", response.text)[0]
                        response.success()
                    else:
                        print("ViewState value not found")

    @task
    def enter_zip_code(self):
        with self.client.post("/InsuranceWebExtJS/agent_lookup.jsf", name="agent_lookup1", data={
            "show-all": "show-all",
            "show-all:search-all.x": "27",
            "show-all:search-all.y": "6",
            'javax.faces.ViewState': self.ViewState

        }, cookies={"JSESSIONID": self.JSESSIONID,
                    "UserSessionFilter.sessionId": self.UserSessionFilter
                    }, catch_response=True) as response:
            if response.status_code == 200:
                if "Here is the list of all available Agents." not in response.text:
                    response.failure("Failed to navigate to 'Insurance Agent Search Results' Page,"
                                     " status code: " + str(response.status_code))
                else:
                    if re.findall("j_id\d+:j_id\d+", response.text):
                        self.ViewState = re.findall("j_id\d+:j_id\d+", response.text)[0]
                        response.success()
                    else:
                        print("ViewState value not found")


class MyUser(HttpUser):
    host = 'https://demo.borland.com'
    wait_time = between(3, 5)
    tasks = [Login]
