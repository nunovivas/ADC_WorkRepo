from datetime import date

from io_terminal import imprime_lista, pergunta_id

nome_ficheiro_lista_de_faturas = "lista_de_faturas.pk"
def cria_nova_fatura(lista_de_clientes, lista_de_veiculos):
  


    id_cliente = pergunta_id(questao="Qual o id do cliente?", lista=lista_de_clientes, mostra_lista=True)
    id_veiculo = pergunta_id(questao="Qual o id do veiculo?", lista=lista_de_veiculos, mostra_lista=True)

  
    fatura = {"cliente": id_cliente,
              "veiculo": id_veiculo,
              "data": date.today()}

    return fatura