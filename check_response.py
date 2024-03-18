from locust import HttpUser, between, SequentialTaskSet, task
import logging
import enum


class LogType(enum.Enum):
    INFO = 1
    DEBUG = 2
    ERROR = 3
    CRITICAL = 4


# Class definition #
class Logger:
    log_obj = None

    @staticmethod
    def init_logger(name, log_file):
        Logger.log_obj = logging.getLogger(name)
        open(log_file, 'w').close()

    @staticmethod
    def log_message(message, log_type=LogType.INFO):
        if not Logger.log_obj:
            print(message)
            return

        if log_type == LogType.INFO:
            Logger.log_obj.info(message)
        elif log_type == LogType.DEBUG:
            Logger.log_obj.debug(message)
        elif log_type == LogType.ERROR:
            Logger.log_obj.error(message)
        else:
            Logger.log_obj.critical(message)


class ViewCart(SequentialTaskSet):

    @task
    def get_all_cart_item(self):
        with self.client.get("/index.php?controller=order", catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get response with status: " + str(response.status_code))
                Logger.log_message("Failed to get response with status: " + str(response.status_code))
            else:
                if "Shopping-cart summary" in response.text:
                    response.success()
                    logging.log("SUCCESS with status: " + str(response.status_code))
                else:
                    response.failure("Failed" + response.text)
                    logging.log("Failed to get response with status: " + str(response.status_code))

    @task
    def exit_criteria(self):
        self.interrupt()


class MyUser(HttpUser):
    host = "http://www.automationpractice.pl"
    wait_time = between(1, 2)
    tasks = [ViewCart]
