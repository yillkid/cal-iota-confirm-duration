# coding=utf-8
from iota import Iota
from config_iota_wallet import NODE_URL, SEED

api = Iota(NODE_URL, SEED)
dict_account = api.get_account_data()

print("Balance: " + str(dict_account["balance"]))
