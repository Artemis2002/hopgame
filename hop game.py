zarib = int(input('zarib hope ra wared konid:\n'))
while True:
    x = random.randint(1 , 100)
    if (x % zarib) == 0:
        continue
    else:
        break
counter = 0
while True:
    if (x % zarib) == 0:
        print("CPU: hope" )
        x = x+1
    else:
        print("CPU:" + str(x))
        x = x+1
    a = input("its player turn:\n")
    if a != 'hope':
        if int(a) != x:
            print("player lost \n")
            print("best score: " + str(counter))
            break
        else:
            print("Player: " + str(a))
            counter = counter + 1
            x = x+1
    elif (x % zarib) == 0 and a != "hope":
        print("player lost \n")
        print("best score: " + str(counter))
        break
    else:
        print("Player: " + str(a))
        counter = counter + 1
        x = x+1