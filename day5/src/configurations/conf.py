#create configuration for the project
 
import os
from dotenv import load_dotenv
 
load_dotenv()
 
class Config:
    def __init__(self):
        self.app_env = os.getenv("APP_ENV", "Development")
        self.resource_path = self.get_resource_path("data")
 
    def get_resource_path(self, resource_name) -> str:
        if self.app_env == "Production":
            return f"src/resources/customers.json"
        elif self.app_env == "Development":
            return f"src/resources/customers.csv"
        elif self.app_env == "Testing":
            return f"src/resources/customers.txt"
        else:
            raise ValueError(f"Invalid APP_ENV value. Must be 'production', 'Development', or 'Test': {self.app_env}")