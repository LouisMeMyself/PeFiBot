from web3 import Web3

from constants import Constants

w3 = Web3(Web3.HTTPProvider("https://api.avax.network/ext/bc/C/rpc"))
if not w3.isConnected():
    print("Error web3 can't connect")
ipefi_contract = w3.eth.contract(address=Constants.IPEFI_ADDRESS, abi=Constants.IPEFI_ABI)

def getIPefiRatio():
    return w3.fromWei(ipefi_contract.functions.currentExchangeRate().call(), 'ether')

if __name__ == '__main__':
    getIPefiRatio()
