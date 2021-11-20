from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView

from faucet.models import FaucetRequests


class FaucetRequestsView(SuccessMessageMixin, CreateView):
    success_url = '/'
    success_message = "Запрос на добавление принят"
    model = FaucetRequests
    fields = ['address', 'value']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        req = FaucetRequests.objects.filter(state=False)
        context['request_list'] = req
        context['queue_size'] = len(req)

        return context
