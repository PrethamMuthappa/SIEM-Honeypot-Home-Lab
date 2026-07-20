import json
import requests
import urllib3
import certifi
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from config import *

headers = {
    "Authorization": f"Splunk {SPLUNK_TOKEN}"
}

with open(LOG_FILE) as f:
    line = f.readline()

event = json.loads(line)

payload = {
    "event": event,
    "sourcetype": "_json"
}

response = requests.post(
    SPLUNK_URL,
    headers=headers,
    json=payload,
    verify=VERIFY_SSL,
    timeout=10,
)

print(response.status_code)
print(response.text)
