# dict-exe10
dic={
    "emp1":{"name":'Jhon','salary':7500},
    "emp2":{'name':'Emma','salary':8000},
    'emp3':{'name':'Brad','salary':5000}
}

for emp in dic.keys():
    if dic[emp]['name']=='Brad':
        dic[emp]['salary']=8500
print(dic)
