import requests
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path)

class Triage:
    
    @staticmethod
    def triage_search(file_hash: str) -> str:
        url = f"https://tria.ge/api/v0/search?query={file_hash}"

        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {os.environ.get("TRIAGE_APIKEY")}'
        }

        response = requests.get(url=url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            first_id = data['data'][0]['id']
            return first_id
        else:
            print(f"Triage Error {response.status_code}: {response.text}")
            return None


    @staticmethod
    def triage_summary(id: str):
        url = f"https://tria.ge/api/v0/samples/{id}/summary"

        headers = {
            'Authorization': f'Bearer {os.environ.get("TRIAGE_APIKEY")}'
        }

        response = requests.get(url=url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Triage Error {response.status_code}: {response.text}")
            return None
