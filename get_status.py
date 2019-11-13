import json
import requests
from tips import get_latest_milestone 
from config_iota_wallet import NODE_URL

def get_inclusion_states(txn_hash):
    tips = get_latest_milestone()
    data = {'command': 'getInclusionStates', 'transactions':[txn_hash], 'tips':[tips]}
    headers = {'Content-type': 'application/json', 'X-IOTA-API-Version': '1'}
    r = requests.post(NODE_URL, data=json.dumps(data), headers=headers)
    if r.status_code == requests.codes.ok:
        json_response = json.loads(r.text)
        return json_response["states"][0]
