from django.conf import settings
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from django.utils.timezone import now, timedelta

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
        try:
            web3 = apps.get_app_config('faucet').web3
            gwei_balance = web3.eth.get_balance(web3.eth.coinbase)
            balance = round(web3.fromWei(gwei_balance, 'ether'), 4)
        except:
            balance = "_"

        req = FaucetRequests.objects.filter(state=False)
        context['request_list'] = req
        context['queue_size'] = len(req)
        context['service_status'] = status
        context['faucet_balance'] = balance

        return context

    def form_valid(self, form):
        address_list = FaucetRequests.objects.filter(address=form.data['address']).order_by('-time')
        if address_list:
            calculate_timeout = now() - address_list[0].time
            if calculate_timeout.seconds < settings.DEFAULT_FAUCET_TIMEOUT_SEC:
                wait_time = settings.DEFAULT_FAUCET_TIMEOUT_SEC - calculate_timeout.seconds
                form.add_error(None, "Please, wait {} sec.".format(wait_time))
                return self.form_invalid(form)

        try:
            web3 = apps.get_app_config('faucet').web3
            web3.eth.get_balance(form.data['address'])
        except:
            form.add_error(None, "Incorrect address format: {}".format(form.data['address']))
            return self.form_invalid(form)

        return super().form_valid(form)
