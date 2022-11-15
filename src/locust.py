from locust import constant_pacing
from locust import HttpUser
from locust import run_single_user
from locust import TaskSet


def task_io(task):
    task.client.get("/run_sync?cpu_test=false&io_test=true")


def task_cpu(task):
    task.client.get("/run_sync?cpu_test=true&io_test=false")


class TaskHttp(TaskSet):
    tasks = [task_io, task_cpu]


class User(HttpUser):
    wait_time = constant_pacing(1)
    host = "http://localhost:8999"
    tasks = [TaskHttp]


if __name__ == "__main__":
    run_single_user(User)
