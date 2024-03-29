# Apresentando os diferentes modos de fazer um print em python e com suas particularidades;
# \n = pular linha

# 1
print('Hello world!\n')
# ===============================================================================
# 2
# ===============================================================================
idade = 10
pets = 3
print('João tem ',10,'anos de idade\n')
# ===============================================================================
# 3 - (  My favorite :)  )
print(f'Maria tem {idade} anos de idade\n')
# ===============================================================================
# 4
print('Amanda tem {} anos de idade\n'.format(idade))
print('Amanda tem {} anos de idade e {} pets\n'.format(idade,pets))
# ===============================================================================
# 5 - Com valores específicos (strings, float, inteiros)
# %s = strings, %d inteiros, %f decimais
# %
troco = 3.45
nome = 'Paulo'
bolso = 5.65
print('Carlinhos recebeu de %f \n' %troco)
print('%s recebeu %f de troco \n'%(nome, troco))
# Agora alterando o número de casas depois da vírgula - '%0.2f' = Sem zero a esquerda(posições) e apenas 2 casas decimais.
print('O troco é de : %0.2f \n' %troco)
# %20f = o conteúdo começara a aparecer com o intervalo de 20 posições (espaços em branco) Sem zeros a esquerda;
print('O troco é de : %20f \n' %troco)
# %020f = o conteúdo começara a aparecer com o intervalo de 20 posições (espaços em branco) COM zeros a esquerda;
print('O troco é de : %020f \n' %troco)
# ===============================================================================
# 6 - Compor string, escohendo a posição (espaços em brancos) para iniciar o print.
# Assim adiciono mais de 5 posições posições em branco antes da palavra "tem" e reduzo para menor que 10 após a palavra.
# Depois adiciono 5 espaços em branco antes do valor decimal, e deixo apenas 2 casas decimais.
print('{:>5}tem {:<10} anos e apenas R$ {:5.2f} no bolso \n'.format(nome, idade, bolso))