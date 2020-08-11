from locust import HttpUser, TaskSet, task


class UserBehavior(TaskSet):
    def on_start(self):
        self.client.get("/")

    @task(3)
    def posts(self):
        self.client.get("/posts")

    @task(1)
    def new_comment(self):
        data = {
            "postId": 1,
            "author": "test user",
            "body": "Some text. Hello world!"
        }
        self.client.post("/comments", json=data)

    @task(1)
    def comments(self):
        self.client.get("/comments")


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 1000
    max_wait = 2000