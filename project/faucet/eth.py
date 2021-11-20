from django.apps import apps


def faucet_eth(faucet_request):
    web3 = apps.get_app_config('faucet').web3

    if web3.eth.get_balance(faucet_request.address):
        nonce = web3.eth.getTransactionCount(web3.eth.coinbase)

        tx = {
            'nonce': nonce,
            'to': faucet_request.address,
            'value': web3.toWei(faucet_request.value, 'ether'),
            'gas': 2000000,
            'gasPrice': web3.toWei('50', 'gwei')
        }

        signed_tx = web3.eth.account.sign_transaction(tx)

        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

        # TODO: check tx_hash

        faucet_request.state = True

        faucet_request.save()

        return tx_hash