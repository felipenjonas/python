# Jogo do 2 ou 1
# 3 amigos A,B e C estão jogando 2 ou 1, mostrar qual venceu, neste jogo
# Vence quem é diferente dos outros 2;

def startGame():
    vencedor = 0

    while(vencedor==0):
        A = int(input('Amigo A [2] ou [1]:'))
        B = int(input('Amigo B [2] ou [1]:'))
        C = int(input('Amigo C [2] ou [1]:'))

        if(A==B and A==C):
            print('\nJogo empatado, Sem vencedores!!')
            again = int(input('Jogar novamente? Sim [1] ou Não [0]:'))

            if(again==0):
                break
            else:
                if(again==1):
                    vencedor = 0
        else:
            if(A==B):
                print('\nC é o vencedor!!')
                again = int(input('Jogar novamente? Sim [1] ou Não [0]:'))
                if(again==0):
                    break
                else:
                    if(again==1):
                        vencedor = 0                
            else:
                if(B==C):
                    print('\nA é o vencedor!!')
                    again = int(input('Jogar novamente? Sim [1] ou Não [0]:'))
                    if(again==0):
                        break
                    else:
                        if(again==1):
                            vencedor = 0
                else:
                    if(A==C):
                        print('B é o vencedor!!')
                        again = int(input('Jogar novamente? Sim [1] ou Não [0]:'))
                        if(again==0):
                            break
                        else:
                            if(again==1):
                                vencedor = 0
                

         
        
            

        

startGame()    
    