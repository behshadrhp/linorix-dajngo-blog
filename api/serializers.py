from rest_framework import serializers
from blog.models import Essay

class EssaySerializers(serializers.ModelSerializer):
    class Meta:
        model = Essay
        fields = '__all__'