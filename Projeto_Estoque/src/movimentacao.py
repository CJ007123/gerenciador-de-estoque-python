from dataclasses import dataclass,field
from datetime import datetime
from validacoes import EstadoDoProduto,Validador
from produtos import Produtos

@dataclass
class Movimentacao:
    produto: Produtos
    tipo: EstadoDoProduto
    quantidade_registros: int
    data: datetime


@dataclass
class GerenciandoMovimentacao:
    movimentacao: list = field(default_factory=list)

    def registrar_movimentacao(self,movimentacao:Movimentacao):
        Validador.validar_instancia_na_lista(movimentacao, Movimentacao)
        Validador.validar_valores_duplicados(self.movimentacao, 'produto', movimentacao.produto, 'movimentacao')
        self.movimentacao.append(movimentacao)
        print(f'Registrando movimentação do produto {movimentacao.produto}')
    
    def listar_movimentacao(self):
        Validador.validar_lista(self.movimentacao, 'movimentacao')
        resultado = []
        for movimentacao in self.movimentacao:
            resultado.append(f'Produto:{movimentacao.produto}\nTipo: {movimentacao.tipo}\nQuantidade de registros: {movimentacao.quantidade_registros} Data: {movimentacao.data}\n')
        return resultado
    

    def atualizar_entrada_saida(self,movimentacao,atualizando_tipo: EstadoDoProduto):
        if not isinstance(atualizando_tipo, EstadoDoProduto):
            raise TypeError("Tipo de movimentação inválido. Use TipoMovimentacao.ENTRADA ou TipoMovimentacao.SAIDA.")
        movimentacao.tipo = atualizando_tipo
        return movimentacao.tipo
        # print(f'Estado foi atualizado para: {movimentacao.tipo.value}')

    
    def atualizar_quantidade_de_registros(self, quantidade_atual: int, nova_quantidade: int):
        if not self.movimentacao:
            print(f'Essa quantidade {quantidade_atual} não foi inserida')
        
        Validador.validar_int(quantidade_atual, 'Quantidade atual')
        Validador.validar_int(nova_quantidade, 'Nova Quantidade')
        
        for quantidade in self.movimentacao:
            if quantidade.quantidade_registros == quantidade_atual:
                quantidade.quantidade_registros = nova_quantidade
                print(f'Quantidade de registro foi atualizada para: {nova_quantidade} registros')


    def remover_movimentacao(self, remover: Movimentacao):
        if remover not in self.movimentacao:
            print(f'O produto {remover} não existe no estoque')
            return
        self.movimentacao.remove(remover)
        print(f'O registro {remover.produto} foi removido')
        return remover.produto
