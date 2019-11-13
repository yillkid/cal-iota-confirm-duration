import time
from send import transfer
from get_status import get_inclusion_states
from iota import Iota
from config_iota_wallet import NODE_URL, SEED, RECEIVE_ADDR

for index in range(100):
    # send
    bundle_hash = transfer(RECEIVE_ADDR, "TAG", "MSG", 0)
    print("Send IOTA txn success, bundle: " + str(bundle_hash))

    # get status
    api = Iota(NODE_URL, SEED)
    list_txns = api.find_transaction_objects(bundles = [bundle_hash])

    index = 0
    count = 0
    start_time = time.time()
    elapsed_time = time.time()
    while True:
        if index == len(list_txns["transactions"]):
            elapsed_time = time.time() - start_time
            print("Confirm! duration is: " + time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
            time.sleep(1)
            break

        status = get_inclusion_states(str(list_txns["transactions"][index].hash))

        if status:
            index = index + 1
        else:
            time.sleep(1)

        count = count + 1
        if count > 300:
            print("Timeout! " + time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
            break
