import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))



import unittest
from movimentacao import *
from datetime import datetime
from validacoes import EstadoDoProduto
from teste_categoria import TestBaseGerenciador


class TestMovimentacao(TestBaseGerenciador):
    def setUp(self):
        self.m1 = Movimentacao(produto='nome', tipo=EstadoDoProduto.Entrada.value, quantidade_registros=10,data=datetime.now())
        self.gm = GerenciandoMovimentacao()
    
    def test_adicionando_movimentacao(self):
        self.gm.registrar_movimentacao(self.m1)
        self.assertIn(self.m1, self.gm.movimentacao)
        self.assertEqual(len(self.gm.movimentacao),1)
    
    def test_adicionando_movimentacao_duplicadas(self):
        self.gm.registrar_movimentacao(self.m1)
        movimentacao_duplicados = Movimentacao(produto='nome', tipo=EstadoDoProduto.Entrada.value, quantidade_registros=10,data=datetime.now())
        self.assert_erro_valor(lambda: self.gm.registrar_movimentacao(movimentacao_duplicados), 'já existe e não pode ser duplicado.')
    
    def test_listar_movimentacao(self):
        self.gm.registrar_movimentacao(self.m1)
        resultado = self.gm.listar_movimentacao()
        esperado = [f'Produto:{self.m1.produto}\nTipo: {self.m1.tipo}\nQuantidade de registros: {self.m1.quantidade_registros} Data: {self.m1.data}\n']
        self.assertEqual(esperado,resultado)




    def test_atualizar_quantidade_registros(self):
        self.gm.registrar_movimentacao(self.m1)
        self.gm.atualizar_quantidade_de_registros(10, 100)
        self.assertEqual(self.m1.quantidade_registros, 100)
    
    def atualizar_quantidade_registros_float(self):
        self.gm.registrar_movimentacao(self.m1)
        self.assert_erro_tipo(lambda: self.gm.atualizar_quantidade_de_registros(10, 100.00), 'apenas números inteiros')


    def atualizar_quantidade_registros_str(self):
        self.gm.registrar_movimentacao(self.m1)
        self.assert_erro_tipo(lambda: self.gm.atualizar_quantidade_de_registros(10, 'asd'), 'apenas números inteiros')

    def atualizar_quantidade_registros_none(self):
        self.gm.registrar_movimentacao(self.m1)
        self.assert_erro_valor(lambda: self.gm.atualizar_quantidade_de_registros(10, None), 'não pode estar vazio')

    def atualizar_quantidade_registros_negativo(self):
        self.gm.registrar_movimentacao(self.m1)
        self.assert_erro_valor(lambda: self.gm.atualizar_quantidade_de_registros(10, -10), 'é necessário ser número posítivo')

    def atualizar_quantidade_registros_campos_incorretos(self):
        self.gm.registrar_movimentacao(self.m1)
        self.assert_erro_tipo(lambda: self.gm.atualizar_quantidade_de_registros(10, -10), 'apenas números inteiros')




    
    def test_remover_movimentacao(self):
        self.gm.registrar_movimentacao(self.m1)
        remover_movimentacao = self.gm.remover_movimentacao(self.m1)
        self.assertEqual(remover_movimentacao, self.m1.produto)
        self.assertNotIn(self.m1, self.gm.movimentacao)
    
    def test_entrada_saida(self):
        self.gm.registrar_movimentacao(self.m1)
        atualizando = self.gm.atualizar_entrada_saida(EstadoDoProduto.Entrada, EstadoDoProduto.Saida)
        self.assertEqual(atualizando, EstadoDoProduto.Saida)
        self.assertIn(EstadoDoProduto.Saida, EstadoDoProduto)

