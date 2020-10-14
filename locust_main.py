from locust import HttpUser, TaskSet, between, task

from locustfiles.locust_newsCommand import TestNewsCommand
from locustfiles.locust_LightCut import ForumSection


class LoggedInUser(HttpUser):
    wait_time = between(1, 5)
    tasks = {TestNewsCommand: 1}


if __name__ == "__main__":
    import os

    os.system("locust -f locust_main.py --host=http://100.0.10.180:8080")
    # os.system("locust -f locust_main.py --host=http://news.baidu.com --logfile=./log.txt")
