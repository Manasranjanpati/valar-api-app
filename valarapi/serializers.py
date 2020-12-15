from rest_framework import serializers
from .models import Quote

class QuoteSerializer(serializers.ModelSerializer):
	# user = serializers.SlugRelatedField(slug_field='username')
    class Meta:
        model=Quote
        fields = ('id', 'quote', 'author', 'created', 'rating')