import json
import time
import requests
import urllib3

from config import *

session=requests.Session()


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

session.headers.update({
    "Authorization": f"Splunk {SPLUNK_TOKEN}"
})


def send_to_splunk(event):
    payload = {
        "host": "oracle-vps",
        "source": "cowrie",
        "sourcetype": "cowrie:json",
        "event": event,
    }

    response = session.post(
        SPLUNK_URL,
        json=payload,
        verify=VERIFY_SSL,
        timeout=10,
    )

    if response.status_code != 200:
        print("Failed:", response.text)
    else:
        print(f"Sent: {event['eventid']}")


with open(LOG_FILE, "r") as f:

    # Jump to the end of the file
    f.seek(0, 2)

    print("Watching for new Cowrie events...")

    while True:

        line = f.readline()

        if not line:
            time.sleep(0.5)
            continue

        try:
            event = json.loads(line)
            send_to_splunk(event)

        except json.JSONDecodeError:
            print("Invalid JSON")
