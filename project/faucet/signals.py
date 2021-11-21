from django.db.models.signals import pre_save
from django.dispatch import receiver

from faucet.models import FaucetRequests

from faucet.eth import faucet_eth


@receiver(pre_save, sender=FaucetRequests)
def send_eth(sender, instance, **kwargs):
    faucet_eth(instance)
    instance.state = True
