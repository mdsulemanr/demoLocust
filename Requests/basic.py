import requests


class NavigateCategory:

    def view_home_page(self):
        with requests.get('https://learn.tndy.academy/login') as resp:
            print(resp.status_code)
            print(resp.is_redirect)
            print(dir(resp))
            print(help(resp))

    def get_csrf_token(self):
        with requests.get('https://learn.tndy.academy/api/user/v2/account/login_session/') as resp:
            if resp.ok:
                print(resp.cookies)


obj1 = NavigateCategory()
obj1.get_csrf_token()
