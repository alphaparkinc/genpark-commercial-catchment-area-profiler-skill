from client import CommercialCatchmentAreaProfilerClient

def main():
    client = CommercialCatchmentAreaProfilerClient()
    res = client.profile_store_catchment('loc_ny_01', 40.7580, -73.9855)
    print('Commercial Catchment Profiler: ' + res['profiling_id'] + ' (Score: ' + str(res['commercial_viability_score']) + '/10)')
    print('Daytime Workers: ' + str(res['daytime_office_workers_density']) + ' | Cannibalization: ' + str(res['cannibalization_risk_pct']) + '%')
    print('Dossier URL: ' + res['catchment_dossier_url'])

if __name__ == '__main__':
    main()
