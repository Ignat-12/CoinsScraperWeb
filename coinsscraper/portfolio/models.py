from django.db import models

class Portfolio(models.Model):
    name = models.CharField(max_length=255)
    own_wallet = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Asset(models.Model):
    portfolio = models.ForeignKey(
        Portfolio,
        related_name="assets",
        on_delete=models.CASCADE,
    )

    cryptocurrency_id = models.IntegerField()
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=20)

    amount = models.FloatField()
    current_price = models.FloatField()
    holdings_value = models.FloatField()

    pl_value = models.FloatField()
    pl_percent_value = models.FloatField()

    last_updated = models.DateTimeField()

    def __str__(self):
        return f"{self.name} ({self.symbol})"
