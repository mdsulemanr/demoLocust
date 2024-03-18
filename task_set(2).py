from locust import HttpUser, task, TaskSet, constant


class SearchProducts(TaskSet):
    @task
    def search_men_products(self):
        self.client.get("200")
        print("status 200")

    @task
    def exit_criteria(self):
        self.interrupt(reschedule=False)  # BREATH TIME


class ViewCarts(TaskSet):
    @task
    def get_cart_items(self):
        self.client.get("500")
        print("status 500")

    @task
    def exit_criteria(self):
        self.interrupt(reschedule=False)  # BREATH TIME


class MyUser(HttpUser):
    host = "https://http.cat/"
    wait_time = constant(1)
    tasks = [SearchProducts, ViewCarts]
