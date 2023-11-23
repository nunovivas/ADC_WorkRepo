import pickle

nome_ficheiro_lista_de_veiculos = "lista_de_veiculos.pk"

def cria_novo_veiculo():
    marca = input("marca? ")
    matricula = input("matricula? ").upper()
    combustivel = input("combustivel? ")  
    categoria = input("categoria?")
    veiculo = {"marca": marca,
               "matricula": matricula,
               "combustivel": combustivel,
               "categoria": categoria}  
    return veiculo

def imprime_lista_de_veiculos(lista_de_veiculos):
    imprime_lista(cabecalho="Lista de Veiculos", lista=lista_de_veiculos)

def imprime_lista(cabecalho, lista):
    print(cabecalho)
    for veiculo in lista:
        print(f"Marca: {veiculo['marca']}, Matrícula: {veiculo['matricula']}, Combustível: {veiculo['combustivel']}, Categoria: {veiculo['categoria']}")  
        print("-" * 82)

def salvar_lista_de_veiculos(lista_de_veiculos):
    with open(nome_ficheiro_lista_de_veiculos, "wb") as f:
        pickle.dump(lista_de_veiculos, f)

def carregar_lista_de_veiculos():
    try:
        with open(nome_ficheiro_lista_de_veiculos, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

lista_de_veiculos_exemplo = [
    {"marca": "Toyota", "matricula": "ABC123", "combustivel": "Gasolina", "categoria": "Carro compacto"},  
    {"marca": "Ford", "matricula": "DEF456", "combustivel": "Diesel", "categoria": "Carro esportivo"},  
    # Adicione mais veículos conforme necessário o cliente presisar
]

salvar_lista_de_veiculos(lista_de_veiculos_exemplo)

lista_carregada = carregar_lista_de_veiculos()

# Imprimir a lista de veículos carregada
imprime_lista_de_veiculos(lista_carregada)
