import os
import json
import requests
import getpass
import sys

def import_detectors_from_json(opensearch_host, username, password):
    api_endpoint = f"{opensearch_host}/_plugins/_anomaly_detection/detectors"
    headers = {"Content-Type": "application/json"}
    auth = (username, password)

    for filename in os.listdir('.'):
        if filename.endswith('.json'):
            print(f"Importing {filename}...")
            with open(filename, 'r') as file:
                try:
                    detector_config = json.load(file)
                    response = requests.post(
                        api_endpoint,
                        headers=headers,
                        json=detector_config,
                        auth=auth,
                        verify=False  # Disable SSL verification
                    )
                    if response.status_code == 201:
                        print(f"✅ Successfully imported {filename}")
                    else:
                        print(f"❌ Failed to import {filename}: {response.status_code} - {response.text}")
                except json.JSONDecodeError as e:
                    print(f"⚠️ Error decoding {filename}: {e}")
                except Exception as e:
                    print(f"🔥 Unexpected error with {filename}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python opensearch_import_ml_detectors_json.py <opensearch_host> <username>")
        print("Example: python opensearch_import_ml_detectors_json.py https://10.101.2.126:9200 admin")
        sys.exit(1)

    opensearch_host = sys.argv[1]
    username = sys.argv[2]
    password = getpass.getpass(prompt='Enter your OpenSearch password: ')

    import_detectors_from_json(opensearch_host, username, password)
