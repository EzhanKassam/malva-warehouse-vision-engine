import numpy as np

def estimate_stockpile(image_path, bulk_density=1.6):
    # Simulated stockpile segmentation and tonnage calculation
    area_m2 = 120.5
    avg_depth = 3.2
    volume_m3 = area_m2 * avg_depth
    tonnage = volume_m3 * bulk_density

    return {
        "volume_m3": volume_m3,
        "tonnage": tonnage,
        "capacity_utilization": 67.5,
        "bay_utilization": {
            "Bay A": 75.0,
            "Bay B": 60.0
        }
    }
