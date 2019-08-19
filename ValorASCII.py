while(1):  
  valordigi = (input('\nDigite algo no teclado: '))
  para = '000'

  print('\n\n\nO valor ASCII de [ {} ] é:'.format(valordigi))
  print('>>>'),print(ord(valordigi))
  print('---------------------------------------------\n')
  print('\n\n\nPara sair tecle: [000]')
  if (valordigi == para):
    break


