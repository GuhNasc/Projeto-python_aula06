import csv

# Lendo csv e processando os dados
path_arquivo = "vendas.csv"

def ler_arquivo_csv(nome_arquivo_csv: str) -> list[dict]:
    """
    Função que le um arquivo csv e retorna uma lista de dicionarios
    """
    
    lista = []
    with open (nome_arquivo_csv, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista

vendas_itens = list[dict]

vendas_itens = ler_arquivo_csv(path_arquivo)
print(vendas_itens)

# Calcular vendas (CALCULO DE KPI)

def filtrar_produtos_nao_entregues(lista: list[dict]) -> list[dict]:
    """
    Função que filtra produtos que foram entregues
    """
    lista_filtrada = []
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_filtrada.append(produto)
    return lista_filtrada


def somar_valores_price(lista_filtrada: list[dict]) -> list[dict]:
    """
    Soma de todos os produtos da lista
    """
    valor_total = 0
    for produto in lista_filtrada:
        valor_total += int(produto.get("price"))
    return valor_total

# Fazendo a analise final

lista_de_produtos = ler_arquivo_csv(path_arquivo)
produtos_entregues = filtrar_produtos_nao_entregues(lista_de_produtos)
valor_dos_produtos_entregues = somar_valores_price(produtos_entregues)

print(valor_dos_produtos_entregues)

