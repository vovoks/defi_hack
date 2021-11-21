from django.apps import apps
from django.db.models.signals import pre_save
from django.dispatch import receiver

from faucet.models import FaucetRequests

from faucet.eth import faucet_eth


@receiver(pre_save, sender=FaucetRequests)
def send_eth(sender, instance, **kwargs):
    web3 = apps.get_app_config('faucet').web3
    address = instance.address.lower()
    instance.address = web3.toChecksumAddress(address)
    faucet_eth(instance)
    instance.state = True
