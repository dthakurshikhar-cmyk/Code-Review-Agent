# Assuming a generic wrapper for Hindsight observability and continuous learning
import requests
from config import HINDSIGHT_API_KEY

class HindsightLogger:
    def __init__(self):
        self.api_key = HINDSIGHT_API_KEY
        self.endpoint = "https://api.hindsight.ai/v1/log" # Example endpoint

    def log_review(self, pr_number: int, diff: str, prompt: str, generated_review: str):
        if not self.api_key:
            print("Hindsight API key not configured. Skipping remote log.")
            return

        payload = {
            "task": "code_review",
            "metadata": {"pr_number": pr_number},
            "inputs": {"diff": diff, "prompt": prompt},
            "output": generated_review
        }
        
        try:
            requests.post(
                self.endpoint, 
                json=payload, 
                headers={"Authorization": f"Bearer {self.api_key}"},
                timeout=5
            )
        except Exception as e:
            print(f"Failed to log to Hindsight: {e}")