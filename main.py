from queries.virustotal import VirusTotal
from queries.alienvault import AlienVault
from queries.hybrid import Hybrid
from queries.triage import Triage


def main():
    file_hash = "02e30c889212c695f1e0c69981ff47b4a985953887976956abd523b2e1478d67"

    # print("\n🔍 VirusTotal File Check:")
    # vt_result = VirusTotal.virus_total_file_check(file_hash)
    # if vt_result:
    #     print(vt_result)

    print("\n🔍 VirusTotal Behavior Summary:")
    vt_behavior_summary = VirusTotal.virustotal_behavior_summary(file_hash)
    if vt_behavior_summary:
        print(vt_behavior_summary)

    # print("\n🔍 Checking with AlienVault OTX...")
    # av_result = AlienVault.alienvault_subscribed_check()
    # if av_result:
    #     print(av_result)

    # print("\n🔍 Checking with Hybrid Analysis...")
    # ha_result = Hybrid.hybrid_summary_report_check(file_hash)
    # if ha_result:
    #     print(ha_result)

    # print("\n🔍 Checking with Triage...")
    # sample_id = Triage.triage_search(file_hash)
    # if sample_id:
    #     print(sample_id)

    # print("\n TRIAGE SUMMARY REPORT")
    # ts_result = Triage.triage_summary(sample_id)
    # if ts_result:
    #     print(ts_result)

    # print("\n TRIAGE DYNAMIC REPORT")
    # td_result = Triage.triage_dynamic(sample_id)
    # if td_result:
    #     print(td_result)


if __name__ == "__main__":
    main()
