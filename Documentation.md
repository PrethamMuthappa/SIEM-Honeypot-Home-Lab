Here is my documentation to set up a SOC homelab + honeypot 

- Splunk- Splunk cloud
- VPS - Currently using Oracle cloud instance to set up honeypot
- Tailscale
- Host OS: MacOS

Currently Going ahead with Splunk as the choice of SIEM tool to collect data from the vps and logs them, Wazhuh couldn't be installed in my VM due to cpu architecture/docker issue 

Created a splunk account and added data inputs **HTTP Event collector** because we decided to collect logs from vps to Splunk through https

for testing purpose whether the HEC works or not we send a curl request(HEC URL and token is important)

curl -k https://URL----.splunkcloud.com:8088/services/collector/event \
  -H "Authorization: TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "event": {
      "message": "Hello from my SOC Lab!"
    },
    "sourcetype": "_json",
    "source": "manual-test"
  }'



now we can see that data ingestion is successful and can be viewed here 

# Deploying Cowrie in vps

we will be using cowrie through VPS so we can isolate stuff 

Install Docker and compose

`docker run -d \`
  `--name cowrie \`
  `-p 2222:2222 \`
  `cowrie/cowrie:latest`
  

Just pull up the cowrie docker image and run it , if you try to build the docker image from source using there repo it will not work including both stable and latest release too

**Allow ingress rule to allow port 2222**



