list1=[87,45,41,65,94,41,99,94]
luni=[]
for i in list1:
    if i not in luni:
        luni.append(i)
print("unique items",luni)
print("tuple",tuple(luni))
print("min:",min(luni))
print("max:",max(luni))
