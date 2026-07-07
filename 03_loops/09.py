items = ["apple", "banana", "orange", "banana", "mango"]
flag = False
for i in items:
    if items.count(i)> 1:
        flag = True
        break
print(flag, i)