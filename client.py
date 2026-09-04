class CommercialCatchmentAreaProfilerClient:
    def profile_store_catchment(self, store_id='store_sf_01', store_lat=37.7915, store_lng=-122.4012, primary_radius_meters=800):
        return {
            'profiling_id': 'ctc_prf_7721',
            'store_id': store_id,
            'estimated_resident_population': 24500,
            'daytime_office_workers_density': 68000,
            'commercial_viability_score': 8.9,
            'cannibalization_risk_pct': 3.2,
            'catchment_dossier_url': 'https://carto.catchment.genpark.ai/dossiers/7721.json'
        }
