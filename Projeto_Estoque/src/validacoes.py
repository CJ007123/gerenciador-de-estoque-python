from enum import Enum
import math

class EstadoDoProduto(Enum):
    """
    Enum que representa o estado de movimentação de um produto.

    Valores:
        Entrada: Representa a entrada de produtos no estoque.
        Saida: Representa a saída de produtos do estoque.
    """
    Entrada = 'Entrada'
    Saida = 'Saída'


class Validador:
    """
    Classe utilitária com métodos estáticos para validar tipos, valores e estruturas de dados.

    Todos os métodos levantam exceções apropriadas (TypeError ou ValueError) 
    quando os dados fornecidos não atendem às regras esperadas.
    """

    @staticmethod
    def validar_str_campo_vazio(entrada, res='msg'):
        """
        Valida se uma string é válida e não está vazia.

        Args:
            entrada (str): Valor a ser validado.
            res (str): Nome do campo (usado na mensagem de erro).

        Raises:
            TypeError: Se entrada não for uma string.
            ValueError: Se entrada estiver vazia ou apenas com espaços.
        """
        if not isinstance(entrada, str):
            raise TypeError(f'"{res}" precisa ser um caracter')
        if not entrada.strip():
            raise ValueError(f'"{res}" não pode estar vazio')

    @staticmethod
    def validar_int(entrada_int, res='msg'):
        """
        Valida se um valor é um inteiro válido e positivo.

        Args:
            entrada_int (int): Valor a ser validado.
            res (str): Nome do campo.

        Raises:
            TypeError: Se não for inteiro.
            ValueError: Se for None ou negativo.
        """
        if entrada_int is None:
            raise ValueError(f'{res} não pode estar vazio')
        if not isinstance(entrada_int, int):
            raise TypeError(f'Digite a "{res}" apenas números inteiros')
        if entrada_int < 0:
            raise ValueError(f'"{res}" é necessário ser número positivo')

    @staticmethod
    def validar_float(entrada_float, res='msg'):
        """
        Valida se um valor é um número de ponto flutuante válido.

        Args:
            entrada_float (float): Valor a ser validado.
            res (str): Nome do campo.

        Raises:
            TypeError: Se não for float.
            ValueError: Se for None, negativo, infinito ou NaN.
        """
        if entrada_float is None:
            raise ValueError(f'{res} não pode estar vazio')
        if not isinstance(entrada_float, float):
            raise TypeError(f'"{res}" aceita apenas números de ponto flutuante')
        if math.isnan(entrada_float) or math.isinf(entrada_float):
            raise ValueError(f'{res} não pode ser número infinito ou inválido')
        if entrada_float < 0:
            raise ValueError(f'"{res}" é necessário ser número positivo')

    @staticmethod
    def validar_lista(lista, res='msg'):
        """
        Valida se uma lista está preenchida corretamente.

        Args:
            lista (list): Lista a ser validada.
            res (str): Nome da lista.

        Raises:
            TypeError: Se não for uma lista.
            ValueError: Se estiver vazia.
        """
        if not isinstance(lista, list):
            raise TypeError(f'{res} precisa ser uma lista')
        if not lista:
            raise ValueError(f'Não tem nada na lista: {res}')

    @staticmethod
    def validar_instancia_na_lista(objeto, tipo_esperado):
        """
        Valida se um objeto é do tipo esperado.

        Args:
            objeto (Any): Objeto a ser verificado.
            tipo_esperado (type): Tipo esperado da instância.

        Raises:
            ValueError: Se o objeto não for do tipo esperado.
        """
        if not isinstance(objeto, tipo_esperado):
            raise ValueError(f'Só é permitido adicionar objetos do tipo {tipo_esperado.__name__}')

    # @staticmethod
    # def validar_valor_positivo(valor):
    #     """
    #     Valida se um número float é positivo e finito.

    #     Args:
    #         valor (float): Valor a ser verificado.

    #     Observação:
    #         Este método apenas imprime a mensagem e não levanta exceção.
    #     """
    #     if isinstance(valor, float) and (math.isnan(valor) or math.isinf(valor)):
    #         print(f'{valor} não pode ser número infinito ou inválido')

    @staticmethod
    def validar_valores_duplicados(lista, atributo, valor, campo='msg'):
        """
        Valida se há duplicação de um atributo específico dentro de uma lista de objetos.

        Args:
            lista (list): Lista onde a verificação será feita.
            atributo (str): Nome do atributo do objeto a ser verificado.
            valor (Any): Valor a ser comparado.
            campo (str): Nome do campo usado na mensagem de erro.

        Raises:
            ValueError: Se o valor já existir na lista.
        """
        for item in lista:
            if getattr(item, atributo) == valor:
                raise ValueError(f'{campo} "{valor}" já existe e não pode ser duplicado.')
