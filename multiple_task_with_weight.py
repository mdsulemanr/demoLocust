from locust import User, task, TaskSet, between, SequentialTaskSet


class SearchProducts(SequentialTaskSet):
    @task
    def search_men_products(self):
        print("searching men products")

    @task
    def search_kids_products(self):
        print("searching kids products")

    @task
    def exit_this_task(self):
        self.interrupt()


class ViewCarts(SequentialTaskSet):
    @task
    def get_cart_items(self):
        print("getting all cart items")

    @task
    def search_cart_items(self):
        print("searching cart items")

    @task
    def exit_this_task(self):
        self.interrupt()


class MyUser(User):
    wait_time = between(1, 2)
    tasks = {
        SearchProducts: 4,
        ViewCarts: 1
    }
