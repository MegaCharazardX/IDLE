_ = input("Enter Sequence : ")

_list = []

cnt = 1
tempLetter = ""
for i in _:
    if i == tempLetter:
        cnt+=1
    else:
        _list.append(f"{cnt}{i}")
    tempLetter = i