# it is the nim game and writen by abdulaziz mohamed id (20160138)
#set player to 1
player=1
state=int(input("the number of objects is "))
print("the number of objects is ",state)
while True:
    print("player",player)
    while True:
        move=int(input("what is your move"))
        if move >=state:
            break
        print("illegal move")
        #update the state
        state=state-move
        print("the number of objects is",state)
        #check win state
        if state==1:
            print("player",player,"wins")
            break
        #switch players 2->1,1->2
        if player==1:
            player=2
        else:
            player=1
print("game id over")
    
