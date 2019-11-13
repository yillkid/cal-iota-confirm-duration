import time
import json
import requests
NODE_URL="https://node.deviceproof.org:443"
DEPTH = 14

def get_tips():
    data = {'command': 'getNodeInfo'}
    headers = {'Content-type': 'application/json', 'X-IOTA-API-Version': '1'}
    r = requests.post(NODE_URL, data=json.dumps(data), headers=headers)

    # latestSolidSubtangleMilestoneIndex
    if r.status_code == requests.codes.ok:
        json_node_info = json.loads(r.text)
        return json_node_info["latestMilestone"]

def get_inclusion_states(txn_hash):
    tips = get_tips()
    data = {'command': 'getInclusionStates', 'transactions':[txn_hash], 'tips':[tips]}
    headers = {'Content-type': 'application/json', 'X-IOTA-API-Version': '1'}
    r = requests.post(NODE_URL, data=json.dumps(data), headers=headers)
    if r.status_code == requests.codes.ok:
        json_response = json.loads(r.text)
        print(r.text)
        return json_response["states"][0]

for index in range(20):
    # txn_hash = "YPWUTTNUTYEXEZVJEZRJ9HYOABHDOTZLRQSUYGQBHLQJDXC9OTEWCDYELCRB9MRBQDQWMGUQIMOP99999"
    txn_hash = "ZO9DGGTGMF9BRMAHBJETDQAPCCPOTYDDRNXRFPNTWIIKQFJFMXBSFLRZLB99TCXEGTMMGAQGUGOWZ9999"
    print("txn hash = " + txn_hash)
    status = get_inclusion_states(txn_hash)
    time.sleep(1)
