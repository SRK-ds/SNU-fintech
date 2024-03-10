
lst = [1,2,3]
lst.append(5)

lst_A = lst
lst_A.reverse()
lst_A.pop()


lst_B = lst_A[:2]
lst_B = lst_B * 2
lst_B.insert(2,1)

print(lst_A)
print(lst_B)

lst4 = [1,2,3,4,5]
for i in range(4,0,-1):
    if i == 3:
        continue
    elif i < 2:
        break
    lst4[i] = lst4[i]+1

print(lst4)