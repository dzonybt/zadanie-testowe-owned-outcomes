from rest_framework import serializers

from .models import Frase, Url


class FraseSerializer(serializers.HyperlinkedModelSerializer):  
    result = serializers.SerializerMethodField()

    class Meta:
        model = Frase
        fields = ('frase', 'result', 'pages')

    def get_result(self, obj):
        urls = Url.objects.all().filter(frase_key=obj)
        frase_result = []
        for url in urls:
            frase_result.append(url.url)

        return frase_result