Here is my documentation to set up a SOC homelab + honeypot 

- SIEM- Splunk cloud
- VPS - Currently using Oracle cloud instance to set up honeypot
- Host OS: MacOS

Currently Going ahead with Splunk as the choice of SIEM tool to collect data from the vps and logs them, Wazhuh couldn't be installed in my VM due to cpu architecture/docker image

Created a splunk account and added data inputs **HTTP Event collector** because I decided to collect logs from vps to Splunk through https

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

<img width="1469" height="834" alt="Screenshot 2026-07-20 at 8 03 32 AM" src="https://github.com/user-attachments/assets/2cb52f88-9235-4ca0-b78b-b1297e25618f" />


now we can see that data ingestion is successful and can be viewed here 


# Deploying Cowrie in vps

we will be using cowrie through Docker so we can isolate stuff 

Install Docker and compose

`docker run -d \`
  `--name cowrie \`
  `-p 2222:2222 \`
  `cowrie/cowrie:latest`
  

Just pull up the cowrie docker image and run it , if you try to build the docker image from source using there repo it will not work including both stable and latest release too

**Allow ingress rule to allow port 2222**

Along with this we also create a folder where the docker will store the logs, we then use these logs and feed it to splunk


# Setting up python script to read logs and send to splunk

we automate this process by setting up a python script to read all the logs and do a post request to splunk

In here i came across a problem of SSL certificate issue so fixing it with generating a new cert but still doesn't work well do going to be turning off SSL= false for now its not recommended but for now it will do 

**First try** : Sent a single request to splunk to check if the logs are being read and queried in splunk (**Works!**)

**Next step**: will automate this part where every logs will be streamed to splunk


# Using Splunk to search the data and visualize them in dashboards

After 24 hours of collecting logs we now find ourself with 64 ip address conneting to our server with over 256 login attempets

Using SPL which is splunk's query language we can see different data and such

and we can also built charts to visualize them



<img width="1470" height="956" alt="Screenshot 2026-07-21 at 12 58 49 PM" src="https://github.com/user-attachments/assets/762ed158-26cd-4f53-ac05-f0a21a5139f1" />


<img width="1470" height="956" alt="Screenshot 2026-07-21 at 1 11 39 PM" src="https://github.com/user-attachments/assets/71b6085f-01a4-450f-b24f-01b888f7cded" />



I came across a major problem during this time, all ssh logs, ip address, passwords were all get logged normally but i noticed you actually cannot ssh into the shell after u enter the password 

for example when you `ssh -p 2222 root@ipaddrs` and when u enter any password it just gets stuck when it was supposed to let you log in to the shell irrespective of the password

**The Fix**

The cowrie docker image doesn't ship tty in the docker package and you had to install it and by that i was able to get into the cowrie shell





