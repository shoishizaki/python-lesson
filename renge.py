# for i in range(10):
#     print(i)

#print(type(range(10)))

def handmade_range(n):
    count = 0
    l = []
    while count < n:
        l.append(count)
        count += 1
    
    return l

#print(handmade_range(10))

for i in handmade_range(10):
    print(i)

print('###############')

for i in range(10):
    print(i)

count = 5
while count < 20:
    print(count)
    count += 2

