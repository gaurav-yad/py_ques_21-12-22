roll_num=[47,64,69,37,76,83,95,97]
dic={"John":47,"Emma":69,"Kelly":76,"Jason":97}
for i in roll_num:
    if i not in dic.values():
        roll_num.remove(i)
print("After removing unwanted elements from the list",roll_num)

