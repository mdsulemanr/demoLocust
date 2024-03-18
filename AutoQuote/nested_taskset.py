from locust import HttpUser, TaskSet, task, constant, SequentialTaskSet
from locust.exception import StopUser
import re


class UserBehavior(TaskSet):

    def __init__(self, parent):
        super().__init__(parent)
        self.UserSessionFilter = ""
        self.JSESSIONID = ""
        self.ViewState = ""

    def base_header(self):
        base_header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Sec-Ch-Ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Referer': 'https://demo.borland.com/InsuranceWebExtJS/index.jsf',
            'Origin': 'https://demo.borland.com',
            'Sec-Ch-Ua-Platform': "macOS",
            'Sec-Fetch-Dest': "document",
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-AutoQuote': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }
        return base_header['Upgrade-Insecure-AutoQuote']

    #
    # def set_header_with_cookie(self, cookie):
    #     base_header = self.base_header()
    #     base_header['Cookie'] = cookie

    def set_cookie(self):
        resp = self.client.get("/InsuranceWebExtJS/index.jsf")
        if resp.status_code == 200:
            self.JSESSIONID = resp.cookies['JSESSIONID']
            #  j_id1:j_id2
            if re.findall("j_id\d+:j_id\d+", resp.text):
                re1 = re.findall("j_id\d+:j_id\d+", resp.text)
                self.ViewState = re1[0]
            else:
                print("set_cookie, value of ViewState not found in the response")

    def on_start(self):

        self.set_cookie()  # get and store values of self.JSESSIONID & self.ViewState in init
        with self.client.post('/InsuranceWebExtJS/index.jsf', data={
            'login-form': 'login-form',
            'login-form:email': 'john.smith@gmail.com',
            'login-form:password': 'john',
            'login-form:login.x': '56',
            'login-form:login.y': '11',
            'javax.faces.ViewState': self.ViewState
        }, cookies={"JSESSIONID": self.JSESSIONID}, catch_response=True) as response:

            if response.status_code == 200 and "Logged in as" in response.text:
                print("login successful")
                self.UserSessionFilter = response.cookies["UserSessionFilter.sessionId"]
                self.ViewState = re.findall("j_id\d+:j_id\d+", response.text)[0]
                response.success()
            else:
                response.failure("Failed to login, status code: " + str(response.status_code))
                raise StopUser

    @task(2)
    class AutoQuote(SequentialTaskSet):

        @task
        def select_autoquote(self):
            with self.client.get("/InsuranceWebExtJS/quote_auto.jsf",
                                 cookies={"JSESSIONID": self.parent.JSESSIONID,
                                          "UserSessionFilter.sessionId": self.parent.UserSessionFilter
                                          }, catch_response=True) as response:
                if response.status_code == 200:
                    if "Get Instant Auto Quote" not in response.text:
                        response.failure("Failed to navigate to Quote Page, status code: " + str(response.status_code))
                    else:
                        self.parent.ViewState = re.findall("j_id\d+:j_id\d+", response.text)[0]
                        response.success()

        @task
        def enter_zip_code(self):
            with self.client.post("/InsuranceWebExtJS/quote_auto.jsf", name="quoate_auto1", data={
                "autoquote": "autoquote",
                "autoquote:zipcode": "110001",
                "autoquote:e-mail": "john.smith@gmail.com",
                "autoquote:vehicle": "car",
                "autoquote:next.x": "35",
                "autoquote:next.y": "6",
                'javax.faces.ViewState': self.parent.ViewState

            }, cookies={"JSESSIONID": self.parent.JSESSIONID,
                        "UserSessionFilter.sessionId": self.parent.UserSessionFilter
                        }, catch_response=True) as response:
                if response.status_code == 200:
                    if "You're almost done!" not in response.text:
                        response.failure("Failed to navigate to 'Instant Auto Quote - Continued' Page,"
                                         " status code: " + str(response.status_code))
                    else:
                        self.parent.ViewState = re.findall("j_id\d+:j_id\d+", response.text)[0]
                        response.success()

        @task
        def enter_age(self):
            with self.client.post("/InsuranceWebExtJS/quote_auto.jsf", name="quoate_auto2", data={
                "autoquote": "autoquote",
                "autoquote:age": "40",
                "autoquote:gender": "Male",
                "autoquote:type": "Excellent",
                "autoquote:next.x": "24",
                "autoquote:next.y": "1",
                'javax.faces.ViewState': self.parent.ViewState

            }, cookies={"JSESSIONID": self.parent.JSESSIONID,
                        "UserSessionFilter.sessionId": self.parent.UserSessionFilter
                        }, catch_response=True) as response:
                if response.status_code == 200:
                    if "Last Screen!" not in response.text:
                        response.failure(
                            "Failed to navigate to 'Last Screen! Give us some information about your automobile.' Page,"
                            " status code: " + str(response.status_code))
                    else:
                        self.parent.ViewState = re.findall("j_id\d+:j_id\d+", response.text)[0]
                        response.success()

        @task
        def get_full_quote(self):
            with self.client.post("/InsuranceWebExtJS/quote_auto3.jsf", name="quoate_auto3", data={
                "autoquote": "autoquote",
                "autoquote:year": "2018",
                "makeCombo": "Buick",
                "autoquote:make": "Buick",
                "modelCombo": "Century",
                "autoquote:model": "Century",
                "autoquote:finInfo": "Finance",
                "autoquote:next.x": "59",
                "autoquote:next.y": "12",
                'javax.faces.ViewState': self.parent.ViewState

            }, cookies={"JSESSIONID": self.parent.JSESSIONID,
                        "UserSessionFilter.sessionId": self.parent.UserSessionFilter
                        }, catch_response=True) as response:
                if response.status_code == 200:
                    if "Your Instant Quote is" not in response.text:
                        response.failure("Failed to navigate to 'Your Instant Quote is' Page,"
                                         " status code: " + str(response.status_code))
                    else:
                        self.parent.ViewState = re.findall("j_id\d+:j_id\d+", response.text)[0]
                        response.success()

        @task
        def exit_task(self):
            self.interrupt()

    @task(1)
    class AgentLookUp(SequentialTaskSet):

        @task
        def select_agent_lookup(self):
            with self.client.get("/InsuranceWebExtJS/agent_lookup.jsf",
                                 cookies={"JSESSIONID": self.parent.JSESSIONID,
                                          "UserSessionFilter.sessionId": self.parent.UserSessionFilter
                                          }, catch_response=True) as response:
                if response.status_code == 200:
                    if "Find an Insurance Co. Agent" not in response.text:
                        response.failure(
                            "Failed to navigate to Agent Lookup Page, status code: " + str(response.status_code))
                    else:
                        if re.findall("j_id\d+:j_id\d+", response.text):
                            self.parent.ViewState = re.findall("j_id\d+:j_id\d+", response.text)[0]
                            response.success()
                        else:
                            print("ViewState value not found")

        @task
        def search_agents(self):
            with self.client.post("/InsuranceWebExtJS/agent_lookup.jsf", name="agent_lookup1", data={
                "show-all": "show-all",
                "show-all:search-all.x": "27",
                "show-all:search-all.y": "6",
                'javax.faces.ViewState': self.parent.ViewState

            }, cookies={"JSESSIONID": self.parent.JSESSIONID,
                        "UserSessionFilter.sessionId": self.parent.UserSessionFilter
                        }, catch_response=True) as response:
                if response.status_code == 200:
                    if "Here is the list of all available Agents." not in response.text:
                        response.failure("Failed to navigate to 'Insurance Agent Search Results' Page,"
                                         " status code: " + str(response.status_code))
                    else:
                        if re.findall("j_id\d+:j_id\d+", response.text):
                            self.parent.ViewState = re.findall("j_id\d+:j_id\d+", response.text)[0]
                            response.success()
                        else:
                            print("ViewState value not found")

        @task
        def exit_task(self):
            self.interrupt()


class MyUser(HttpUser):
    # host = 'https://demo.borland.com'
    wait_time = constant(1)
    tasks = [UserBehavior]
