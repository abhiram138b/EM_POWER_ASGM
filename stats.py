def SummaryStatistics(records: list) -> dict:
    """
    Compute summary statistics and retrieve assets with high failure rates from a list of records.
    """
    if not records:
        return {
            "avg_downtime": 0,
            "avg_uptime": 0,
            "total_maintenance_cost": 0,
            "failure_rate_threshold": 0,
            "assets_with_high_failure_rates": []
        }
    
    sorted_records = sorted(records, key=lambda x: x["FailureRate"], reverse=True)
    
    avg_downtime = sum(record["Downtime"] for record in records) / len(records)
    avg_uptime = sum(record["Uptime"] for record in records) / len(records)
    total_maintenance_cost = sum(record["MaintenanceCosts"] for record in records)
    top_5_percent_index = int(len(records) * 0.05)
    top_5_percent_records = sorted_records[:top_5_percent_index]
    
    failure_rate_threshold = top_5_percent_records[-1]["FailureRate"] if top_5_percent_records else 0

    assets_with_high_failure_rates = [{"AssetID": record["AssetID"], "FailureRate": record["FailureRate"]} for record in records if record["FailureRate"] > failure_rate_threshold]

    return {
        "avg_downtime": avg_downtime,
        "avg_uptime": avg_uptime,
        "total_maintenance_cost": total_maintenance_cost,
        "failure_rate_threshold": failure_rate_threshold,
        "assets_with_high_failure_rates": assets_with_high_failure_rates
    }
