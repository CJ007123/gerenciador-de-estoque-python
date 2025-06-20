from dataclasses import dataclass,field
from validacoes import Validador
from categoria import InformacoesDoProduto, Categoria, GerenciadorDeCategoria


@dataclass
class Produtos(InformacoesDoProduto):
    categoria: Categoria
    _quantidade: int 
    _preco: float
    localizacao: str

    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self,valor:float):
        Validador.validar_float(valor,'Preço')
        self._preco = valor
    
    @property 
    def quantidade(self):
        return self._quantidade
    
    @quantidade.setter
    def quantidade(self,valor:int):
        Validador.validar_int(valor,'Quantidade')
        self._quantidade = valor
            
@dataclass
class GerenciadorDeTarefas:
    produtos: list = field(default_factory=list)

    def cadastrar_produtos(self,produto:Produtos):
        Validador.validar_instancia_na_lista(produto, Produtos)
        Validador.validar_valores_duplicados(self.produtos, 'nome', produto.nome, 'produto')
        self.produtos.append(produto)
        print(f'O produto {produto.nome} foi adicionado no estoque')
    
    def exibir_estoque(self):
        Validador.validar_lista(self.produtos, 'produtos')
        resultado = []
        for exibir in self.produtos:
            resultado.append(f'Nome: {exibir.nome}\nCategoria: {exibir.categoria}\nQuantidade: {exibir.quantidade}\nPreço: R${exibir.preco:.2f} Localização: {exibir.localizacao}\nDescrição: {exibir.descricao}')
        return resultado
    
    def atualizando_estoque(self,nome_produto:str,quantidade:int):
        Validador.validar_int(quantidade, 'Quantidade')
        Validador.validar_str_campo_vazio(nome_produto, 'Nome do Produto')
        
        add_produto = [p for p in self.produtos if p.nome == nome_produto]
          
        if not add_produto:
            raise ValueError('Esse produto não esta no estoque.')
             
        for produto in add_produto:
            produto.quantidade += quantidade
            print(f'A quantidade do produto: {nome_produto} foi atualizada para: {quantidade} Unidades')

    
    def atualizando_preco(self,nome_produto:str, novo_preco:float):
        if not self.produtos:
            print(f'O produto {nome_produto} não esta no estoque')

        Validador.validar_float(novo_preco,'Novo preço')
        Validador.validar_str_campo_vazio(nome_produto,'Nome do produto')
              
        for produto in self.produtos:
            if produto.nome == nome_produto:
                produto.preco = novo_preco
                print(f'O preço do produto: {produto.nome} foi atualizada para: R${novo_preco:.2f}')
                
                
    def atualizando_localizacao(self,localizacao_atual:str, localizacao_nova:str):
        if not self.produtos:
            print(f'O produto {localizacao_atual} não esta no estoque')
        
        Validador.validar_str_campo_vazio(localizacao_atual,'Localização atual')
        Validador.validar_str_campo_vazio(localizacao_nova,'Nova Localização')
        
        for produto in self.produtos:
            if produto.localizacao == localizacao_atual:
                produto.localizacao = localizacao_nova
                print(f'Localização do produto: {produto.nome} foi atualizada para: {localizacao_nova}')


    def atualizando_descricao(self,descricao_atual:str, descricao_nova:str):
        if not self.produtos:
            print(f'O produto {descricao_atual} não esta no estoque')
        
        Validador.validar_str_campo_vazio(descricao_atual,'Localização atual')
        Validador.validar_str_campo_vazio(descricao_nova,'Nova Localização')

        for descricao in self.produtos:
            if descricao.descricao == descricao_atual:
                descricao.descricao = descricao_nova
                print(f'Localização do produto: {descricao.nome} foi atualizada para: {descricao_nova}')


    def remover_produtos(self,remover:Produtos):
        if remover not in self.produtos:
            print(f'O produto {remover} não existe no estoque')
            return
        self.produtos.remove(remover)
        print(f'Produto {remover.nome} foi removido do estoque')
        return remover.nome
    
    def retirar_quantidade_estoque(self,nome_produto:str, quantidade:int):
        Validador.validar_int(quantidade,'Quantidade')
        Validador.validar_str_campo_vazio(nome_produto, 'Nome do produto')
        
        
        diminuir_produto = [p for p in self.produtos if p.nome == nome_produto]
        
        if not diminuir_produto:
            raise ValueError('Esse produto não esta no estoque.')
             
        for produto in diminuir_produto:
            if produto.quantidade < quantidade:
                raise ValueError(f'Não é possível retirar uma quantidade maior que o estoque disponível.')
            produto.quantidade -= quantidade
            print(f'A quantidade do produto {produto.nome} foi retirado! Estoque atual {produto.quantidade}')


