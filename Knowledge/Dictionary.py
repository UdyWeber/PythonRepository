tupla = (1, 3, 2, 5)
print(tupla)
lista = [1, 3, 2, 5]
print(lista)
dicionario = {"um": None, "tres": [3, 13], "dois":None, "cinco": [5, 25]}
print(dicionario)

for key in dicionario:

    print(f"A chave encontrada foi {key}")

    if dicionario[key]:
        for value in dicionario[key]:
            print(f"Dentro da chave {key} foi encontrado o valor {value}")
    else:
        print(f"Nao foi encontrado nenhum valor na chave {key}")