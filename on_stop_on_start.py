from locust import SequentialTaskSet, task, HttpUser, constant


class SearchGifts(SequentialTaskSet):
    def on_start(self):
        self.client.get("/", name=self.on_start.__name__)
        print("Task execution has Started")

    def on_stop(self):
        self.client.get("/", name=self.on_stop.__name__)
        print("ENDED")

    @task
    def look_products(self):
        self.client.get("/", name=self.look_products.__name__)
        print("look_products")

    @task
    def search_item(self):
        self.client.get("/", name=self.search_item.__name__)
        print("search_item")


class MyUser(HttpUser):
    host = "https://http.cat"
    wait_time = constant(1)
    tasks = [SearchGifts]
