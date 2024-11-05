from rest_framework.viewsets import ModelViewSet

from core.models import Livro
from core.serializers import LivroSerializer, LivroListRetrieveSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    def get_serializer(self):
        if self.action in ["list", "retrive"]:
            return LivroListRetrieveSerializer
        return LivroSerializer
