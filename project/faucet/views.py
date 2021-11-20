from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView

from faucet.models import FaucetRequests

from django.apps import apps


class FaucetRequestsView(SuccessMessageMixin, CreateView):
    success_url = '/'
    success_message = "Запрос на добавление принят"
    model = FaucetRequests
    fields = ['address', 'value']

    def get_context_data(self, **kwargs):
        web3 = apps.get_app_config('faucet').web3
        if web3 == 'Fail':
            status = False
        else:
            status = web3.isConnected()

        if not status:
            messages.error(self.request, 'Sorry, service unavailable!')

        context = super().get_context_data(**kwargs)
        req = FaucetRequests.objects.filter(state=False)
        context['request_list'] = req
        context['queue_size'] = len(req)
        context['service_status'] = status

        return context
