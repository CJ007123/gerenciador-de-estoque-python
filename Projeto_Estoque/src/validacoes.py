from enum import Enum
import math
class EstadoDoProduto(Enum):
    Entrada = 'Entrada'
    Saida = 'Saída'

class Validador:
    @staticmethod
    def validar_str_campo_vazio(entrada, res='msg'):
        if not isinstance(entrada, str):
            raise TypeError(f'"{res}" Precisa ser um caracter')
        if not entrada.strip():
            raise ValueError(f'"{res}" Não pode estar vazio')
        
    @staticmethod
    def validar_int(entrada_int, res='msg'):
        if entrada_int is None:
            raise ValueError(f'{res} não pode estar vazio')
        if not isinstance(entrada_int, int):
            raise TypeError(f'Digite a "{res}" apenas números inteiros ')
        if entrada_int < 0:
            raise ValueError(f'"{res}" é necessário ser número posítivo')

    @staticmethod
    def validar_float(entrada_float, res='msg'):
        if entrada_float is None:
            raise ValueError(f'{res} não pode estar vazio')
        
        if not isinstance(entrada_float, float):
            raise TypeError(f'"{res}" aceita apenas números de ponto flutuante')
        
        if math.isnan(entrada_float) or math.isinf(entrada_float):
            raise ValueError(f'{res} não pode ser número infinito ou inválido')
        
        if entrada_float < 0:
            raise ValueError(f'"{res}" é necessário ser número posítivo')
        

        
    @staticmethod
    def validar_lista(lista, res='msg'):
        if not isinstance(lista, list):
            raise TypeError(f'{res} Precisa ser uma lista')
        if not lista:
            raise ValueError(f'Não tem nada na lista: {res}')
    
    @staticmethod
    def validar_instancia_na_lista(objeto, tipo_esperado):
        if not isinstance(objeto, tipo_esperado):
            raise ValueError('Só é permitido adicionar objetos do tipo {tipo_esperado.__name__}')
    
    @staticmethod
    def validar_valor_positivo(valor):
        if isinstance(valor, float) and (math.isnan(valor) or math.isinf(valor)):
            print(f'{valor} não pode ser número infinito ou inválido')
    
    @staticmethod
    def validar_valores_duplicados(lista, atributo,valor, campo='msg'):
        for item in lista:
            if getattr(item, atributo) == valor:
                raise ValueError(f'{campo} "{valor}" já existe e não pode ser duplicado.')

