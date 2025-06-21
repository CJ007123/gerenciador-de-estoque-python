import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


import unittest
from categoria import *

class TestBaseGerenciador(unittest.TestCase):
    """Classe base com métodos utilitários para verificar erros de tipo e valor em testes."""

    def assert_erro_tipo(self, funcao, mensagem_esperada, *args):
        """
        Verifica se uma função lança um TypeError com a mensagem esperada.
        """
        with self.assertRaises(TypeError) as context:
            funcao(*args)
        self.assertIn(mensagem_esperada, str(context.exception))


    def assert_erro_valor(self, funcao, mensagem_esperada, *args):
        """
        Verifica se uma função lança um ValueError com a mensagem esperada.
        """
        with self.assertRaises(ValueError) as context:
            funcao(*args)
        self.assertIn(mensagem_esperada, str(context.exception))


class TestCategoria(TestBaseGerenciador):
    """Testa funcionalidades da classe GerenciadorDeCategoria."""

    def setUp(self):
        """Configuração inicial com uma categoria padrão."""
        self.c1 = Categoria(nome='Instrumental', descricao='instrumento musical')
        self.gc = GerenciadorDeCategoria()

    def test_adicionar_categoria(self):
        """Verifica se uma nova categoria é adicionada corretamente à lista."""
        self.gc.adicionar_categoria(self.c1)
        self.assertIn(self.c1, self.gc.categorias)
        self.assertEqual(len(self.gc.categorias), 1)

    def test_adicionar_categoria_duplicado(self):
        """Testa se o sistema impede a adição de uma categoria duplicada pelo nome."""
        self.gc.adicionar_categoria(self.c1)
        categoria_duplicada = Categoria(nome='Instrumental', descricao='instrumento musical')
        self.assert_erro_valor(lambda: self.gc.adicionar_categoria(categoria_duplicada),
                               'já existe e não pode ser duplicado.')

    def test_exibir_categoria(self):
        """Testa a exibição formatada das categorias cadastradas."""
        self.gc.adicionar_categoria(self.c1)
        resultado = self.gc.exibir_categoria()
        esperado = [f'Categoria: {self.c1.nome}\nDescrição: {self.c1.descricao}']
        self.assertEqual(esperado, resultado)







    def test_atualizar_descricao_categoria(self):
        """Testa a atualização da descrição de uma categoria existente."""
        self.gc.adicionar_categoria(self.c1)
        self.gc.atualizar_descricao('instrumento musical', 'Test_intrumental')
        self.assertEqual(self.c1.descricao, 'Test_intrumental')

    def test_atualizar_descricao_int_categoria(self):
        """Testa erro ao atualizar descrição com tipo inteiro."""
        self.gc.adicionar_categoria(self.c1)
        self.assert_erro_tipo(lambda: self.gc.atualizar_categoria('instrumento musical', 5000),
                              "precisa ser um caracter")

    def test_atualizar_descricao_float_categoria(self):
        """Testa erro ao atualizar descrição com tipo float."""
        self.gc.adicionar_categoria(self.c1)
        self.assert_erro_tipo(lambda: self.gc.atualizar_categoria('instrumento musical', 5000.00),
                              "precisa ser um caracter")

    def test_atualizar_descricao_com_campo_vazio_categoria(self):
        """Testa erro ao passar string vazia para nova descrição."""
        self.gc.adicionar_categoria(self.c1)
        self.assert_erro_valor(lambda: self.gc.atualizar_categoria('instrumento musical', ''),
                               "não pode estar vazio")

    def test_atualizar_descricao_com_campo_incorreto(self):
        """Testa erro ao passar tipos incorretos para descrição."""
        self.gc.adicionar_categoria(self.c1)
        self.assert_erro_tipo(lambda: self.gc.atualizar_categoria(5000, 4500.00),
                              "precisa ser um caracter")








    def test_atualizar_categoria(self):
        """Testa a atualização do nome da categoria."""

        self.gc.adicionar_categoria(self.c1)
        self.gc.atualizar_categoria('Instrumental', 'Test_intrumento')
        self.assertEqual(self.c1.nome, 'Test_intrumento')

    def test_atualizar_categoria_int(self):
        """Testa erro ao atualizar nome da categoria com valor inteiro."""
        self.gc.adicionar_categoria(self.c1)
        self.assert_erro_tipo(lambda: self.gc.atualizar_categoria('instrumento musical', 5000),
                              "precisa ser um caracter")

    def test_atualizar_categoria_float(self):
        """Testa erro ao atualizar nome da categoria com valor float."""
        self.gc.adicionar_categoria(self.c1)
        self.assert_erro_tipo(lambda: self.gc.atualizar_categoria('instrumento musical', 5000.00),
                              "precisa ser um caracter")

    def test_atualizar_categoria_com_campo_vazio(self):
        """Testa erro ao atualizar categoria com campo vazio."""
        self.gc.adicionar_categoria(self.c1)
        self.assert_erro_valor(lambda: self.gc.atualizar_categoria('instrumento musical', ''),
                               "não pode estar vazio")

    def test_atualizar_categoria_campos_incorretos(self):
        """Testa erro com tipos incorretos para nome da categoria."""
        self.gc.adicionar_categoria(self.c1)
        self.assert_erro_tipo(lambda: self.gc.atualizar_categoria(4500, 5000.00),
                              "precisa ser um caracter")






    def test_remover_categoria(self):
        """Testa a remoção de uma categoria da lista."""
        self.gc.adicionar_categoria(self.c1)
        categoria_removido = self.gc.remover_categoria(self.c1)
        self.assertEqual(categoria_removido, self.c1.nome)
        self.assertNotIn(self.c1, self.gc.categorias)


