while(1):
    print('\n[1] = Encriptar')
    print('[2] = Decriptar')
    print('[3] = sair')
    perg = input('Escolha a operação: ')
    novotext=''
    
    if(perg == '1' ):
        print('\n--------------OPERAÇÃO: ENCRIPTAR--------------')
        valordigia = (input('\nDigite o texto: '))
        for x in valordigia:
            #print(x)
            codificado = ord(x)
            #print(codificado)
            codificado = codificado+3
            decodificado = chr(codificado)
            #print(decodificado)
            novotext=novotext + decodificado
            print('---------------------------------------------')
            print('O valor Encriptado é: {}'.format(novotext))
            print('---------------------------------------------')
            
    if(perg == '2'):
        print('\n--------------OPERAÇÃO: DECRIPTAR--------------')
        valordigib = (input('\nDigite o texto: '))
        for x in valordigib:
            codificado = ord(x)
            codificado = codificado-3
            decodificado = chr(codificado)
            novotext=novotext+decodificado
            print('---------------------------------------------')
            print('O valor Decriptado é: {}'.format(novotext))
            print('---------------------------------------------')
            
    if(perg == '3'):
        break


    
     

    


