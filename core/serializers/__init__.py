from .user import UserSerializer
from .categoria import CategoriaSerializer

from .editora import EditoraSerializer
from .autor import AutorSerializer
from .livro import LivroListRetrieveSerializer, LivroSerializer
from .compra import (
    CompraCreateUpdateSerializer,
    CompraSerializer,
    ItensCompraSerializer,
    CompraListSerializer, # novo
    ItensCompraListSerializer, # novo
)