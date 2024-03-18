import logging

from locust import User, between, SequentialTaskSet, events, task


@events.test_start.add_listener
def on_test_start(**kwargs):
    print("------Initiating load Testing-----On_test_start")


@events.test_stop.add_listener
def on_test_end(**kwargs):
    logging
    print("------Load Testing Completed-----On_test_end")


class SearchProducts(SequentialTaskSet):
    def on_start(self):
        print("SearchProducts: Test execution has Started")

    def on_stop(self):
        print("SearchProducts: Test execution has ended")

    @task
    def search_men_products(self):
        print("searching men products")

    @task
    def search_kids_products(self):
        print("searching for kids products")


class MyUser(User):
    wait_time = between(1, 2)
    tasks = [SearchProducts]

    def on_start(self):
        print("MyUser: Hatching new user")

    def on_stop(self):
        print("MyUser: deleting new user")
