# Sobre estrutura de dados em python
# Chave: Valor
# Chaves podem ser string ou numero, e valores tbm
dicionario = {}

# print(dicionario)


pessoa = { 
    'nome':'Felipe',
    'idade': 20,
    'dataNascimento': '15/05/200'
}

print(pessoa)

#Consultas valores de chaves do dicionário 
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['dataNascimento'])

# Adicionar novas chaves e valores dentor do dicionário:
pessoa['corFavorita'] = 'Preto'

print(pessoa)

# Outros métodos:

# Mostra as chaves, também seus valores
print(pessoa.keys())


# # Mostrar os valroes
print(pessoa.values())

# # LIMPAR ou deleta:
print(pessoa.clear())
