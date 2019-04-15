d = { 
    1 : 'apple',
    2 : 'banana',
    3 : 'orange'
}

d[4] = 'graph'
# print(d[4])

#for key in d.keys():
 #   print(key)

for key,value in d.items():
    if key % 2 == 0:
        print(value)
