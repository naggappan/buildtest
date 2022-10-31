a = [1,2,4,5,3,4,5,2,4,5]
print(a)
#numbers which are not duplicated
count = {}
for i in a:
    if i in count:
        count[i] = count[i] + 1
    else:
        count[i] = 1

#print(count)

for key, value in count.items():
    if value ==1:
        print (key)
