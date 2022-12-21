#dict-exe9
dic={"Physics":82,"Math":65,"history":75}
val=dic.values()
min_val=min(val)
for k,v in dic.items():
    if v==min_val:
        print(k)
        break
