from locust import task, HttpUser, between, SequentialTaskSet, TaskSet, wait_time, constant


class Jupyterlite(SequentialTaskSet):

    @task
    def home_page(self):
        with self.client.get("/lab/index.html", catch_response=True) as response:
            # print(response.text)
            if response.status_code == 200:
                if "JupyterLite" in response.text:
                    response.success()
                else:
                    response.failure("JupyterLite not found")

    @task
    def add_notebook1(self):
        with self.client.get(
                "/lab/index.html?fromURL=https://raw.githubusercontent.com/"
                "jupyterlab/jupyterlab-demo/master/notebooks/Lorenz.ipynb",
                data={
                    "fromURL": "https://raw.githubusercontent.com/"
                               "jupyterlab/jupyterlab-demo/master/notebooks/Lorenz.ipynb"
                }, catch_response=True) as response:
            # print(response.text)
            if response.status_code == 200:
                if "JupyterLite" in response.text:
                    response.success()
                else:
                    response.failure("JupyterLite not found, url:"
                                     "/lab/index.html?fromURL=https://raw.githubusercontent.com/"
                                     "jupyterlab/jupyterlab-demo/master/notebooks/Lorenz.ipynb")

    @task
    def add_notebook2(self):
        with self.client.get(
                "/lab/index.html?fromURL=https://raw.githubusercontent.com/"
                "jupyterlab/jupyterlab-demo/master/data/iris.csv",
                data={
                    "fromURL": "https://raw.githubusercontent.com/"
                               "jupyterlab/jupyterlab-demo/master/data/iris.csv"
                }, catch_response=True) as response:
            if response.status_code == 200:
                if "JupyterLite" in response.text:
                    response.success()
                else:
                    response.failure("JupyterLite not found, url:"
                                     "/lab/index.html?fromURL=https://raw.githubusercontent.com/"
                                     "jupyterlab/jupyterlab-demo/master/data/iris.csv")

    @task
    def add_notebook3(self):
        with self.client.get(
                "?fromURL=https://raw.githubusercontent.com/jupyterlab/jupyterlab-demo/master/notebooks/Lorenz.ipynb&"
                "fromURL=https://raw.githubusercontent.com/jupyterlab/jupyterlab-demo/master/data/iris.csv",
                data={
                    "fromURL": "https://raw.githubusercontent.com/"
                               "jupyterlab/jupyterlab-demo/master/notebooks/Lorenz.ipynb",
                    "fromURL": "https://raw.githubusercontent.com/"
                               "jupyterlab/jupyterlab-demo/master/data/iris.csv"
                }, catch_response=True) as response:
            if response.status_code == 200:
                if "JupyterLite" in response.text:
                    response.success()
                else:
                    response.failure("JupyterLite not found, url:"
                                     "?fromURL=https://raw.githubusercontent.com/"
                                     "jupyterlab/jupyterlab-demo/master/notebooks/Lorenz.ipynb&"
                                     "fromURL=https://raw.githubusercontent.com/"
                                     "jupyterlab/jupyterlab-demo/master/data/iris.csv")


class UserGroupA(HttpUser):
    wait_time = constant(1)
    host = "https://jupyterlite.tndy.academy"
    tasks = [Jupyterlite]
