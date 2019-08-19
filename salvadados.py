import csv



with open('teste_file.csv', mode='w') as teste_file:
        teste_writer = csv.writer(teste_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        nome = input('\nNome: ')
        endereco = input('\nEndereço: ')
        city = input('\nCidade: ')
        Estado = input('\nEstado: ')
        cep = input('\nCEP: ')

        teste_writer.writerow(['Nome', 'Endereço', 'Cidade','Estado','cep'])                
        teste_writer.writerow([nome, endereco, city,Estado,cep])
        









#with open('testecsv.csv', mode='w') as DADOSSALVOS_file:
       # DADOSSALVOS_writer = csv.writer(DADOSSALVOS_file, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
       # nome = input('\nNome: ')
       # endereco = input('\nEndereço: ')
       # city = input('\nCidade: ')
       # Estado = input('\nEstado: ')
       # cep = input('\nCEP: ')

        #DADOSSALVOS.writerow(['Nome', 'Endereço', 'Cidade','Estado','Cep'])
        #DADOSSALVOS.writerow([nome, endereco, city,Estado,cep])

#print('\nDigite as seguintes informações:')

#nome = input('\nNome: ')
#endereco = input('\nEndereço: ')
#city = input('\nCidade: ')
#Estado = input('\nEstado: ')
#cep = input('\nCEP: ')

#a = writerow([nome])
#a.writerow()

   

