from core.settings import db
from .externals import Triage, VirusTotal, AlienVault, Hybrid
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

collection = db["hashes"]

class InsertService:

    def realizar_buscas_paralelas(file_hash) -> dict:
        triage_id = Triage.triage_search(file_hash)

        with ThreadPoolExecutor() as executor:
            futures = {
                "triage_summary": executor.submit(Triage.triage_summary, triage_id),
                "triage_dynamic": executor.submit(Triage.triage_dynamic, triage_id),
                "hybrid": executor.submit(Hybrid.hybrid_summary_report_check, file_hash),
                "virustotal_file_check": executor.submit(VirusTotal.virus_total_file_check, file_hash),
                "virustotal_behaviour_summary": executor.submit(VirusTotal.virustotal_behavior_summary, file_hash),
                "virustotal_mitre_summary": executor.submit(VirusTotal.virustotal_mitre_summary, file_hash),
                "alienvault_subscribed_check": executor.submit(AlienVault.alienvault_subscribed_check, file_hash),
            }

            responses = {}
            for key, future in futures.items():
                try:
                    responses[key] = future.result()
                except Exception as e:
                    print(f"Erro ao buscar na API {key}: {e}")
                    responses[key] = None
        
        return responses


    def db_insert(data_dict) -> str:
        data_dict["timestamp"] = datetime.now()
        result = collection.insert_one(data_dict)
        return str(result.inserted_id)

