
import time


def playgame():
    print('Which Game Would you like to play Today :')
    print(''' 
    list of available games:
            \n1.bagels
            \n2.blackjack
            \n3.connect4
            \n4.flappy
            \n5.pong
           

        OR type "quit" to exit gamemanager.

             ''')
    
    uinp=input("Enter the number in front of the game you'll like to play\n>>")
    
    if '1' in uinp :
        from games import bagels
    

    elif '2' in uinp:
        from games import blackjack

    elif '3' in uinp:
        from games import connect4

    elif '4' in uinp:
        from games import flappy

    elif '5' in uinp:
        from games import pong             
    
   
    elif uinp>8:
        print('this slot is empty... Pay Dev to Add More Games XD')

    elif uinp=="quit":
        quit()

    else:
        print('you need to choose a number from the list above NOOB! ')
        return playgame
    time.sleep(3)



playgame()
#after running this contine use krna,