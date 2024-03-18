from locust import HttpUser, task, TaskSet, between, SequentialTaskSet


class SearchProducts(SequentialTaskSet):

    @staticmethod
    def get_base_header():
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
            # 'X-CSRFToken': token,
            'Origin': 'https://apps.tndy.academy',
            'Referer': 'https://apps.tndy.academy/',
            'Upgrade-Insecure-AutoQuote': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
        }
        return base_header

    @task
    def search_men_products(self):
        with self.client.get("https://courses.tndy.academy/", headers=self.get_base_header()) as response:
            print(response.status_code)


class MyUser(HttpUser):
    wait_time = between(1, 2)
    tasks = [SearchProducts]
