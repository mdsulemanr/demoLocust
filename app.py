from locust import User, task, between, constant, TaskSet, SequentialTaskSet


class SearchProducts(User):
    weight = 2
    wait_time = constant(1)
    @task
    def search_products(self):
        print("Class1: task1")

    @task
    def search_categories(self):
        print("Class2: task2")


class SearchVehicles(User):
    weight = 2
    wait_time = constant(1)

    @task
    def search_for_products(self):
        print("looking for it")

    @task
    def search_for_categories(self):
        print("got it")


