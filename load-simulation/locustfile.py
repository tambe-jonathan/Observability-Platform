import random
from locust import HttpUser, task, between

class SREPlatformUser(HttpUser):
    # Simulates a user waiting 1 to 5 seconds between actions
    wait_time = between(1, 5)

    @task(5) # This task happens 5x more often (The "Happy Path")
    def view_homepage(self):
        self.client.get("/", name="Home Page")

    @task(2)
    def view_metrics_dashboard(self):
        # This simulates a user hitting an API endpoint
        self.client.get("/api/v1/status", name="Status API")

    @task(1)
    def trigger_potential_error(self):
        # This helps us see if our 'Spies' catch 404 errors
        pages = ["/login", "/settings", "/admin", "/secret-page"]
        target = random.choice(pages)
        self.client.get(target, name="Random Page Navigation")

    def on_start(self):
        """ Runs when a simulated user starts """
        print("👤 A new simulated user has joined the platform...")
