from locust import task, HttpUser, between, SequentialTaskSet, TaskSet, wait_time, constant
import logging


class UtilHelper:

    @staticmethod
    def navigate_page(self, url, keyword, resp_fail_msg, status_code_fail_msg, params=None):
        if params is None:
            params = {}
        with self.client.get(url, catch_response=True) as response:
            if response.status_code == 200:
                if keyword in response.text:
                    response.success()
                else:
                    logging.info(resp_fail_msg)
            else:
                logging.error(status_code_fail_msg)


class Jupyterlite(SequentialTaskSet):

    @task
    def home_page(self):
        UtilHelper.navigate_page(self, "/lab/index.html", "JupyterLite",
                                 "JupyterLite not found",
                                 "Failed to navigate url")

    @task
    def add_notebook1(self):
        UtilHelper.navigate_page(self,
                                 "/lab/index.html?fromURL=https://raw.githubusercontent.com"
                                 "/jupyterlab/jupyterlab-demo/master/notebooks/Lorenz.ipynb",
                                 "JupyterLite", "JupyterLite not found",
                                 "Failed to navigate url", params={
                "fromURL": "https://raw.githubusercontent.com/jupyterlab/jupyterlab-demo/master/notebooks/Lorenz.ipynb"
            })

    @task
    def add_notebook2(self):
        UtilHelper.navigate_page(self,
                                 url="/lab/index.html?fromURL=https://raw.githubusercontent.com"
                                     "/jupyterlab/jupyterlab-demo/master/data/iris.csv",
                                 keyword="JupyterLite", resp_fail_msg="JupyterLite not found",
                                 status_code_fail_msg="Failed to navigate url")

    @task
    def add_notebook3(self):
        UtilHelper.navigate_page(self,
                                 url="?fromURL=https://raw.githubusercontent.com"
                                     "/jupyterlab/jupyterlab-demo/master/notebooks/Lorenz.ipynb&fromURL="
                                     "https://raw.githubusercontent.com"
                                     "/jupyterlab/jupyterlab-demo/master/data/iris.csv",
                                 keyword="JupyterLite", resp_fail_msg="JupyterLite not found",
                                 status_code_fail_msg="Failed to navigate url")


class UserGroupA(HttpUser):
    host = "https://jupyterlite.tndy.academy"
    wait_time = constant(1)

    tasks = [Jupyterlite]
