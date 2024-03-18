import requests


class NavigateCategory:
    def __init__(self):
        self.csrftoken = None
        self.host = "https://learn.tndy.academy"
        self.session = requests.Session()

    # def get_login(self):
    #     with requests.get(url='https://learn.tndy.academy') as response:
    #         print(response.status_code)

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
            # 'X-Csrftoken': token,
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
        response = self.session.get("{}/".format(
                                        self.host), allow_redirects=False)  # https://learn.sdaia.academy/csrf/api/v1/token
        if response.status_code == 302 and response.cookies['csrftoken']:
            # print(resp.cookies['csrftoken'])
            self.csrftoken = response.cookies['csrftoken']
            # print(response.cookies['csrftoken'])

    def on_start(self):
        self.set_csrf_token_before_login()
        headers = self.get_base_header_with_token()

        payload = {
            'email_or_username': 'test1_learner', 'password': 'pfDB3MNShF5Tq7m'
            # ,'next': '/dashboard'
        }

        with self.session.post("{}/api/user/v2/account/login_session/".format(self.host), data=payload,
                               headers=headers) as response:
            print(response.text)
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
                print('login Failed with status code: ' + str(response.status_code))

    def navigate_to_dashboard(self):
        with self.session.get("{}/dashboard".format(self.host)) as response:
            if response.status_code == 200:
                if "Dashboard" in response.text:
                    pass
                else:
                    print("Dashboard string not found" + str(response.status_code))


obj1 = NavigateCategory()

obj1.on_start()
obj1.navigate_to_dashboard()
