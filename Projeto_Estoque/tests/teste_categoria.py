import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


import unittest
from categoria import *


class TestBaseGerenciador(unittest.TestCase):
    def assert_erro_tipo(self, funcao, mensagem_esperada, *args):
        with self.assertRaises(TypeError) as context:
            funcao(*args)
        self.assertIn(mensagem_esperada, str(context.exception))

    def assert_erro_valor(self, funcao, mensagem_esperada,*args):
        with self.assertRaises(ValueError) as context:
            funcao(*args)
        self.assertIn(mensagem_esperada, str(context.exception))



class TestCategoria(TestBaseGerenciador):
    def setUp(self):
        self.c1 = Categoria(nome='Instrumental', descricao='instrumento musical')
        self.gc = GerenciadorDeCategoria()
    
    def test_adicionar_categoria(self):
        self.gc.adicionar_categoria(self.c1)
        self.assertIn(self.c1, self.gc.categorias)
        self.assertEqual(len(self.gc.categorias), 1)
    
    def test_adicionar_categoria_duplicado(self):
        self.gc.adicionar_categoria(self.c1)
        categoria_duplicada =  Categoria(nome='Instrumental', descricao='instrumento musical')

        self.assert_erro_valor(lambda: self.gc.adicionar_categoria(categoria_duplicada), 'já existe e não pode ser duplicado.')


    
    def test_exibir_categoria(self):
        self.gc.adicionar_categoria(self.c1)
        resultado = self.gc.exibir_categoria()
        esperado = [f'Categoria: {self.c1.nome}\nDescrição: {self.c1.descricao}']
        self.assertEqual(esperado, resultado)







    def test_atualizar_descricao_categoria(self):
        self.gc.adicionar_categoria(self.c1)
        self.gc.atualizar_descricao('instrumento musical', 'Test_intrumental')
        self.assertEqual(self.c1.descricao, 'Test_intrumental')


    def test_atualizar_descricao_int_categoria(self):
        self.gc.adicionar_categoria(self.c1)
        self.assert_erro_tipo(lambda: self.gc.atualizar_categoria('instrumento musical', 5000), "Precisa ser um caracter")


    def test_atualizar_descricao_float_categoria(self):
        self.gc.adicionar_categoria(self.c1)
        self.assert_erro_tipo(lambda: self.gc.atualizar_categoria('instrumento musical', 5000.00), "Precisa ser um caracter")
 

    def test_atualizar_descricao_com_campo_vazio_categoria(self):
        self.gc.adicionar_categoria(self.c1)
        self.assert_erro_valor(lambda: self.gc.atualizar_categoria('instrumento musical', ''), "Não pode estar vazio")

    def test_atualizar_descricao_com_campo_incorreto(self):
        self.gc.adicionar_categoria(self.c1)
        self.assert_erro_tipo(lambda: self.gc.atualizar_categoria(5000, 4500.00), "Precisa ser um caracter")



    
    def test_atualizar_categoria(self):
        self.gc.adicionar_categoria(self.c1)
        self.gc.atualizar_categoria('Instrumental', 'Test_intrumento')
        self.assertEqual(self.c1.nome, 'Test_intrumento')
    
    def test_atualizar_categoria_int(self):
        self.gc.adicionar_categoria(self.c1)
        self.assert_erro_tipo(lambda: self.gc.atualizar_categoria('instrumento musical', 5000), "Precisa ser um caracter")

    def test_atualizar_categoria_float(self):
        self.gc.adicionar_categoria(self.c1)
        self.assert_erro_tipo(lambda: self.gc.atualizar_categoria('instrumento musical', 5000.00), "Precisa ser um caracter")

    def test_atualizar_categoria_com_campo_vazio(self):
        self.gc.adicionar_categoria(self.c1)
        self.assert_erro_valor(lambda: self.gc.atualizar_categoria('instrumento musical', ''), "Não pode estar vazio")

    def test_atualizar_categoria_campos_incorretos(self):
        self.gc.adicionar_categoria(self.c1)
        self.assert_erro_tipo(lambda: self.gc.atualizar_categoria(4500, 5000.00), "Precisa ser um caracter")




    
    def test_remover_categoria(self):
        self.gc.adicionar_categoria(self.c1)
        categoria_removido = self.gc.remover_categoria(self.c1)
        self.assertEqual(categoria_removido, self.c1.nome)
        self.assertNotIn(self.c1, self.gc.categorias)


