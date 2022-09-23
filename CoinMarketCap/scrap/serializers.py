from rest_framework import serializers
from .models import ScrappedData

class ScrappedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrappedData
        fields = ["name", "price", "perc_1h", "perc_24h", "perc_7d", "market_cap", "volume_24h", "circulating_supply"]