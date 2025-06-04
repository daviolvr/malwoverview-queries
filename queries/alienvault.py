import requests
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path)

class AlienVault:
    headers = {
        'X-OTX-API-KEY': os.environ.get("ALIENVAULT_APIKEY")
    }

    @staticmethod
    def alienvault_file_check(file_id: str):
        url = f"https://otx.alienvault.com/api/v1/indicators/file/{file_id}/analysis"
        

        response = requests.get(url=url, headers=AlienVault.headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"AlienVault Error {response.status_code}: {response.text}")
            return None

    
    @staticmethod
    def alienvault_subscribed_check():
        url = f"https://otx.alienvault.com/api/v1/pulses/subscribed"

        response = requests.get(url=url, headers=AlienVault.headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"AlienVault Error {response.status_code}: {response.text}")
            return None
