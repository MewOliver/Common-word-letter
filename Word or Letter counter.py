
from asyncio.windows_events import NULL


active = True
while active is True:
    try:
        fhand = open(input('type the file you want to look at (txt file only) '))
        active = False
    except:
        print('type a valid file')

active = True
while active is True:
    choice = input('Would you like to view the most common words or letters? ')
    if choice == 'words':
        active = False
    elif choice == 'letters':
        active = False
    else:
        print("type either 'words' or 'letters' ")

    
active = True
while active is True:
    char = input('Would you like to include special characters? ')
    if char == 'yes':
        active = False
    elif char == 'no':
        active = False
    else:
        print("type 'yes' or 'no' ")

active = True
while active is True:
    try:
        amount = int(input("How many results do you want? "))
        active = False
    except:
        print('type a valid number')
        

alph = "abcdefghijklmnopqrstuvwxyz"
spel = '!''@''#''$''%''^''&''*''('')''_''-''['']''{''}'';'':''"'',''.''<''>''/''?''|''+''='"'"

if choice == 'words':
    lines = list()
    count = dict()
    sort = list()
    clean = list()

    for i in fhand:
        line = i.lower()
        line = line.rstrip().split()
        lines = lines + line


    for i in lines:
        if char == 'no':
            if i[len(i)-1] in spel:
                x = i[:-1]   
            elif i[0] in spel:
                x = i[1:]
            else:
                x = i
        else:
            x = i
        clean = clean + x.split()

    for i in clean:
        count[i] = count.get(i, 0) + 1

    for k, v in count.items():
        newtup = (v, k)
        sort.append(newtup)

    sort = sorted(sort, reverse=True)

    print(sort[:int(amount)])

    done = input('')

elif choice == 'letters':
    lines = list()
    count = dict()
    sort = list()
    letters = list()

    for i in fhand:
        line = i.lower()
        lines = lines + line.rstrip().split()

    for i in lines:
        for x in i:
            if char == 'no':
                if x in spel:
                    x is NULL 
                else:
                    letters.append(x)
            else:
                letters.append(x)

    for i in letters:
        count[i] = count.get(i, 0) + 1

    for k, v in count.items():
        newtup = (v, k)
        sort.append(newtup)

    sort = sorted(sort, reverse=True)

    print(sort[:int(amount)])

done = input('')