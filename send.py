# coding=utf-8
from iota import Iota, ProposedTransaction, Address, TryteString, Tag, Transaction
from config_iota_wallet import NODE_URL, SEED, DEPTH, MIN_WEIGHT_MAGNITUDE

def transfer(address, tag, message, value):

    recipient_address = address
    sender_message = message
    sender_tag = tag

    bundle_hash = ""
    prepared_transferes = []
    api = Iota(NODE_URL, SEED)

    sender_tag = sender_tag
    transfer_value = int(value)

    txn = \
        ProposedTransaction(
            address = Address(
                recipient_address
        ),

        message = TryteString.from_string(sender_message),
        tag = Tag(sender_tag),
        value = transfer_value,
    )

    prepared_transferes.append(txn)
    try:
        bundle_hash = api.send_transfer(
            depth=DEPTH,
            transfers=prepared_transferes,
            min_weight_magnitude=MIN_WEIGHT_MAGNITUDE
        )
    except Exception as e:
        return "Exception." + e

    return str(bundle_hash['bundle'].hash)
