fhand = open('lyrics.txt')

lyrics = list()
count = dict()
sort = list()
letters = list()

for i in fhand:
    line = i.lower()        
    lyrics = lyrics + line.rstrip().split()

for i in lyrics:
    for x in i:
        letters.append(x)
        
for i in letters:
    count[i] = count.get(i, 0) + 1

for k, v in count.items():
    newtup = (v, k)
    sort.append(newtup)

sort = sorted(sort, reverse=True) 
print(sort)

print(len(sort))
'''
fhand = open('lyrics.txt')

lyrics = list()
count = dict()
sort = list()

for i in fhand:
    line = i.lower()        
    lyrics = lyrics + line.rstrip().split()


for i in lyrics:
    count[i] = count.get(i, 0) + 1

for k, v in count.items():
    newtup = (v, k) 
    sort.append(newtup)   
    
sort = sorted(sort, reverse=True)
print(sort)
'''