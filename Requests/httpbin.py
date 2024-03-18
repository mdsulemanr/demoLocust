import requests


class NavigateCategory:
    def __init__(self):
        self.payload = {
            "page": "2",
            "count": "25"
        }
        self.data = {
            'username': 'test',
            'password': 'testing123'
        }

    def send_params_in_payload(self):
        response = requests.get('https://httpbin.org/get', params=self.payload)
        # print(response.text)
        print(response.url)

    def post_request(self):
        with requests.post('https://httpbin.org/post', data=self.data) as response:
            response_dist = response.json()
            print(response_dist['form'])

    def auth(self):
        with requests.get('https://httpbin.org/basic-auth/test/testing123',
                          auth=('test', 'testing123')) as response:
            print(response.text)

    def auth_with_wrong_credentials(self):
        with requests.get('https://httpbin.org/basic-auth/test/testing123',
                          auth=('test_wrong', 'testing123')) as response:
            print(response)

    def time_delay(self):
        with requests.get('https://httpbin.org/delay/6', timeout=3) as response:
            print(response.text)

obj1 = NavigateCategory()
obj1.time_delay()