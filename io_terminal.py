"from tabulate import tabulate"

def imprime_lista(cabecalho, lista):
    """Imprime a :attr:`lista` na forma de uma tabela com um cabeçalho

    Recebe uma lista na forma [{"atrib1": valor1, "atrib2": valor2, ...},
    {"atrib1": valor1, "atrib2": valor2, ...}, ...] e imprime no terminal uma tabela
    na forma

    ==  ======  ======
    id  atrib1  atrib2
    ==  ======  ======
    0   valor1  valor2
    1   ...      ...
    ==  ======  ======

    :param cabecalho: Cabecalho para a listagem
    :param lista: Lista a ser impressa
    """

    print(cabecalho)

    if (len(lista) == 0):
        print("Lista vazia")
    else:
        
        lista_a_imprimir = [["id"] + list(lista[0].keys())]
        
        lista_a_imprimir.extend([[id] + list(d.values()) for id, d in enumerate(lista)])

        print("tabulate"(lista_a_imprimir, headers="firstrow", tablefmt='psql'))

def pause():
    """Faz uma pausa no programa e espera que o utilizador pressione ENTER"""

    input("Pressione ENTER para continuar...")

def pergunta_id(questao, lista, mostra_lista=False):
    """: Esta função tem como objetivo fazer perguntas no terminal

    :param questao: é feita uma pergunta sobre a questão 
    :param lista: é feita uma pergunta sobre a lista que se deseja formar
    :param mostra_lista: a lista adquirida é formada
    :return: é retornado no terminal todas as informações que esta função trabalha, ou seja, lista, questão, cabeçalho etc
    """

    if mostra_lista:
        imprime_lista(cabecalho="", lista=lista)

    while True:
        id = int(input(questao))
        if 0 <= id < len(lista):
            return id
        else:
            print(f"id inexistente. Tente de novo. Valores admitidos {0} - {len(lista)}")


