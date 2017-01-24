from rest_framework import mixins, viewsets

from .models import Frase  
from .serializers import FraseSerializer


class FraseViewSet(mixins.CreateModelMixin,  
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):

    queryset = Frase.objects.all()
    serializer_class = FraseSerializer