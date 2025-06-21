from dataclasses import dataclass, field
from validacoes import Validador
from categoria import InformacoesDoProduto, Categoria, GerenciadorDeCategoria

@dataclass
class Produtos(InformacoesDoProduto):
    """
    Representa um produto no estoque com informações de categoria, quantidade, preço e localização.

    Herda:
        InformacoesDoProduto: Atributos nome e descricao.

    Atributos:
        categoria (Categoria): Categoria do produto.
        _quantidade (int): Quantidade disponível no estoque (acessado via propriedade).
        _preco (float): Preço do produto (acessado via propriedade).
        localizacao (str): Local onde o produto está armazenado.
    """

    categoria: Categoria
    _quantidade: int 
    _preco: float
    localizacao: str

    @property
    def preco(self):
        """Retorna o preço do produto."""
        return self._preco
    
    @preco.setter
    def preco(self, valor: float):
        """Define um novo valor para o preço do produto, com validação."""
        Validador.validar_float(valor, 'Preço')
        self._preco = valor
    
    @property 
    def quantidade(self):
        """Retorna a quantidade disponível do produto no estoque."""
        return self._quantidade
    
    @quantidade.setter
    def quantidade(self, valor: int):
        """Define uma nova quantidade para o produto, com validação."""
        Validador.validar_int(valor, 'Quantidade')
        self._quantidade = valor


@dataclass
class GerenciadorDeTarefas:
    """
    Gerencia uma lista de produtos no estoque, permitindo cadastro, visualização, atualização e remoção.

    Atributos:
        produtos (list): Lista de objetos do tipo Produtos.
    """

    produtos: list = field(default_factory=list)

    def cadastrar_produtos(self, produto: Produtos):
        """
        Adiciona um novo produto ao estoque após validações.

        Args:
            produto (Produtos): Produto a ser adicionado.

        Raises:
            TypeError: Se não for uma instância de Produtos.
            ValueError: Se o nome do produto já existir.
        """
        Validador.validar_instancia_na_lista(produto, Produtos)
        Validador.validar_valores_duplicados(self.produtos, 'nome', produto.nome, 'produto')
        self.produtos.append(produto)
        print(f'O produto {produto.nome} foi adicionado no estoque')

    def exibir_estoque(self):
        """
        Retorna uma lista formatada com informações dos produtos cadastrados.

        Returns:
            list: Lista de strings com os dados de cada produto.

        Raises:
            ValueError: Se a lista de produtos estiver vazia.
        """
        Validador.validar_lista(self.produtos, 'produtos')
        resultado = []
        for exibir in self.produtos:
            resultado.append(
                f'Nome: {exibir.nome}\nCategoria: {exibir.categoria}\nQuantidade: {exibir.quantidade}'
                f'\nPreço: R${exibir.preco:.2f} Localização: {exibir.localizacao}\nDescrição: {exibir.descricao}'
            )
        return resultado

    def atualizando_estoque(self, nome_produto: str, quantidade: int):
        """
        Aumenta a quantidade de um produto específico no estoque.

        Args:
            nome_produto (str): Nome do produto.
            quantidade (int): Quantidade a ser adicionada.

        Raises:
            ValueError: Se o produto não for encontrado.
        """
        Validador.validar_int(quantidade, 'Quantidade')
        Validador.validar_str_campo_vazio(nome_produto, 'Nome do Produto')
        
        add_produto = [p for p in self.produtos if p.nome == nome_produto]
          
        if not add_produto:
            raise ValueError('Esse produto não está no estoque.')
             
        for produto in add_produto:
            produto.quantidade += quantidade
            print(f'A quantidade do produto: {nome_produto} foi atualizada para: {produto.quantidade} Unidades')

    def atualizando_preco(self, nome_produto: str, novo_preco: float):
        """
        Atualiza o preço de um produto no estoque.

        Args:
            nome_produto (str): Nome do produto.
            novo_preco (float): Novo preço a ser atribuído.
        """
        if not self.produtos:
            print(f'O produto {nome_produto} não está no estoque')

        Validador.validar_float(novo_preco, 'Novo preço')
        Validador.validar_str_campo_vazio(nome_produto, 'Nome do produto')
              
        for produto in self.produtos:
            if produto.nome == nome_produto:
                produto.preco = novo_preco
                print(f'O preço do produto: {produto.nome} foi atualizado para: R${novo_preco:.2f}')

    def atualizando_localizacao(self, localizacao_atual: str, localizacao_nova: str):
        """
        Atualiza a localização de um produto no estoque.

        Args:
            localizacao_atual (str): Localização atual.
            localizacao_nova (str): Nova localização.
        """
        if not self.produtos:
            print(f'O produto {localizacao_atual} não está no estoque')
        
        Validador.validar_str_campo_vazio(localizacao_atual, 'Localização atual')
        Validador.validar_str_campo_vazio(localizacao_nova, 'Nova Localização')
        
        for produto in self.produtos:
            if produto.localizacao == localizacao_atual:
                produto.localizacao = localizacao_nova
                print(f'Localização do produto: {produto.nome} foi atualizada para: {localizacao_nova}')

    def atualizando_descricao(self, descricao_atual: str, descricao_nova: str):
        """
        Atualiza a descrição de um produto no estoque.

        Args:
            descricao_atual (str): Descrição atual.
            descricao_nova (str): Nova descrição.
        """
        if not self.produtos:
            print(f'O produto {descricao_atual} não está no estoque')
        
        Validador.validar_str_campo_vazio(descricao_atual, 'Descrição atual')
        Validador.validar_str_campo_vazio(descricao_nova, 'Nova descrição')

        for descricao in self.produtos:
            if descricao.descricao == descricao_atual:
                descricao.descricao = descricao_nova
                print(f'Descrição do produto: {descricao.nome} foi atualizada para: {descricao_nova}')

    def remover_produtos(self, remover: Produtos):
        """
        Remove um produto do estoque.

        Args:
            remover (Produtos): Produto a ser removido.

        Returns:
            str: Nome do produto removido, caso exista.
        """
        if remover not in self.produtos:
            print(f'O produto {remover} não existe no estoque')
            return
        self.produtos.remove(remover)
        print(f'Produto {remover.nome} foi removido do estoque')
        return remover.nome

    def retirar_quantidade_estoque(self, nome_produto: str, quantidade: int):
        """
        Retira uma quantidade de um produto do estoque.

        Args:
            nome_produto (str): Nome do produto.
            quantidade (int): Quantidade a ser retirada.

        Raises:
            ValueError: Se a quantidade for maior do que o disponível ou produto não existir.
        """
        Validador.validar_int(quantidade, 'Quantidade')
        Validador.validar_str_campo_vazio(nome_produto, 'Nome do produto')
        
        diminuir_produto = [p for p in self.produtos if p.nome == nome_produto]
        
        if not diminuir_produto:
            raise ValueError('Esse produto não está no estoque.')
             
        for produto in diminuir_produto:
            if produto.quantidade < quantidade:
                raise ValueError('Não é possível retirar uma quantidade maior que o estoque disponível.')
            produto.quantidade -= quantidade
            print(f'A quantidade do produto {produto.nome} foi retirada! Estoque atual: {produto.quantidade}')
