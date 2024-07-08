from locust import HttpUser, task

class PokemonExample(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/api/v2/pokemon/onix")
