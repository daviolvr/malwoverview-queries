import os
import requests
from dotenv import load_dotenv

DOTENV_PATH = os.path.join(os.path.dirname(__file__), "..", "..", ".env")
load_dotenv(DOTENV_PATH)

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
        url = f"https://tria.ge/api/v0/samples/{id}/overview.json"

        headers = {
            'Authorization': f'Bearer {os.environ.get("TRIAGE_APIKEY")}'
        }

        response = requests.get(url=url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Triage Error {response.status_code}: {response.text}")
            return None
        

    @staticmethod
    def triage_dynamic(id: str):
        url = f"https://tria.ge/api/v0/samples/{id}/behavioral1/report_triage.json"

        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {os.environ.get("TRIAGE_APIKEY")}'
        }

        response = requests.get(url=url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Triage Error {response.status_code}: {response.text}")
            return None
        

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
    def alienvault_subscribed_check(file_id: str):
        params = {
            'limit': file_id,
        }

        url = f"https://otx.alienvault.com/api/v1/pulses/subscribed"

        response = requests.get(url=url, headers=AlienVault.headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"AlienVault Error {response.status_code}: {response.text}")
            return None


