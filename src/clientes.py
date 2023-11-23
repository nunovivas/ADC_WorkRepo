from io_terminal import imprime_lista

nome_ficheiro_lista_de_clientes = "lista_de_clientes.pk"

# TODO: Copie para aqui o código de cada uma das funções nos
# ficheiros com o nome clientes-*.py e faça um commit de cada vez
# Quando este ficheiro estiver completo com todas as suas funções,
# deve ser o unico ficheiro clientes.py existente, deve apagar
# todos os outros ficheiros clientes-*.py, e inclusive estes comentários

# ...

#### (Esta função pergunta uma lista de clientes com os seguintes dados: Primeiro e ultimo nome, email, telemovel e nif)
def cria_novo_cliente():
    """Pedir os dados de um novo cliente

    :return: dicionario com o novo cliente, {"firstName": <<nome>>,"lastName":<<nome>>, "email",<<email>>, "mobilePhone", <<mobilePhone>>,"nif",<<nif>>, ...}
    """
    # TODO: pedir os dados do cliente e não esquecer de os devolver
    # ...
    primeiroNome = input("Primeiro nome?: ")
    ultimoNome= input("Ultimo nome? :")
    email = input ("Correio Electronico? : ")
    telemovel = input ("Telemóvel? :")
    nif = input ("NIF? :")
    
    newClient = {"firstName", primeiroNome,"lastName", ultimoNome,"email", email,"mobilePhone",telemovel,"nif",nif}
    return newClient

### Imprime uma lista de cliente (que é recebida pelo tipo de dados dicionario)
def imprime_lista_de_clientes(lista_de_clientes):
    """TODO: documentação"""
    imprime_lista(cabecalho="Lista de clientes", lista=lista_de_clientes)


