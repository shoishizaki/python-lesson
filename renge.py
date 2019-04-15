# for i in range(10):
#     print(i)

#print(type(range(10)))

def handmade_range(n):
    count = 0
    l = []
    while True:
        if count < n:
            l.append(count)
            count += 1
        else:
            print(l)
            break

handmade_range(10)




