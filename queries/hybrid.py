import requests
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path)

class Hybrid:
    
    @staticmethod
    def hybrid_summary_report_check(file_id: str):
        url = f"https://www.hybrid-analysis.com/api/v2/report/{file_id}/summary"

        headers = {
            'user_agent': 'Falcon Sandbox',
            'api-key': os.environ.get("HYBRID_APIKEY"),
            'content-type': 'application/json'
        }

        response = requests.get(url=url, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Hybrid Analysis Error {response.status_code}: {response.text}")
            return None
        