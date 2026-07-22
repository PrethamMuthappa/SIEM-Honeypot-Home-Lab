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


def follow():
    f = open(LOG_FILE, "r")
    f.seek(0, os.SEEK_END)
    inode = os.fstat(f.fileno()).st_ino

    print("Watching for new Cowrie events...")

    while True:
        line = f.readline()

        if line:
            try:
                event = json.loads(line)
                send_to_splunk(event)
            except json.JSONDecodeError:
                print("Invalid JSON")
            continue

        time.sleep(0.5)

        try:
            new_inode = os.stat(LOG_FILE).st_ino
        except FileNotFoundError:
            continue

        if new_inode != inode:
            print("Log rotated. Reopening...")

            f.close()
            f = open(LOG_FILE, "r")
            inode = os.fstat(f.fileno()).st_ino



       
follow()       
