from dataclasses import dataclass, field
from datetime import datetime
from validacoes import EstadoDoProduto, Validador
from produtos import Produtos

@dataclass
class Movimentacao:
    """
    Representa uma movimentação de entrada ou saída de um produto no estoque.

    Atributos:
        produto (Produtos): Produto relacionado à movimentação.
        tipo (EstadoDoProduto): Tipo da movimentação (Entrada ou Saída).
        quantidade_registros (int): Quantidade de itens movimentados.
        data (datetime): Data e hora da movimentação.
    """
    produto: Produtos
    tipo: EstadoDoProduto
    quantidade_registros: int
    data: datetime


@dataclass
class GerenciandoMovimentacao:
    """
    Gerencia todas as movimentações de produtos, incluindo registros, atualizações e remoções.

    Atributos:
        movimentacao (list): Lista de objetos do tipo Movimentacao.
    """
    movimentacao: list = field(default_factory=list)

    def registrar_movimentacao(self, movimentacao: Movimentacao):
        """
        Registra uma nova movimentação após validações de tipo e duplicidade.

        Args:
            movimentacao (Movimentacao): A movimentação a ser registrada.

        Raises:
            TypeError: Se o objeto não for uma instância de Movimentacao.
            ValueError: Se já existir movimentação do mesmo produto.
        """
        Validador.validar_instancia_na_lista(movimentacao, Movimentacao)
        Validador.validar_valores_duplicados(self.movimentacao, 'produto', movimentacao.produto, 'movimentacao')
        self.movimentacao.append(movimentacao)
        print(f'Registrando movimentação do produto {movimentacao.produto}')

    def listar_movimentacao(self):
        """
        Lista todas as movimentações registradas.

        Returns:
            list: Lista de strings com os dados das movimentações.

        Raises:
            ValueError: Se a lista de movimentações estiver vazia.
        """
        Validador.validar_lista(self.movimentacao, 'movimentacao')
        resultado = []
        for movimentacao in self.movimentacao:
            resultado.append(f'Produto:{movimentacao.produto}\nTipo: {movimentacao.tipo}\nQuantidade de registros: {movimentacao.quantidade_registros} Data: {movimentacao.data}\n')
        return resultado

    def atualizar_entrada_saida(self, movimentacao, atualizando_tipo: EstadoDoProduto):
        """
        Atualiza o tipo de movimentação (Entrada/Saída) de um registro.

        Args:
            movimentacao (Movimentacao): Objeto a ser atualizado.
            atualizando_tipo (EstadoDoProduto): Novo tipo de movimentação.

        Returns:
            EstadoDoProduto: Tipo atualizado.

        Raises:
            TypeError: Se o tipo informado não for uma instância de EstadoDoProduto.
        """
        if not isinstance(atualizando_tipo, EstadoDoProduto):
            raise TypeError("Tipo de movimentação inválido. Use EstadoDoProduto.Entrada ou EstadoDoProduto.Saida.")
        movimentacao.tipo = atualizando_tipo
        print(f'Estado foi atualizado para: {movimentacao.tipo.value}')
        return movimentacao.tipo

    def atualizar_quantidade_de_registros(self, quantidade_atual: int, nova_quantidade: int):
        """
        Atualiza a quantidade de registros de uma movimentação específica.

        Args:
            quantidade_atual (int): Valor atual da quantidade.
            nova_quantidade (int): Novo valor a ser atribuído.

        Raises:
            ValueError ou TypeError: Se os valores não forem válidos.
        """
        if not self.movimentacao:
            print(f'Essa quantidade {quantidade_atual} não foi inserida')

        Validador.validar_int(quantidade_atual, 'Quantidade atual')
        Validador.validar_int(nova_quantidade, 'Nova Quantidade')
        
        for quantidade in self.movimentacao:
            if quantidade.quantidade_registros == quantidade_atual:
                quantidade.quantidade_registros = nova_quantidade
                print(f'Quantidade de registro foi atualizada para: {nova_quantidade} registros')

    def remover_movimentacao(self, remover: Movimentacao):
        """
        Remove uma movimentação do sistema.

        Args:
            remover (Movimentacao): A movimentação a ser removida.

        Returns:
            Produtos: Produto referente à movimentação removida.

        Observação:
            Se a movimentação não existir, apenas exibe uma mensagem.
        """
        if remover not in self.movimentacao:
            print(f'O produto {remover} não existe no estoque')
            return
        self.movimentacao.remove(remover)
        print(f'O registro {remover.produto} foi removido')
        return remover.produto
