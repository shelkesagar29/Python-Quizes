import getpass 
while True:
    print("""Valid inputs are:
    rock
    paper
    scissors""")
    #inp1=input("Player1 enter your choice\n")
    inp1=getpass.getpass("Player1 enter your choice\n")
    #inp2=input("Player2 enter your choice\n")
    inp2=getpass.getpass("Player2 enter your choice\n")

    if inp1==inp2:
        print("Oops! Draw it is...")
        
    if inp1=='rock':
        if inp2=='scissors':
            print ("rock beats scissors,congratulations Player 1!\n")
        elif inp2=='paper':
            print ("paper beats rock, congratulations Player 2!\n")
    elif inp1=='scissors':
        if inp2=='rock':
            print ("rock beats scissors,congratulations Player 2!\n")
        elif inp2=='paper':
            print ("scissors beats paper, congratulations Player 1!\n")
    elif inp1=='paper':
        if inp2=='scissors':
            print ("scissors beats paper,congratulations Player 2!\n")
        elif inp2=='rock':
            print ("paper beats rock, congratulations Player 1!\n")
    
    
    #inpu=input("Do you want to play next game? (y/n)\n")
    inpu=getpass.getpass("Do you want to play next game? (y/n)\n")
    if inpu=='n':
        break
    else:
        pass
        