#exercise9
speed={"jan":47,"feb":52,"march":47,"April":44,"May":52,"June":53,"July":54,"Aug":44,"Sept":54}
l=[]
for i in speed.values():
    if i not in l:
        l.append(i)
print(l)