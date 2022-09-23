from django.db import models

# Create your models here.
class ScrappedData(models.Model):
    name = models.TextField(max_length=100, blank=False, primary_key=True)
    price = models.TextField(max_length=100, blank=True, default="")
    perc_1h = models.TextField(max_length=100, blank=True, default="")
    perc_24h = models.TextField(max_length=100, blank=True, default="")
    perc_7d = models.TextField(max_length=100, blank=True, default="")
    market_cap = models.TextField(max_length=100, blank=True, default="")
    volume_24h = models.TextField(max_length=100, blank=True, default="")
    circulating_supply = models.TextField(max_length=100, blank=True, default="")

    def __str__(self):
        return self.name
    
    @classmethod
    def create_or_update(cls, data):
        name = data["name"]
        cls.objects.update_or_create(
            name=name,
            defaults=data,
        )

