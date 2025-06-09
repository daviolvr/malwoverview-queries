import requests
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path)

class VirusTotal:

    @staticmethod
    def virus_total_file_check(file_id: str):
        url = f"https://www.virustotal.com/api/v3/files/{file_id}"

        headers = {
            'x-apikey': os.environ.get("VIRUSTOTAL_APIKEY")
        }

        response = requests.get(url=url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"VirusTotal Error {response.status_code}: {response.text}")
            return None
    

    @staticmethod
    def virustotal_behavior_summary(file_id: str):
        url = f"https://www.virustotal.com/api/v3/files/{file_id}/behaviour_summary"

        headers = {
            'x-apikey': os.environ.get("VIRUSTOTAL_APIKEY")
        }

        response = requests.get(url=url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"VirusTotal Error {response.status_code}: {response.text}")
            return None
        
    
    @staticmethod
    def virustotal_mitre_summary(file_id: str):
        url = f"https://www.virustotal.com/api/v3/files/{file_id}/behaviour_mitre_trees"

        headers = {
            'x-apikey': os.environ.get("VIRUSTOTAL_APIKEY")
        }

        response = requests.get(url=url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"VirusTotal Error {response.status_code}: {response.text}")
            return None

        
        