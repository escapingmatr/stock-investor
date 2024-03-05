from rest_framework import serializers

# This is a simple serializer for demonstration. Adjust according to your needs.
class StockCodeSerializer(serializers.Serializer):
    stock_code = serializers.CharField(max_length=10)
