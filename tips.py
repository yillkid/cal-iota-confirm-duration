import json
import requests
from send import transfer
from iota import Iota
from config_iota_wallet import NODE_URL, SEED

def get_tips():
    data = {'command': 'getTransactionsToApprove', 'depth':4}
    headers = {'Content-type': 'application/json', 'X-IOTA-API-Version': '1'}
    r = requests.post(NODE_URL, data=json.dumps(data), headers=headers)
    if r.status_code == requests.codes.ok:
        json_response = json.loads(r.text)
        return json_response["trunkTransaction"], json_response["branchTransaction"]

def get_latest_milestone():
    data = {'command': 'getNodeInfo'}
    headers = {'Content-type': 'application/json', 'X-IOTA-API-Version': '1'}
    r = requests.post(NODE_URL, data=json.dumps(data), headers=headers)

    if r.status_code == requests.codes.ok:
        json_node_info = json.loads(r.text)
        return json_node_info["latestMilestone"]
