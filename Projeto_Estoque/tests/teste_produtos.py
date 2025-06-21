import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


import unittest
from produtos import *
from teste_categoria import TestBaseGerenciador

class TestProduto(TestBaseGerenciador):
    def setUp(self):
        self.p1 = Produtos(nome='Ibanez',descricao='instrumento musical' ,categoria='Musica',
                           _quantidade=50,_preco=4500.00,localizacao='Entrada03')
        self.g1 = GerenciadorDeTarefas()
    
    def test_setter_preco(self):
        """Deve permitir atribuir um valor de preço float válido ao produto."""
        self.p1.preco = 4500.00
        self.assertEqual(self.p1.preco, 4500.00)

    def test_setter_preco_str(self):
        """Deve levantar TypeError ao tentar atribuir uma string ao preço."""
        self.assert_erro_tipo(lambda: setattr(self.p1, "preco", 'asd'), "aceita apenas números de ponto flutuante")

    def test_setter_preco_int(self):
        """Deve levantar TypeError ao tentar atribuir um int ao preço (esperado float)."""
        self.assert_erro_tipo(lambda: setattr(self.p1, "preco", 4500), "aceita apenas números de ponto flutuante")

    def test_setter_preco_negativo(self):
        """Deve levantar ValueError ao atribuir um preço float negativo."""
        self.assert_erro_valor(lambda: setattr(self.p1, "preco", -5000.00), "é necessário ser número positivo")

    def test_setter_preco_none(self):
        """Deve levantar ValueError ao atribuir None ao preço."""
        self.assert_erro_valor(lambda: setattr(self.p1, "preco", None), "não pode estar vazio")

    def test_setter_preco_valor_positivo_nan(self):
        """Deve levantar ValueError ao atribuir NaN como preço."""
        self.assert_erro_valor(lambda: setattr(self.p1, "preco", float('nan')), 'não pode ser número infinito ou inválido')

    def test_setter_preco_valor_positivo_inf(self):
        """Deve levantar ValueError ao atribuir valor infinito como preço."""
        self.assert_erro_valor(lambda: setattr(self.p1, "preco", float('inf')), 'não pode ser número infinito ou inválido')



    

    
    
    def test_setter_quantidade(self):
        """Deve permitir atribuir um valor inteiro válido à quantidade."""
        self.p1.quantidade = 50
        self.assertEqual(self.p1.quantidade, 50)

    def test_setter_quantidade_none(self):
        """Deve levantar ValueError ao atribuir None como quantidade."""
        self.assert_erro_valor(lambda: setattr(self.p1, "quantidade", None), "não pode estar vazio")

    def test_setter_quantidade_negativo(self):
        """Deve levantar ValueError ao atribuir um valor negativo à quantidade."""
        self.assert_erro_valor(lambda: setattr(self.p1, "quantidade", -5), "é necessário ser número positivo")

    def test_setter_quantidade_str(self):
        """Deve levantar TypeError ao atribuir uma string como quantidade."""
        self.assert_erro_tipo(lambda: setattr(self.p1, "quantidade", 'asd'), "apenas números inteiros")

    def test_setter_quantidade_float(self):
        """Deve levantar TypeError ao atribuir um float como quantidade."""
        self.assert_erro_tipo(lambda: setattr(self.p1, "quantidade", 50.00), "apenas números inteiros")

        
        
    





    
    def test_cadastrar_produto(self):
        """Deve cadastrar corretamente um produto na lista de produtos."""
        self.g1.cadastrar_produtos(self.p1)
        self.assertIn(self.p1, self.g1.produtos)
        self.assertEqual(len(self.g1.produtos), 1)

    def test_cadastar_produto_duplicados(self):
        """Deve levantar ValueError ao tentar cadastrar um produto já existente."""
        self.g1.cadastrar_produtos(self.p1)
        duplicado = Produtos(nome='Ibanez', descricao='instrumento musical', categoria='Musica',
                             _quantidade=50, _preco=4500.00, localizacao='Entrada03')
        self.assert_erro_valor(lambda: self.g1.cadastrar_produtos(duplicado), ' já existe e não pode ser duplicado.')

    def test_produto_nao_inseridos(self):
        """Deve levantar ValueError ao tentar cadastrar algo que não seja objeto Produto."""
        with self.assertRaises(ValueError) as context:
            self.g1.cadastrar_produtos('Esse produto não existe!')
        self.assertIn('Só é permitido adicionar objetos do tipo', str(context.exception))

    def test_exibir_produtos(self):
        """Deve retornar a lista formatada dos produtos cadastrados."""
        self.g1.cadastrar_produtos(self.p1)
        resultado = self.g1.exibir_estoque()
        esperado = [f'Nome: {self.p1.nome}\nCategoria: {self.p1.categoria}\nQuantidade: {self.p1.quantidade}\nPreço: R${self.p1.preco:.2f} Localização: {self.p1.localizacao}\nDescrição: {self.p1.descricao}']
        self.assertEqual(esperado, resultado)

    def test_exibir_produto_vazio(self):
        """Deve levantar ValueError ao tentar exibir estoque vazio."""
        with self.assertRaises(ValueError) as context:
            self.g1.exibir_estoque()
        self.assertIn('Não tem nada na lista:', str(context.exception))


    
    
    def test_atualizar_estoque(self):
        """Deve atualizar corretamente a quantidade de um produto no estoque."""
        self.g1.cadastrar_produtos(self.p1)
        self.g1.atualizando_estoque(self.p1.nome, 150)
        self.assertEqual(self.p1.quantidade, 200)

    def test_atualizar_estoque_com_quantidade_negativa(self):
        """Deve levantar erro ao tentar atualizar com quantidade negativa."""
        self.g1.cadastrar_produtos(self.p1)
        self.assert_erro_valor(lambda: self.g1.atualizando_estoque(50, -10), "é necessário ser número positivo")

    def test_atualizar_estoque_com_tipo_errado_str(self):
        """Deve levantar erro ao passar uma string em vez de número inteiro."""
        self.g1.cadastrar_produtos(self.p1)
        self.assert_erro_tipo(lambda: self.g1.atualizando_estoque(50, 'asd'), "apenas números inteiros")

    def test_atualizar_estoque_com_tipo_errado_float(self):
        """Deve levantar erro ao passar um float em vez de inteiro."""
        self.g1.cadastrar_produtos(self.p1)
        self.assert_erro_tipo(lambda: self.g1.atualizando_estoque(50, 59.00), "apenas números inteiros")

    def test_atualizar_estoque_com_none(self):
        """Deve levantar erro ao passar None como quantidade."""
        self.g1.cadastrar_produtos(self.p1)
        self.assert_erro_valor(lambda: self.g1.atualizando_estoque(50, None), "não pode estar vazio")

    def test_atualizar_estoque_com_campos_incorretos(self):
        """Deve levantar erro ao passar dados de tipos incorretos nos parâmetros."""
        self.g1.cadastrar_produtos(self.p1)
        self.assert_erro_tipo(lambda: self.g1.atualizando_estoque("50", 1500.00), "apenas números inteiros")





       
    def test_atualizar_preco(self):
        """Deve atualizar corretamente o preço de um produto."""
        self.g1.cadastrar_produtos(self.p1)
        self.g1.atualizando_preco(self.p1.nome, 10000.00)
        self.assertEqual(self.p1.preco, 10000.00)

    def test_atualizar_preco_com_valor_negativo(self):
        """Deve levantar erro ao tentar atualizar com valor negativo."""
        self.g1.cadastrar_produtos(self.p1)
        self.assert_erro_valor(lambda: self.g1.atualizando_preco(4500.00, -10.00), "é necessário ser número positivo")

    def test_atualizar_preco_com_valor_tipo_str(self):
        """Deve levantar erro ao passar string em vez de float."""
        self.g1.cadastrar_produtos(self.p1)
        self.assert_erro_tipo(lambda: self.g1.atualizando_preco(4500.00, '456.00'), "aceita apenas números de ponto flutuante")

    def test_atualizar_preco_com_valor_tipo_int(self):
        """Deve levantar erro ao passar int em vez de float."""
        self.g1.cadastrar_produtos(self.p1)
        self.assert_erro_tipo(lambda: self.g1.atualizando_preco(4500.00, 5000), "aceita apenas números de ponto flutuante")

    def test_atualizar_preco_com_valor_none(self):
        """Deve levantar erro ao passar None como novo preço."""
        self.g1.cadastrar_produtos(self.p1)
        self.assert_erro_valor(lambda: self.g1.atualizando_preco(4500.00, None), "não pode estar vazio")

    def test_atualizar_preco_com_campos_errados(self):
        """Deve levantar erro ao passar campos com tipos inválidos."""
        self.g1.cadastrar_produtos(self.p1)
        self.assert_erro_tipo(lambda: self.g1.atualizando_preco(4500, 'None'), "aceita apenas números de ponto flutuante")

    def test_atualizar_preco_com_valor_nan(self):
        """Deve levantar erro ao passar NaN como preço."""
        self.assert_erro_valor(lambda: self.g1.atualizando_preco(1000.00, float('nan')), 'não pode ser número infinito ou inválido')

    def test_atualizar_preco_com_valor_infinito(self):
        """Deve levantar erro ao passar valor infinito como preço."""
        self.assert_erro_valor(lambda: self.g1.atualizando_preco(1000.00, float('inf')), 'não pode ser número infinito ou inválido')


    

    def test_atualizar_localizacao(self):
        """Deve atualizar corretamente a localização de um produto."""
        self.g1.cadastrar_produtos(self.p1)
        self.g1.atualizando_localizacao(self.p1.localizacao, 'Entrada AB')
        self.assertEqual(self.p1.localizacao, 'Entrada AB')

    def test_atualizar_localizacao_tipo_int(self):
        """Deve levantar erro ao passar valor int como nova localização."""
        self.g1.cadastrar_produtos(self.p1)
        self.assert_erro_tipo(lambda: self.g1.atualizando_localizacao('Entrada03', 5000), "precisa ser um caracter")

    def test_atualizar_localizacao_tipo_float(self):
        """Deve levantar erro ao passar valor float como nova localização."""
        self.g1.cadastrar_produtos(self.p1)
        self.assert_erro_tipo(lambda: self.g1.atualizando_localizacao('Entrada03', 5000.00), "precisa ser um caracter")

    def test_atualizar_localizacao_com_campo_vazio(self):
        """Deve levantar erro ao passar string vazia como nova localização."""
        self.g1.cadastrar_produtos(self.p1)
        self.assert_erro_valor(lambda: self.g1.atualizando_localizacao('Entrada03', ''), "não pode estar vazio")

    def test_atualizar_localizacao_com_campos_incorretos(self):
        """Deve levantar erro ao passar dois campos inválidos."""
        self.g1.cadastrar_produtos(self.p1)
        self.assert_erro_tipo(lambda: self.g1.atualizando_localizacao(5000, 456.00), "precisa ser um caracter")




        

    def test_atualizar_descricao(self):
        """Deve atualizar corretamente a descrição do produto."""
        self.g1.cadastrar_produtos(self.p1)
        self.g1.atualizando_descricao(self.p1.descricao, '6 cordas')
        self.assertEqual(self.p1.descricao, '6 cordas')

    def test_atualizar_descricao_int(self):
        """Deve levantar erro ao passar um inteiro como nova descrição."""
        self.g1.cadastrar_produtos(self.p1)
        self.assert_erro_tipo(lambda: self.g1.atualizando_descricao('instrumento musical', 5000), "precisa ser um caracter")

    def test_atualizar_descricao_float(self):
        """Deve levantar erro ao passar float como nova descrição."""
        self.g1.cadastrar_produtos(self.p1)
        self.assert_erro_tipo(lambda: self.g1.atualizando_descricao('instrumento musical', 5000.00), "precisa ser um caracter")

    def test_atualizar_descricao_com_campo_vazio(self):
        """Deve levantar erro ao passar string vazia como nova descrição."""
        self.g1.cadastrar_produtos(self.p1)
        self.assert_erro_valor(lambda: self.g1.atualizando_descricao('instrumento musical', ''), "não pode estar vazio")

    def test_atualizar_descricao_com_campo_incorretos(self):
        """Deve levantar erro ao passar tipos incorretos nos dois campos."""
        self.g1.cadastrar_produtos(self.p1)
        self.assert_erro_tipo(lambda: self.g1.atualizando_descricao(5000, 4500.00), "precisa ser um caracter")



    
    def test_remover_produto(self):
        """Removendo produtos do estoque"""
        self.g1.cadastrar_produtos(self.p1)
        remover_produto = self.g1.remover_produtos(self.p1)
        self.assertEqual(remover_produto, self.p1.nome)
        self.assertNotIn(self.p1, self.g1.produtos)





      

    def test_retirar_estoque(self):
        """Deve retirar a quantidade correta do estoque."""
        self.g1.cadastrar_produtos(self.p1)
        self.g1.retirar_quantidade_estoque(self.p1.nome, 40)
        self.assertEqual(self.p1.quantidade, 10)

    def test_retirar_estoque_com_quantidade_none(self):
        """Deve levantar erro ao tentar retirar quantidade None."""
        self.g1.cadastrar_produtos(self.p1)
        self.assert_erro_valor(lambda: self.g1.retirar_quantidade_estoque(450, None), "não pode estar vazio") 

    def test_retirar_estoque_com_quantidade_tipo_float(self):
        """Deve levantar erro ao passar float como quantidade."""
        self.g1.cadastrar_produtos(self.p1)
        self.assert_erro_tipo(lambda: self.g1.retirar_quantidade_estoque(450, 500.00), "apenas números inteiros") 

    def test_retirar_estoque_com_quantidade_tipo_str(self):
        """Deve levantar erro ao passar string como quantidade."""
        self.g1.cadastrar_produtos(self.p1)
        self.assert_erro_tipo(lambda: self.g1.retirar_quantidade_estoque(450, 'erro'), "apenas números inteiros") 

    def test_retirar_estoque_com_quantidade_valor_negativo(self):
        """Deve levantar erro ao tentar retirar quantidade negativa."""
        self.g1.cadastrar_produtos(self.p1)
        self.assert_erro_valor(lambda: self.g1.retirar_quantidade_estoque(450, -500), "é necessário ser número positivo") 



