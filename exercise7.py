set1={27,43,34}
set2={34,93,22,27,43,53,48}
c1=set1.issubset(set2)
c2=set2.issubset(set1)
c3=set1.issuperset(set2)
c4=set2.issuperset(set1)
print("First set is subset of second set -",c1)
print("Second set is subset of First set -",c2)
print("First set is superset of second set -",c3)
print("Second set is superset of First set -",c4)
if c1==True:
    set1.clear()
elif c2==True:
    set2.clear()

print("First set",set1)
print("Second set",set2)

