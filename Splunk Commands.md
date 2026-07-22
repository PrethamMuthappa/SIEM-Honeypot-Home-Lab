index=main sourcetype="cowrie:json" | table _time eventid src_ip username password

index=* eventid=cowrie.command.input

index=main sourcetype="cowrie:json" eventid="cowrie.session.connect"

index=* filename=*

index=* file

index=* eventid=cowrie.session.file_download | table _time src_ip url shasum outfile

index=* eventid=cowrie.session.file_upload OR eventid=cowrie.session.file_download

index=main sourcetype="cowrie:json" password=cat | sort - _time

index=main sourcetype="cowrie:json" | sort - _time | table _time eventid src_ip username password

index=main sourcetype="cowrie:json" | head 10

index=main session=* eventid=* eventid="cowrie.session.connect"

index=main session=* eventid=* | stats count by eventid

index=main sourcetype="cowrie:json" src_ip="1205.19939"

index=main sourcetype="cowrie:json" | stats count by src_ip | sort -count | head 10

index=main sourcetype="cowrie:json" eventid="cowrie.client.size"

index=main sourcetype="cowrie:json" eventid="cowrie.login.success"

index=main eventid="cowrie.command.input" | table _time src_ip input

| mcatalog values(metric_name) as metrics WHERE NOT metric_name="*_mrollup_*" AND ("index=*" OR "index=*"...)

index=main session="a36449a6aab8" | table _time eventid message input username password | sort _time

index=main sourcetype="cowrie:json" eventid="cowrie.session.disconnect"

index=main sourcetype="cowrie:json" | stats count by eventid

index=main sourcetype="cowrie:json" eventid="cowrie.login.failed"

index=main eventid="cowrie.session.connect"

index=main | stats count by eventid

index="main"

source=""

source="manual-test"