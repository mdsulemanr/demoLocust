from locust import HttpUser, TaskSet, task, constant
from locust.exception import StopUser


class Login(TaskSet):

    def __init__(self, parent: "User"):
        super().__init__(parent)
        self.__gpi = None
        self.__gads = None
        self.cto_bundle = None
        self.panoramaId_expiry = None
        self._cc_id = None
        self._gid = None
        self._ga = None
        self.PHPSESSID = None
        self._pbjs_userid_consent_data = None
        self._sharedid = None

    # def base_header(self):
    #     base_header = {
    #         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #         'Content-Type': 'application/x-www-form-urlencoded',
    #         'Sec-Ch-Ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    #         'Sec-Ch-Ua-Mobile': '?0',
    #         'Referer': 'https://demo.guru99.com/test/newtours/index.php',
    #         'Origin': 'https://demo.guru99.com',
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

    def get_cookie(self):
        with self.client.get("/test/newtours/index.php", catch_response=True) as response:
            if response.status_code == 200:
                print(response.cookies)
                self.PHPSESSID = response.cookies['PHPSESSID']

    def on_start(self):

        # base_header = self.base_header()
        self.get_cookie()
        print(self.PHPSESSID)
        with self.client.post('/test/newtours/index.php', data={
            'action': 'process',
            'userName': 'test01_load',
            'password': 'test01_load',
            'submit': 'Submit'
        }, cookies={"PHPSESSID": self.PHPSESSID}, catch_response=True) as response:
            if response.status_code != 200 or "Enter your userName and password correct" in response.text:
                response.failure("Failed to login, status code: " + str(response.status_code))
                raise StopUser
            else:
                if "Welcome: Mercury Tours" in response.text:
                    print("login successful")
                    print(response.cookies)
                    # self._pbjs_userid_consent_data = response.cookies["_pbjs_userid_consent_data"]
                    # self._sharedid = response.cookies["_sharedid"]
                    # self._ga = response.cookies["_ga"]
                    # self._gid = response.cookies["_gid"]
                    # self._cc_id = response.cookies["_cc_id"]
                    # self.panoramaId_expiry = response.cookies["panoramaId_expiry"]
                    # self.cto_bundle = response.cookies["cto_bundle"]
                    # self.__gads = response.cookies["__gads"]
                    # self.__gpi = response.cookies["__gpi"]
                    response.success()

    @task
    def go_to_home(self):
        with self.client.get("/test/newtours/index.php",
                             cookies={"PHPSESSID": self.PHPSESSID
                                 #      ,"_sharedid": self._sharedid,
                                 #      "_ga": self._ga,
                                 # "_gid": self._gid,
                                 # "_cc_id": self._cc_id,
                                 # "panoramaId_expiry": self.panoramaId_expiry,
                                 # "cto_bundle": self.cto_bundle,
                                 # "__gads": self.__gads,
                                 # "__gpi": self.__gpi,
                                      }, catch_response=True) as response:
            if response.status_code == 200:
                response.success()


class MyUser(HttpUser):
    host = 'https://demo.guru99.com'
    wait_time = constant(1)
    tasks = [Login]
