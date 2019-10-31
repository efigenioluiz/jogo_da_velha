#!/usr/bin/env python3
import sys
import errno
from random import randint

if __name__ == "__main__":
    flag=1
    jogador=str(input("Jogador 1 Nome:"))
    jogador2=str(input("Jogador 2 Nome:"))
    vez=0
    a=' '
    b=' '
    c=' '
    d=' '
    e=' '
    f=' '
    g=' '
    h=' '
    i=' '   
    while flag > 0:
            clear() 
            print("*"*30)
            print("* \033[4m {0} \033[0m|\033[4m {1} \033[0m|\033[4m {2} \033[0m ** \033[4m a \033[0m|\033[4m b \033[0m|\033[4m c \033[0m *".format(a,b,c))
            print("* \033[4m {0} \033[0m|\033[4m {1} \033[0m|\033[4m {2} \033[0m ** \033[4m d \033[0m|\033[4m e \033[0m|\033[4m f \033[0m *".format(d,e,f))
            print("*  {0} | {1} | {2}  **  g | h | i  *".format(g,h,i)) 
            print("*"*30)
            if a =='X' and b == 'X' and c== 'X' or d =='X' and e == 'X' and f== 'X' or g =='X' and h == 'X' and i== 'X':
                    print('VOCÊ GANHOU {0}'.format(jogador.upper()))
                    break
            elif  a =='O' and b == 'O' and c== 'O' or d =='O' and e == 'O' and f== 'O' or g =='O' and h == 'O' and i== 'O':
                    print('VOCÊ GANHOU {0}'.format(jogador2.upper()))
                    break                   
            if vez ==0:
                    while True:        
                            jogada=str(input("É a vez do jogador {0}:".format(jogador)))
                            if jogada == 'a' and a ==' ':
                                    a='X'
                                    break   
                            elif jogada == 'b' and b ==' ':
                                    b='X'
                                    break
                            elif jogada == 'c' and c ==' ':
                                    c='X'
                                    break
                            elif jogada == 'd' and d ==' ':
                                    d='X'
                                    break
                            elif jogada == 'e' and e ==' ':
                                    e='X'
                                    break
                            elif jogada == 'f' and f ==' ':
                                    f='X'
                                    break
                            elif jogada == 'g' and g ==' ':
                                    g='X'
                                    break
                            elif jogada == 'h' and h ==' ':
                                    h='X'
                                    break
                            elif jogada == 'i':              
                                    i='X'
                                    break
                    vez=1
            elif vez == 1:
                    while True:        
                            jogada=str(input("É a vez do jogador {0}:".format(jogador2))) 
                            if jogada == 'a' and a ==' ':
                                    a='O'
                                    break
                            elif jogada == 'b' and b ==' ':
                                    b='O'
                                    break
                            elif jogada == 'c' and c ==' ':
                                    c='O'
                                    break
                            elif jogada == 'd' and d ==' ':
                                    d='O'
                                    break
                            elif jogada == 'e' and e ==' ':
                                    e='O'
                                    break
                            elif jogada == 'f' and f ==' ':
                                    f='O'
                                    break
                            elif jogada == 'g' and g ==' ':
                                    g='O'
                                    break
                            elif jogada == 'h' and h ==' ':
                                    h='O'
                                    break
                            elif jogada == 'i':              
                                    i='O'
                                    break   
                    vez=0
