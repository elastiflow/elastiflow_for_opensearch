# ElastiFlow OpenSearch Anomaly Detector Import Script

The Python script `opensearch_import_ml_dectors_json.py` automates the process of importing ElastiFlow's JSON-based anomaly detector configurations into an OpenSearch cluster using its Anomaly Detection API.

## 🧾 Features

- Automatically scans the current directory for `.json` detector configuration files
- Sends each file to OpenSearch using the `_plugins/_anomaly_detection/detectors` API
- Accepts host and username via command-line arguments
- Prompts for the password securely (hidden input)
- Disables SSL verification (useful for self-signed certificates)

---

## Opensearch HC anomaly detectors

By default Opensearch limits the number of HC anomaly detectors to 10. This can be increased by adding `plugins.anomaly_detection.max_multi_entity_anomaly_detectors` to the `opensearch.yml` configuration file and restarting opensearch.

## 🛠️ Prerequisites

- Python 3.6+
- `requests` library  
  Install it using:

  ```bash
  pip install requests
