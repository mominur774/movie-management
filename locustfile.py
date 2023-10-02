from locust import HttpUser, TaskSet, task

class UserBehavior(TaskSet):
    def on_start(self):
        self.client.post("/login", {"username": "admin", "password": "password"})

    def on_stop(self):
        self.client.post("/logout", {"username": "admin", "password": "password"})

    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def test(self):
        self.client.get("/test")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 5000
    max_wait = 9000
