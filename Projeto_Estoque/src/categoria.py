from dataclasses import dataclass,field
from validacoes import Validador


@dataclass
class InformacoesDoProduto:
    """
    Classe base que representa informações comuns de um produto ou categoria.

    Atributos:
        nome (str): Nome do produto ou categoria.
        descricao (str): Descrição do produto ou categoria.
    """
    nome: str
    descricao: str

@dataclass
class Categoria(InformacoesDoProduto):
    """
    Representa uma categoria de produto.

    Herda:
        InformacoesDoProduto: Contém os atributos 'nome' e 'descricao'.
    """
    pass

@dataclass
class GerenciadorDeCategoria:
    """
    Gerencia uma lista de categorias, permitindo adicionar, exibir, atualizar e remover categorias.

    Atributos:
        categorias (list): Lista de objetos da classe Categoria.
    """
    categorias: list = field(default_factory=list)

    def adicionar_categoria(self, categoria: Categoria):
        """
        Adiciona uma nova categoria à lista, validando tipo e duplicidade.

        Args:
            categoria (Categoria): A categoria a ser adicionada.

        Raises:
            TypeError: Se o objeto não for do tipo Categoria.
            ValueError: Se a categoria já existir na lista.
        """
        Validador.validar_instancia_na_lista(categoria, Categoria)
        Validador.validar_valores_duplicados(self.categorias, 'nome', categoria.nome, 'categoria')
        self.categorias.append(categoria)
        print(f'Adicionando categoria {categoria.nome} na lista')

    def exibir_categoria(self):
        """
        Retorna a lista formatada com todas as categorias cadastradas.

        Returns:
            list: Lista de strings com o nome e descrição de cada categoria.

        Raises:
            ValueError: Se a lista de categorias estiver vazia.
        """
        Validador.validar_lista(self.categorias, 'categorias')
        resultado = []
        for exibir in self.categorias:
            resultado.append(f'Categoria: {exibir.nome}\nDescrição: {exibir.descricao}')
        return resultado

    def atualizar_categoria(self, categoria_atual: str, categoria_nova: str):
        """
        Atualiza o nome de uma categoria existente.

        Args:
            categoria_atual (str): Nome atual da categoria.
            categoria_nova (str): Novo nome da categoria.

        Raises:
            ValueError: Se os campos forem vazios.
        """
        Validador.validar_str_campo_vazio(categoria_atual, 'Categoria Atual')
        Validador.validar_str_campo_vazio(categoria_nova, 'Nova categoria')

        if not self.categorias:
            print(f'A categoria {categoria_atual} não existe')

        for categoria in self.categorias:
            if categoria.nome == categoria_atual:
                categoria.nome = categoria_nova
                print(f'Categoria {categoria_atual} foi atualizada para: {categoria_nova}')

    def atualizar_descricao(self, descricao_atual: str, descricao_nova: str):
        """
        Atualiza a descrição de uma categoria existente.

        Args:
            descricao_atual (str): Descrição atual da categoria.
            descricao_nova (str): Nova descrição a ser atribuída.

        Raises:
            ValueError: Se os campos forem vazios.
        """
        Validador.validar_str_campo_vazio(descricao_atual, 'Descrição atual')
        Validador.validar_str_campo_vazio(descricao_nova, 'Nova Descrição')

        if not self.categorias:
            print(f'A descrição {descricao_atual} não existe')

        for categoria in self.categorias:
            if categoria.descricao == descricao_atual:
                categoria.descricao = descricao_nova
                print(f'Descrição {descricao_atual} foi atualizada para: {descricao_nova}')

    def remover_categoria(self, remover: Categoria):
        """
        Remove uma categoria da lista, se ela existir.

        Args:
            remover (Categoria): A categoria a ser removida.

        Returns:
            str: O nome da categoria removida, caso tenha sido encontrada.
        """
        if remover not in self.categorias:
            print(f'A categoria {remover.nome} não existe.')
            return
        self.categorias.remove(remover)
        print(f'Categoria {remover.nome} foi removido')
        return remover.nome
