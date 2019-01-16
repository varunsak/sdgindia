from rest_framework import serializers
from .models import PortData


class DataSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = PortData
        fields = (
            'id', 'product', 'quantity', 'unit', 'item_rate_inv', 'currency', 'total_amount', 'fob_inr', 'item_rate_inr', 'fob_usd', 'foreign_port', 'foreign_country', 'india_port', 'india_company',
            'foreign_company', 'invoice_number', 'hs_code'
        )
