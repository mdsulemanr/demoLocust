from locust import HttpUser, TaskSet, task, constant
from locust.exception import StopUser
import re


class Login(TaskSet):

    def __init__(self, parent):
        super().__init__(parent)
        self.UserSessionFilter = ""
        self.JSESSIONID = ""
        self.ViewState = ""

    # def base_header(self):
    #     base_header = {
    #         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #         'Content-Type': 'application/x-www-form-urlencoded',
    #         'Sec-Ch-Ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    #         'Sec-Ch-Ua-Mobile': '?0',
    #         'Referer': 'https://demo.borland.com/InsuranceWebExtJS/index.jsf',
    #         'Origin': 'https://demo.borland.com',
    #         'Sec-Ch-Ua-Platform': "macOS",
    #         'Sec-Fetch-Dest': "document",
    #         'Sec-Fetch-Mode': 'navigate',
    #         'Sec-Fetch-Site': 'none',
    #         'Sec-Fetch-User': '?1',
    #         'Upgrade-Insecure-AutoQuote': '1',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    #     }
    #     return base_header
    #
    # def set_header_with_cookie(self, cookie):
    #     base_header = self.base_header()
    #     base_header['Cookie'] = cookie

    def set_cookie(self):
        resp = self.client.get("/InsuranceWebExtJS/index.jsf")
        if resp.status_code == 200:
            self.JSESSIONID = resp.cookies['JSESSIONID']
            #  j_id1:j_id2
            re1 = re.findall("j_id\d+:j_id\d+", resp.text)
            self.ViewState = re1[0]

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

    @task
    def select_autoquote(self):
        with self.client.get("/InsuranceWebExtJS/quote_auto.jsf",
                             cookies={"JSESSIONID": self.JSESSIONID,
                                      "UserSessionFilter.sessionId": self.UserSessionFilter
                                      }, catch_response=True) as response:
            if response.status_code == 200:
                if "Get Instant Auto Quote" not in response.text:
                    response.failure("Failed to navigate to Quote Page, status code: " + str(response.status_code))
                else:
                    response.success()

    # @task
    # def go_to_autoquote(self):
    #     with self.client.get("/InsuranceWebExtJS/quote_auto.jsf",
    #                          cookies={"JSESSIONID": self.JSESSIONID,
    #                                   "UserSessionFilter.sessionId": self.UserSessionFilter
    #                                   }, catch_response=True) as response:
    #         if response.status_code == 200:
    #             if "InsuranceWeb: Automobile Instant Quote" in response.text:
    #                 response.failure("Failed to navigate to Quote Page, status code: " + str(response.status_code))
    #                 response.success()


class MyUser(HttpUser):
    host = 'https://demo.borland.com'
    wait_time = constant(1)
    tasks = [Login]
