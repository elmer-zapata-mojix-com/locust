from locust import HttpUser, task, between

class PokemonExample(HttpUser):
    wait_time = between(1, 5)
    @task
    def hello_world(self):
        self.client.get("/api/v2/pokemon/onix")
