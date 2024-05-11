import requests


class NavigateCategory:
    def __init__(self):
        self.response_msg = "response successful"
        self.host = "https://learn.tndy.academy"
        self.session = requests.Session()

    def get_csrf_token(self):
        response = self.session.get("{}/login".format(self.host),
                                    allow_redirects=False)  # https://learn.tndy.academy/csrf/api/v1/token
        if response.status_code == 302 and response.cookies['csrftoken']:
            csrftoken = response.cookies['csrftoken']
            return csrftoken
            print(response.cookies['csrftoken'])
        else:
            print("Failed to retrieve csrf-token")

    def get_base_header(self, token):
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
            'X-Csrftoken': token,
            'Origin': 'https://apps.tndy.academy',
            'Referer': 'https://apps.tndy.academy/',
            'Upgrade-Insecure-AutoQuote': '1'
            # 'Content-Type': 'application/x-www-form-urlencoded',
            # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
        }
        return base_header

    def user_login(self, headers_with_token):
        payload = {
            'email_or_username': 'fatima.rafiq@arbisoft.com', 'password': '$fatima123456'
            # ,'next': '/dashboard'
        }

        with self.session.post("{}/api/user/v2/account/login_session/".format(self.host), data=payload,
                               headers=headers_with_token) as response:
            if response.status_code == 200 and '"success": true' in response.text:
                print(response.text)
                print("login successful with " + "test1_learner")
            else:
                print('login Failed with status code: ' + str(response.status_code))

    def navigate_to_dashboard(self):
        with self.session.get("{}/dashboard".format(self.host)) as response:
            if response.status_code == 200:
                if "Dashboard" in response.text:
                    print(f"Dashboard {self.response_msg}")
                else:
                    print("Dashboard string not found" + str(response.status_code))


if __name__ == '__main__':
    test_instance = NavigateCategory()
    csrftoken = test_instance.get_csrf_token()
    headers_with_token = test_instance.get_base_header(csrftoken)
    test_instance.user_login(headers_with_token)
    test_instance.navigate_to_dashboard()
