import pickle

from clientes import nome_ficheiro_lista_de_cliente
from veiculos import nome_ficheiro_lista_de_veiculos

def carrega_as_listas_dos_ficheiros():
    """
    funçao que irá carregar as listas dos ficheiros para as listas do programa 
    
    args:
    x (str): variavel que recebe...
    
    returns:
    list: uma lista que contem todos os registos dos veiculos
    """

    lista_de_veiculos = (nome_ficheiro_lista_de_veiculos)
    

    return  lista_de_veiculos 

def guarda_as_listas_em_ficheiros(lista_de_veiculos, lista_de_clientes, lista_de_faturas):
    """ documentação

    :param lista_de_clientes: vai ser guardada a lista com as informações dos clientes
    :param lista_de_veiculos: guardará a lista com as informações sobre os veiculos que a loja apresenta
    :param lista_de_faturas: armazena a lista de faturas/pagamentos efetuados pelos clientes
    """

    op = input("Os dados nos ficheiros serão sobrepostos. Continuar (s/N)?")
    if op in ['s', 'S']:
        guarda_em_ficheiro(nome_ficheiro_lista_de_veiculos, lista_de_veiculos)
        guarda_em_ficheiro('nome_ficheiro_lista_de_clientes', lista_de_clientes)
        'guarda_em_io_ficheiros'('nome_ficheiro_lista_de_faturas', lista_de_faturas)
    else:
        print("Gravação cancelada...")
       
    """a informação está como documentação pois não tenho acesso as demais funcões e ficheiros relacionados que o programa quer trabalhar"""

def guarda_em_ficheiro(nome_do_ficheiro, dados):
    """Guarda os dados recebidos num ficheiro

    :param nome_do_ficheiro: nome do ficheiro onde vai guardar os dados
    :param dados: dados a serem guardados
    """

    with open(nome_do_ficheiro, "wb") as f:
        pickle.dump(dados, f)

def le_de_ficheiro(nome_ficheiro):
    """Lê os dados de um ficheiro

    :param nome_ficheiro: nome do ficheiro onde estao os dados
    :return: o que leu do ficheiro (depende dos dados guardados)
    """

    with open(nome_ficheiro, "rb") as f:
        return pickle.load(f)
