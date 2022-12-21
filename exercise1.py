#exercise1
l1=[3,6,9,12,15,18,21]
l2=[4,8,12,16,20,24,28]
l1odd=[]
l2even=[]
for i in l1:
    if l1.index(i)%2!=0:
        l1odd.append(i)
for j in l2:
    if l2.index(j)%2==0:
        l2even.append(j)
l_out=l1odd+l2even
print("Element at odd-index positions from list one",l1odd,
"Element at even-index positions from list two",l2even,"\n","Printing Final third list",l_out,sep="\n")
        