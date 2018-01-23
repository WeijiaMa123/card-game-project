import random
def deckplayer1(a,b):
    cards=random.randint(a,b)
    pai1=cards%7
    if pai1 == 0 or pai1 ==1:
        decision1=int(input("player1 got an attack card, do player1 want to use it 1.yes 2.no"))
        if decision1==1:
            print("from player1 to player2:ATTACK")
            global player2life
            decision2=int(input("Do player 2 want to use a block card,1.yes  2.no?"))
            if decision2==1:
                print("player1's attack is blocked")
                player2life=player2life
            else:
                player2life = player2life-1
        else:
            print("player1 keeps the attack card")
    elif pai1 == 2 or pai1==3:
        print("player1 gain block card")

    elif pai1 == 4:
        print("player1 use HEART")
        global player1life
        if player1life == 3:
            print("player1's maxium life is 3, the heart doesn't work")
        else:
            player1life=player1life+1
        
    elif pai1 == 5:
        print("form player 1 to player 2: ALIEN INVASION")
        decision=int(input("Do player2 want to use an attack card,1.yes  2.no"))
        if decision==1:
            print("player2 kill all the aliens")
            player2life = player2life
        else:
            print("player2 is invaded by aliens and lose one health")
            player2life -= 1       
        
    else: 
        print("peace")
        decisionp=int(input("do player1 wants to use peace card   1.yes  2.no"))
        if decisionp==1:
            if player1life==3 and player2life == 3:
                print("player1life and player2life both already reach maxium")
            elif player1life < 3 and player2life < 3:
                player1life= player1life+1
                player2life= player2life+1
            elif player1life <3 and player2life ==3:
                player1life= player1life+1
            else:
                player2life= player2life+1
        else:
            print("player 1 keep a card")
            
            
            

           
        
        
        
def deckplayer2(a,b):
    cards=random.randint(a,b)
    pai2=cards%7

    if pai2 == 0 or pai2 ==1:
        decision1=int(input("player2 got a attack card, do player2 want to use it 1.yes 2.no"))
        if decision1==1:
            print("from player2 to player1: ATTACK")
            decision2=int(input("Do player1 want to use a block card,1. yes 2. no"))
            global player1life
            if decision2== 1:
                print("player2's attack is blocked")
                player1life=player1life
            else:
                player1life= player1life-1
        else:
            print("player2 keeps the attack card")
    
    elif pai2 == 2 or pai2 ==3:
        print("player2 gain block card")
        
        
    elif pai2 == 4:
        print("player2 use HEART")
        global player2life
        if player2life == 3:
            print("player2life is already maxium, the heart don't work")
        else:
            player2life=player2life+1
    elif pai2 == 5:
        print("from player2 to player1:ALIEN INVASION")
        decision=int(input("do player1 want to use an attack card 1.yes 1.no"))

        if decision==1:
            player1life=player1life
        else:
            print("player1 is invaded and lose 1 health")
            player1life -= 1
        
    else: 
        print("peace")
        decisionp2=int(input("do player2 wants to use peace card   1.yes  2.no"))
        if decisionp2==1:
            if player1life==3 and player2life == 3:
                print("player1life and player2life both already reach maxium")
            elif player1life < 3 and player2life < 3:
                player1life= player1life+1
                player2life= player2life+1
            elif player1life <3 and player2life ==3:
                player1life= player1life+1
            else:
                player2life= player2life+1
        else:
            print("player 2 keep a card")
        
def the_engine():
    while player1life>0 and player2life>0:
        deckplayer1(1,7)
        deckplayer1(1,7)
        deckplayer2(1,7)
        deckplayer2(1,7)
        print("player1 health:",player1life)
        print("player2 health:",player2life)

        
print("This is a world of war. Empires are fighting for lands and resources. Now we have 2 army meeting.")
print("This war is gonna be one of the greatest fight in the human history. The prize for the winner is waiting for you.")
player1life = 3
player2life = 3

the_engine()

if player1life <= 0:
    again=input("To player 1: You lose the battle and becomes a salve. But do you still have the spirit to win! 1.Yes 2.No?")
    if again=="1":
        print("Chapter 2: Second Chance")
        print("Player1, you are a real fighter. You leads a slave evenge and gain a huge slave army.")
        print("Player 1 meets Player 2. Another battle begins!")
        the_engine()
    else:
        print("Slave life is horrible. But I don't care and just want to take a rest.")
        print("GAME OVER")
        
elif player2life <= 0:
    again2=input("To player 2: You lose the battle and becomes a salve. But do you still have the spirit to win! 1.Yes 2.No?")
    if again2=="1":
        print("Chapter 2: Second Chance")
        print("Player 2, you are a real fighter. You leads a slave evenge and gain a huge slave army.")
        print("Player 2 meets Player 1. Another battle begins!")
        the_engine()
    else:
        print("Slave life is horrible. But I don't care and just want to take a rest.")
        print("GAME OVER")
     
    
