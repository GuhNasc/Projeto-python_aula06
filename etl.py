from projeto import ler_arquivo_csv,filtrar_produtos_nao_entregues,somar_valores_price

#
path_arquivo = "vendas.csv"

lista_de_produtos = ler_arquivo_csv(path_arquivo)
produtos_entregues = filtrar_produtos_nao_entregues(lista_de_produtos)
valor_dos_produtos_entregues = somar_valores_price(produtos_entregues)
print(valor_dos_produtos_entregues)