from web3 import Web3
from web3. middleware import geth_poa_middleware
from contract_info import abi, address_contract

w3= Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion. inject(geth_poa_middleware,layer=0)

contract = w3.eth.contract(address=address_contract, abi=abi)

print(f"Баланс пользователя 1: {w3.eth.get_balance('0x24CD8b647421fEb02e9edbeeEd8DAb778b464f32')}")
print(f"Баланс пользователя 2: {w3.eth.get_balance('0x83a831210656aD61eB59a01F4c933C2bC2bE13AF')}")
print(f"Баланс пользователя 3: {w3.eth.get_balance('0x1516550B0275154Ff9fB2274998EB70DC289c976')}")
print(f"Баланс пользователя 4: {w3.eth.get_balance('0x7E5Cbeab3D45F77Aa2Bbaf8ABa704A0291227B82')}")
print(f"Баланс пользователя 5: {w3.eth.get_balance('0xD9BAf02A36Bd2CE92327369e8758283357395607')}")