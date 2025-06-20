from dataclasses import dataclass,field
from validacoes import Validador


@dataclass
class InformacoesDoProduto:
    nome: str
    descricao: str
  
@dataclass
class Categoria(InformacoesDoProduto):
    pass


@dataclass
class GerenciadorDeCategoria:
    categorias: list = field(default_factory=list)

    def adicionar_categoria(self,categoria:Categoria):
        Validador.validar_instancia_na_lista(categoria, Categoria)
        Validador.validar_valores_duplicados(self.categorias, 'nome', categoria.nome, 'categoria')
        self.categorias.append(categoria)
        print(f'Adicionando categoria {categoria.nome} na lista')


    def exibir_categoria(self):
        Validador.validar_lista(self.categorias, 'categorias')
        resultado = []
        for exibir in self.categorias:
            resultado.append(f'Categoria: {exibir.nome}\nDescrição: {exibir.descricao}')
        return resultado
    

    def atualizar_categoria(self,categoria_atual:str, categoria_nova:str):
        Validador.validar_str_campo_vazio(categoria_atual, 'Categoria Atual')
        Validador.validar_str_campo_vazio(categoria_nova, 'Nova categoria')

        if not self.categorias:
            print(f'A categoria {categoria_atual} não existe')
        
        for categoria in self.categorias:
            if categoria.nome == categoria_atual:
                categoria.nome = categoria_nova
                print(f'Categoria {categoria_atual} foi atualizada para: {categoria_nova}')


    def atualizar_descricao(self,descricao_atual:str, descricao_nova:str):
        Validador.validar_str_campo_vazio(descricao_atual,'Descrição atual')
        Validador.validar_str_campo_vazio(descricao_nova, 'Nova Descrição')

        if not self.categorias:
            print(f'A descrição {descricao_atual} não existe')
        
        for categoria in self.categorias:
            if categoria.descricao == descricao_atual:
                categoria.descricao = descricao_nova
                print(f'Descrição {descricao_atual} foi atualizada para: {descricao_nova}')

    
    def remover_categoria(self,remover:Categoria):
        if remover not in self.categorias:
            print(f'A categoria {remover.nome} não existe.')
            return
        self.categorias.remove(remover)
        print(f'Categoria {remover.nome} foi removido')
        return remover.nome
    