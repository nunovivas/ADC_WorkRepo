def cria_novo_cliente():
    """Pedir os dados de um novo cliente

    :return: dicionario com o novo cliente, {"nome": <<nome>>, "nif": <<nif>>, ...}
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