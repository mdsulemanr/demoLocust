from locust import HttpUser, between, SequentialTaskSet, task
from locust.exception import StopUser


class UserLogin(SequentialTaskSet):

    def get_base_header(self):
        base_header_without_token = {
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
            'Origin': 'https://apps.sdaia.academy',
            'Referer': 'https://apps.sdaia.academy',
            'Upgrade-Insecure-AutoQuote': '1'
            # 'Content-Type': 'application/x-www-form-urlencoded',
            # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
        }
        return base_header_without_token

    def get_base_header_with_token(self):
        base_header = self.get_base_header()

        with self.client.get("/api/user/v2/account/login_session/", catch_response=True) as response:  # https://learn.sdaia.academy/csrf/api/v1/token
            if response.status_code == 200:
                token = response.cookies['csrftoken']
                base_header['X-CSRFToken'] = token
        return base_header

    def on_start(self):
        base_header = self.get_base_header_with_token()
        data = {
            'email_or_username': 'loadtesting2', 'password': 'a1b2c3d4'
        }

        with self.client.post("/api/user/v2/account/login_session/", data, headers=base_header,
                              catch_response=True) as response:
            if response.status_code == 200:
                print("login successful")
                print(response.cookies)
                # print(response.cookies['edx-jwt-cookie-header-payload'])
                # print(response.cookies['edx-jwt-cookie-signature'])
                # print(response.cookies['edx-user-info'])
                # print(response.cookies['edxloggedin'])
                # print(response.cookies['sessionid'])
                # print(response.cookies['csrftoken'])

            else:
                print('login Failed with status code: ' + str(response.status_code))
                response.failure('login Failed with status code: ' + str(response.status_code))
                raise StopUser()

    @task
    def navigate_to_dashboard(self):
        with self.client.get("/dashboard", headers=self.get_base_header(),
                             catch_response=True) as response:
            print(response.text)
            if response.status_code == 200:
                if "Dashboard" in response.text:
                    response.success()
                else:
                    response.failure("Dashboard string not found" + str(response.status_code))


    def on_stop(self):
        # TODO: Logout user from server when load test ends
        pass


class MyUser(HttpUser):
    wait_time = between(3, 4)
    host = 'https://learn-stage.sdaia.academy'
    tasks = [UserLogin]
