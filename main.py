import json
from models.traffic_tracker import get_traffic_summary
from models.ore_estimator import estimate_stockpile

def orchestrate():
    # Example integration of camera analytics and stockpile estimates
    traffic = get_traffic_summary(None)
    ore_inventory = estimate_stockpile(None)

    payload = {
        "timestamp": "2026-10-07T12:00:00Z",
        "warehouse_analytics": {
            "traffic": traffic,
            "inventory": ore_inventory
        }
    }

    with open('outputs/malva_warehouse_payload.json', 'w') as f:
        json.dump(payload, f, indent=4)
    print("Orchestration complete. Payload saved to outputs/malva_warehouse_payload.json")

if __name__ == "__main__":
    orchestrate()
