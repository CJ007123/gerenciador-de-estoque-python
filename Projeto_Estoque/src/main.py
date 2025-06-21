from categoria import Categoria, GerenciadorDeCategoria
from produtos import Produtos, GerenciadorDeTarefas
from movimentacao import Movimentacao, GerenciandoMovimentacao
from validacoes import EstadoDoProduto
from datetime import datetime

def main():
    print("Sistema de Estoque")

    # Criando Gerenciadores
    gerenciador_categoria = GerenciadorDeCategoria()
    gerenciador_produto = GerenciadorDeTarefas()
    gerenciador_movimentacao = GerenciandoMovimentacao()

    # Adicionando Categoria
    categoria = Categoria(nome="Instrumentos", descricao="Instrumentos musicais")
    gerenciador_categoria.adicionar_categoria(categoria)

    # Criando Produto
    produto = Produtos(
        nome="Guitarra Gibson",
        descricao=categoria.descricao,
        categoria=categoria.nome,
        _quantidade=20,
        _preco=4500.00,
        localizacao="Estante A"
    )
    gerenciador_produto.cadastrar_produtos(produto)

    # Atualizando Estoque
    gerenciador_produto.atualizando_estoque(produto.nome, 5)

    # Atualizando Preço
    gerenciador_produto.atualizando_preco(produto.nome, 4700.00)

    # Registrando Movimentação
    movimentacao = Movimentacao(
        produto=produto.nome,
        tipo=EstadoDoProduto.Entrada.value,
        quantidade_registros=5,
        data=datetime.now()
    )
    gerenciador_movimentacao.registrar_movimentacao(movimentacao)

    # Exibindo Resultados
    print("\n📂 Categorias:")
    for linha in gerenciador_categoria.exibir_categoria():
        print(linha)

    print("\n📦 Estoque:")
    for linha in gerenciador_produto.exibir_estoque():
        print(linha)

    print("\n🔁 Movimentações:")
    for linha in gerenciador_movimentacao.listar_movimentacao():
        print(linha)

if __name__ == "__main__":
    main()
