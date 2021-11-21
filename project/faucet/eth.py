from django.apps import apps


def faucet_eth(faucet_request):
    web3 = apps.get_app_config('faucet').web3

    tx_hash = web3.eth.send_transaction({
        'to': faucet_request.address,
        'from': web3.eth.coinbase,
        'value': web3.toWei(faucet_request.value, 'ether')
    })
    # TODO: check tx_hash
    return tx_hash
