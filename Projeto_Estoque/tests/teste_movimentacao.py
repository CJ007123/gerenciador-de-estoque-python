import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


import unittest
from movimentacao import *
from validacoes import EstadoDoProduto
from teste_categoria import TestBaseGerenciador
from datetime import datetime



class TestMovimentacao(TestBaseGerenciador):
    def setUp(self):
        """Configura os dados iniciais para cada teste."""
        self.m1 = Movimentacao(produto='nome', tipo=EstadoDoProduto.Entrada.value, quantidade_registros=10, data=datetime.now())
        self.gm = GerenciandoMovimentacao()

    def test_adicionando_movimentacao(self):
        """Testa se uma movimentação válida é registrada corretamente."""
        self.gm.registrar_movimentacao(self.m1)
        self.assertIn(self.m1, self.gm.movimentacao)
        self.assertEqual(len(self.gm.movimentacao), 1)

    def test_adicionando_movimentacao_duplicadas(self):
        """Testa se o sistema impede o registro de movimentações duplicadas."""
        self.gm.registrar_movimentacao(self.m1)
        duplicada = Movimentacao(produto='nome', tipo=EstadoDoProduto.Entrada.value, quantidade_registros=10, data=datetime.now())
        self.assert_erro_valor(lambda: self.gm.registrar_movimentacao(duplicada), 'já existe e não pode ser duplicado.')





    def test_listar_movimentacao(self):
        """Testa a listagem formatada de movimentações registradas."""
        self.gm.registrar_movimentacao(self.m1)
        resultado = self.gm.listar_movimentacao()
        esperado = [f'Produto:{self.m1.produto}\nTipo: {self.m1.tipo}\nQuantidade de registros: {self.m1.quantidade_registros} Data: {self.m1.data}\n']
        self.assertEqual(esperado, resultado)







    def test_atualizar_quantidade_registros(self):
        """Testa a atualização correta da quantidade de registros de uma movimentação."""
        self.gm.registrar_movimentacao(self.m1)
        self.gm.atualizar_quantidade_de_registros(10, 100)
        self.assertEqual(self.m1.quantidade_registros, 100)

    def atualizar_quantidade_registros_float(self):
        """Testa se ocorre erro ao atualizar com valor float inválido."""
        self.gm.registrar_movimentacao(self.m1)
        self.assert_erro_tipo(lambda: self.gm.atualizar_quantidade_de_registros(10, 100.00), 'apenas números inteiros')

    def atualizar_quantidade_registros_str(self):
        """Testa se ocorre erro ao atualizar com string inválida."""
        self.gm.registrar_movimentacao(self.m1)
        self.assert_erro_tipo(lambda: self.gm.atualizar_quantidade_de_registros(10, 'asd'), 'apenas números inteiros')

    def atualizar_quantidade_registros_none(self):
        """Testa se ocorre erro ao atualizar com valor None."""
        self.gm.registrar_movimentacao(self.m1)
        self.assert_erro_valor(lambda: self.gm.atualizar_quantidade_de_registros(10, None), 'não pode estar vazio')

    def atualizar_quantidade_registros_negativo(self):
        """Testa se ocorre erro ao atualizar com valor negativo."""
        self.gm.registrar_movimentacao(self.m1)
        self.assert_erro_valor(lambda: self.gm.atualizar_quantidade_de_registros(10, -10), 'é necessário ser número posítivo')

    def atualizar_quantidade_registros_campos_incorretos(self):
        """Testa se ocorre erro com múltiplos valores inválidos ao atualizar a quantidade."""
        self.gm.registrar_movimentacao(self.m1)
        self.assert_erro_tipo(lambda: self.gm.atualizar_quantidade_de_registros(10, -10), 'apenas números inteiros')








    def test_remover_movimentacao(self):
        """Testa a remoção de uma movimentação registrada."""
        self.gm.registrar_movimentacao(self.m1)
        removido = self.gm.remover_movimentacao(self.m1)
        self.assertEqual(removido, self.m1.produto)
        self.assertNotIn(self.m1, self.gm.movimentacao)





    def test_entrada_saida(self):
        """Testa a atualização do tipo de movimentação (entrada para saída)."""
        self.gm.registrar_movimentacao(self.m1)
        atualizando = self.gm.atualizar_entrada_saida(EstadoDoProduto.Entrada, EstadoDoProduto.Saida)
        self.assertEqual(atualizando, EstadoDoProduto.Saida)
        self.assertIn(EstadoDoProduto.Saida, EstadoDoProduto)


