import random
from typing import List, Dict
from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Access the testing database
db = client["testing"]

# Access the asset and performanceMetrics collections
asset_collection = db["asset"]
pm_collection = db["performanceMetrics"]


def generate_random_assets(num_records: int) -> List[Dict]:
    assets = []
    for i in range(1, num_records + 1):
        asset = {
            "AssetID": i,
            "AssetName": f"Asset{i}",
            "AssetType": f"Type{i}",
            "Location": f"Location{i}",
            "PurchaseDate": "2-3-2024",
            "InitialCost": random.uniform(1000, 10000),
            "OperationalStatus": random.choice(["Operational", "Non-operational"]),
        }
        assets.append(asset)
    return assets


def generate_random_pm(num_records: int) -> List[Dict]:
    pms = []
    for i in range(1, num_records + 1):
        pm = {
            "AssetID": i,
            "Uptime": random.uniform(80, 100),  # Example range for uptime
            "Downtime": random.uniform(0, 20),  # Example range for downtime
            "MaintenanceCosts": random.uniform(100, 1000),  # Example range for maintenance costs
            "FailureRate": random.uniform(0.1, 2),  # Example range for failure rate
            "Efficiency": random.uniform(80, 100),  # Example range for efficiency
        }
        pms.append(pm)
    return pms


# Generating 1000 records
num_records = 1000
assets = generate_random_assets(num_records)
pms = generate_random_pm(num_records)

print(len(pms))
asset_collection.insert_many(assets)
pm_collection.insert_many(pms)

client.close()
