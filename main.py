from clientes import cria_novo_cliente, imprime_lista_de_clientes
"""from faturas import cria_nova_fatura, imprime_lista_de_faturas
from io_ficheiros import (carrega_as_listas_dos_ficheiros,
                          guarda_as_listas_em_ficheiros)
from io_terminal import pause"""
from veiculos import cria_novo_veiculo, imprime_lista_de_veiculos

def menu():
    """Menu principal da aplicação"""

    while True:
        print("""
        *********************************************************************
        :    (-: OFICINA BARATINHA - RESISTIMOS A QUALQUER ORÇAMENTO :-)    :
        *********************************************************************
        :                                                                   :
        : nc - novo cliente         lc - listagem de clientes               :
        : nv - novo veiculo         lv - listagem de veiculos               :
        : nf - nova fatura          lf - listagem das faturas               :
        : ...                                                               :
        : g - guarda tudo           c - carrega tudo                        :
        : x - sair                                                          :
        :                                                                   :
        *********************************************************************
        """)

        op = input("opcao?").lower()

        if op == "x":
            exit()

        elif op == "g":
            pass

        elif op == "c":
           pass

        elif op == "nc":
            pass

        elif op == "nv":
            pass

        elif op == "nf":
            pass

        elif op == "lc":
            pass

        elif op == "lv":
            pass

        elif op == "lf":
            pass
