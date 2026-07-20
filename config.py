import os
from dotenv import load_dotenv

load_dotenv()

SPLUNK_URL = os.getenv("SPLUNK_HEC_URL")
SPLUNK_TOKEN = os.getenv("SPLUNK_HEC_TOKEN")

LOG_FILE = os.getenv("LOG_FILE")

VERIFY_SSL = os.getenv("VERIFY_SSL", "true").lower() == "true"

