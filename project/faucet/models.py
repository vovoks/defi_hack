from django.db import models


class FaucetRequests(models.Model):
    address = models.CharField(verbose_name='Адрес', max_length=42)
    value = models.DecimalField(verbose_name='Значение', max_digits=6, decimal_places=4)
    state = models.BooleanField(verbose_name='Статус', default=False)
    time = models.DateTimeField(verbose_name='Дата/время запроса', auto_now_add=True)

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'
