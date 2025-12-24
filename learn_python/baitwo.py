#Allow the user to input an arbitrary value
lst = [5, 7, 8, 9, 10, 20, 15, 8, 7, 4, 3, 8, 10, 15, 17, 19]
a = int(input("Số bạn muốn là: "))
if a in lst:
    print("Số {a} ở trong list")
else:
    print(f"Số {a} không ở trong list 3")
#Create a new list that is the reverse of the original list.

daonguoc = []
for i in range(len(lst)-1, -1,-1):
    daonguoc.append(lst[i])
print("List đảo ngược là:", daonguoc)
#Sort the original list in ascending order

for i in range(len(lst)-1):
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp
print("List tăng dần là:", lst)