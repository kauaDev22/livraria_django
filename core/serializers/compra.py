from cfgv import ValidationError
from rest_framework.fields import DateTimeField
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import CharField, ModelSerializer
from core.models import Compra, ItensCompra
from core.models import Compra
from rest_framework.serializers import CharField, ModelSerializer, SerializerMethodField, CurrentUserDefault, HiddenField 


class ItensCompraListSerializer(ModelSerializer):
    livro = CharField(source="livro.titulo", read_only=True)

    class Meta:
        model = ItensCompra
        fields = ("quantidade", "livro")
        depth = 1


class CompraListSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True)
    itens = ItensCompraListSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = ("id", "usuario", "itens")


class ItensCompraCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ("livro", "quantidade")
    def validate_quantidade(self, quantidade):
        if quantidade <= 0:
            raise ValidationError("A quantidade deve ser maior do que zero.")
        return quantidade
    def validate(self, item):
        if item["quantidade"] > item["livro"].quantidade:
            raise ValidationError("Quantidade de itens maior do que a quantidade em estoque.")
        return item 

    

class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    def get_total(self, instance):
        return instance.livro.preco * instance.quantidade
    class Meta:
        model = ItensCompra
        fields = ("livro", "quantidade", "total")
        depth = 1


class CompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True) # inclua essa linha
    status = CharField(source="get_status_display", read_only=True)
    data = DateTimeField(read_only=True) # inclua essa linha
    tipo_pagamento = CharField(source="get_tipo_pagamento_display", read_only=True)
    itens = ItensCompraSerializer(many=True, read_only=True)
    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "total", "itens","tipo_pagamento", "data")


class CompraCreateUpdateSerializer(ModelSerializer):
    usuario = HiddenField(default=CurrentUserDefault())
    itens = ItensCompraCreateUpdateSerializer(many=True)

    def create(self, validated_data):
        itens = validated_data.pop("itens")
        compra = Compra.objects.create(**validated_data)
        for item in itens:
            item["preco"] = item["livro"].preco # nova linha
            ItensCompra.objects.create(compra=compra, **item)
        compra.save()
        return compra

    def update(self, compra, validated_data):
        itens = validated_data.pop("itens")
        if itens:
            compra.itens.all().delete()
            for item in itens:
                item["preco"] = item["livro"].preco  # nova linha
                ItensCompra.objects.create(compra=compra, **item)
        compra.save()
        return super().update(compra, validated_data)

    class Meta:
        model = Compra
        fields = ("usuario", "itens")

