from django.contrib import admin

from faucet.models import FaucetRequests


class FaucetAdminView(admin.ModelAdmin):
    list_display = [field.name for field in FaucetRequests._meta.fields if field.name != "id"]

admin.site.register(FaucetRequests, FaucetAdminView)